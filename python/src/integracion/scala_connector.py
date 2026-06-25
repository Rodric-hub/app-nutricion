"""
scala_connector.py
Comunicación entre Python y el módulo Scala mediante archivos JSON.
"""

import json
import os
import subprocess
from datetime import datetime

DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../data")
)
SCALA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../scala")
)


def guardar_usuario_json(usuario: dict) -> str:
    """
    Guarda los datos del usuario en data/entrada/ para que Scala los lea.
    Retorna la ruta del archivo generado.
    """
    os.makedirs(os.path.join(DATA_DIR, "entrada"), exist_ok=True)
    ruta = os.path.join(DATA_DIR, "entrada", f"usuario_{usuario['nombre'].replace(' ', '_')}.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(usuario, f, ensure_ascii=False, indent=2)
    print(f"✅ Usuario guardado en: {ruta}")
    return ruta


def leer_resultado_scala(nombre_usuario: str) -> dict:
    """
    Lee el resultado generado por Scala en data/salida/.
    """
    nombre_archivo = f"resultado_{nombre_usuario.replace(' ', '_')}.json"
    ruta = os.path.join(DATA_DIR, "salida", nombre_archivo)
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def guardar_resultado_python(datos: dict, nombre: str) -> None:
    """
    Guarda los resultados del módulo Python en data/salida/.
    """
    os.makedirs(os.path.join(DATA_DIR, "salida"), exist_ok=True)
    nombre_archivo = f"resultado_python_{nombre.replace(' ', '_')}.json"
    ruta = os.path.join(DATA_DIR, "salida", nombre_archivo)
    datos["timestamp"] = datetime.now().isoformat()
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"✅ Resultado Python guardado en: {ruta}")


if __name__ == "__main__":
    usuario_ejemplo = {
        "nombre": "Ana López",
        "edad": 28,
        "peso": 65.0,
        "altura": 165.0,
        "genero": "femenino",
        "objetivo": "perder_peso"
    }
    guardar_usuario_json(usuario_ejemplo)
