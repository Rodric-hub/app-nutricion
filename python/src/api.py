"""
api.py
API HTTP (FastAPI) que expone el flujo completo del sistema:
Python (datos) -> Scala (rutinas) -> Prolog (recomendaciones) -> resultado final

Reemplaza al menu interactivo de consola (main.py) para que el
frontend en React pueda consumir el mismo flujo via HTTP.

Como ejecutar:
    cd python
    pip install -r requirements.txt
    uvicorn src.api:app --reload --port 8000
"""

import sys
import os
import subprocess
import json

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

from utils.calculadora_calorias import reporte_completo
from utils.planes_alimenticios import generar_plan, PLANES
from integracion.prolog_connector import recomendar_ejercicios, recomendar_alimentos
from integracion.scala_connector import guardar_usuario_json, guardar_resultado_python, DATA_DIR


app = FastAPI(
    title="App Gimnasio Multilenguaje - API",
    description="Orquesta Python, Scala y Prolog para generar reportes de fitness y nutrición.",
    version="1.0.0",
)

# CORS abierto para desarrollo local (Vite corre normalmente en :5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Esquemas de entrada/salida ────────────────────────────────────────────────

class UsuarioInput(BaseModel):
    nombre: str = Field(..., min_length=1, examples=["Ana López"])
    edad: int = Field(..., gt=0, lt=120)
    peso: float = Field(..., gt=0, examples=[65.0])
    altura: float = Field(..., gt=0, examples=[165.0])
    genero: Literal["masculino", "femenino"]
    objetivo: Literal["perder_peso", "ganar_musculo", "mantenimiento"]
    nivel_actividad: Literal["sedentario", "ligero", "moderado", "activo", "muy_activo"] = "moderado"


# ── Llamar a Scala (igual que en main.py) ────────────────────────────────────

def llamar_scala(ruta_json: str) -> bool:
    jar_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "../../scala/target/scala-2.13/gimnasio.jar"
    ))
    if not os.path.exists(jar_path):
        return False
    try:
        ruta_json_norm = ruta_json.replace("\\", "/")
        result = subprocess.run(
            ["java", "-jar", jar_path, ruta_json_norm],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0
    except Exception:
        return False


def leer_resultado_scala(nombre: str) -> dict:
    ruta = os.path.join(DATA_DIR, "salida", f"resultado_scala_{nombre.replace(' ', '_')}.json")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# ── Endpoints ──────────────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    """Verifica que la API esté corriendo."""
    return {"status": "ok"}


@app.get("/api/objetivos")
def listar_objetivos():
    """Lista los objetivos disponibles (para llenar un <select> en el frontend)."""
    return {"objetivos": list(PLANES.keys())}


@app.post("/api/reporte")
def generar_reporte(usuario: UsuarioInput):
    """
    Endpoint principal: recibe los datos del usuario y devuelve el reporte
    completo, replicando el flujo de main.py (Python -> Scala -> Prolog),
    pero sin necesidad de consola.
    """
    usuario_dict = usuario.model_dump(exclude={"nivel_actividad"})

    # 1. Guardar JSON de entrada para que Scala lo lea
    ruta_entrada = guardar_usuario_json(usuario_dict)

    # 2. Llamar a Scala (si el jar no existe o falla, seguimos sin rutina)
    scala_ok = llamar_scala(ruta_entrada)
    resultado_scala = leer_resultado_scala(usuario.nombre) if scala_ok else {}

    # 3. Reporte calórico (Python)
    reporte = reporte_completo(
        nombre=usuario.nombre,
        peso=usuario.peso,
        altura=usuario.altura,
        edad=usuario.edad,
        genero=usuario.genero,
        nivel_actividad=usuario.nivel_actividad,
        objetivo=usuario.objetivo,
    )

    # 4. Plan alimenticio (Python)
    try:
        plan = generar_plan(usuario.objetivo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 5. Recomendaciones Prolog (si SWI-Prolog no está disponible, listas vacías)
    ejercicios_prolog = recomendar_ejercicios(usuario.objetivo)
    alimentos_prolog = recomendar_alimentos(usuario.objetivo)

    # 6. Unificar resultado final y guardarlo (igual que main.py)
    resultado_final = {
        **reporte,
        "plan_alimenticio": plan,
        "ejercicios_prolog": ejercicios_prolog,
        "alimentos_prolog": alimentos_prolog,
        "scala": resultado_scala,
        "scala_disponible": scala_ok,
        "prolog_disponible": len(ejercicios_prolog) > 0 or len(alimentos_prolog) > 0,
    }
    guardar_resultado_python(resultado_final, usuario.nombre)

    return resultado_final


@app.get("/api/plan/{objetivo}")
def obtener_plan(objetivo: str):
    """Devuelve solo el plan alimenticio para un objetivo dado (consulta suelta)."""
    try:
        return generar_plan(objetivo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))