"""
prolog_connector.py
Comunicación entre Python y SWI-Prolog usando pyswip o subprocess.
"""

import subprocess
import os
import json
import shutil

# Ruta al directorio prolog relativa a este archivo
PROLOG_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../prolog")
)
PROLOG_DIR = PROLOG_DIR.replace("\\", "/")

# Candidatos de ruta para el ejecutable de SWI-Prolog.
# Se prueba primero el PATH del sistema (mas portable) y luego
# la ruta tipica de instalacion en Windows como respaldo.
_SWIPL_CANDIDATOS = [
    shutil.which("swipl"),
    r"C:\Program Files\swipl\bin\swipl.exe",
    r"C:\Program Files (x86)\swipl\bin\swipl.exe",
]
SWIPL_PATH = next((p for p in _SWIPL_CANDIDATOS if p and os.path.exists(p)), None)


def consultar_prolog_subprocess(query: str) -> str:
    if SWIPL_PATH is None:
        return "ERROR: SWI-Prolog no encontrado. Instálalo o agrégalo al PATH."

    prolog_file = PROLOG_DIR + "/recomendaciones.pl"
    goal = f"consult('{prolog_file}'), {query}, halt."

    try:
        result = subprocess.run(
            [SWIPL_PATH, "-g", goal, "-t", "halt"],
            capture_output=True,
            text=True,
            timeout=10
        )
        salida = result.stdout.strip()
        if not salida:
            salida = result.stderr.strip()
        return salida
    except FileNotFoundError:
        return "ERROR: SWI-Prolog no encontrado. Instálalo para usar este módulo."
    except subprocess.TimeoutExpired:
        return "ERROR: Timeout al ejecutar Prolog."

def recomendar_ejercicios(objetivo: str) -> list:
    """
    Consulta a Prolog los ejercicios recomendados para un objetivo.
    Retorna lista de strings.
    """
    query = (
        f"recomendar_ejercicios({objetivo}, Lista), "
        f"format('~w~n', [Lista])"
    )
    salida = consultar_prolog_subprocess(query)

    # Parsear la lista Prolog [a,b,c] a lista Python
    if salida.startswith("[") and salida.endswith("]"):
        contenido = salida[1:-1]
        return [item.strip() for item in contenido.split(",") if item.strip()]
    return []


def recomendar_alimentos(objetivo: str) -> list:
    """
    Consulta a Prolog los alimentos recomendados para un objetivo.
    """
    query = (
        f"recomendar_alimentos({objetivo}, Lista), "
        f"format('~w~n', [Lista])"
    )
    salida = consultar_prolog_subprocess(query)

    if salida.startswith("[") and salida.endswith("]"):
        contenido = salida[1:-1]
        return [item.strip() for item in contenido.split(",") if item.strip()]
    return []


def obtener_plan_semanal(objetivo: str) -> dict:
    """
    Obtiene el plan semanal desde Prolog.
    """
    query = (
        f"plan_semanal({objetivo}, Plan), "
        f"format('~w~n', [Plan])"
    )
    salida = consultar_prolog_subprocess(query)
    return {"raw": salida, "objetivo": objetivo}


if __name__ == "__main__":
    print("🔗 Probando conexión Python → Prolog\n")
    ejs = recomendar_ejercicios("perder_peso")
    print(f"Ejercicios para perder_peso: {ejs}")
    als = recomendar_alimentos("ganar_musculo")
    print(f"Alimentos para ganar_musculo: {als}")