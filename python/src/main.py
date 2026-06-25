"""
main.py
Punto de entrada principal - orquesta el flujo completo:
Python (datos) → Scala (rutinas) → Prolog (recomendaciones) → resultado final
"""

import sys
import os
import subprocess
import json

sys.path.insert(0, os.path.dirname(__file__))

from utils.calculadora_calorias import reporte_completo
from utils.planes_alimenticios import imprimir_plan, generar_plan
from integracion.prolog_connector import recomendar_ejercicios, recomendar_alimentos
from integracion.scala_connector import guardar_usuario_json, guardar_resultado_python, DATA_DIR


# ── Llamar a Scala ────────────────────────────────────────────────────────────
def llamar_scala(ruta_json: str) -> dict:
    jar_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        "../../scala/target/scala-2.13/gimnasio.jar"
    ))
    print("\n⚙️  Llamando al módulo Scala...")
    try:
        ruta_json_norm = ruta_json.replace("\\", "/")
        result = subprocess.run(
            ["java", "-jar", jar_path, ruta_json_norm],
            capture_output=True,
            text=True,
            timeout=30
        )
        for linea in result.stdout.splitlines():
            if any(k in linea for k in ["[Scala]", "TMB", "Rutina", "Calor", "IMC", "Metabolismo"]):
                print(f"   {linea.strip()}")
        return {"scala_ok": True}
    except Exception as e:
        print(f"   (Scala omitido: {e})")
        return {"scala_ok": False}


def leer_resultado_scala(nombre: str) -> dict:
    ruta = os.path.join(DATA_DIR, "salida", f"resultado_scala_{nombre.replace(' ', '_')}.json")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# ── Menú interactivo ──────────────────────────────────────────────────────────
def menu_interactivo():
    print("╔══════════════════════════════════════════╗")
    print("║   APP GIMNASIO MULTILENGUAJE              ║")
    print("║   Python  →  Scala  →  Prolog             ║")
    print("╚══════════════════════════════════════════╝\n")

    # 1. Datos del usuario
    print("📝 Ingresa tus datos:\n")
    nombre   = input("   Nombre: ").strip() or "Usuario"
    edad     = int(input("   Edad (años): ") or 25)
    peso     = float(input("   Peso (kg): ") or 70)
    altura   = float(input("   Altura (cm): ") or 170)
    genero   = input("   Género (masculino/femenino): ").strip().lower() or "masculino"

    print("\n   Objetivos: 1. perder_peso  2. ganar_musculo  3. mantenimiento")
    obj_map = {"1": "perder_peso", "2": "ganar_musculo", "3": "mantenimiento"}
    objetivo = obj_map.get(input("   Elige objetivo (1/2/3): ").strip(), "mantenimiento")

    print("\n   Actividad: 1.sedentario  2.ligero  3.moderado  4.activo  5.muy_activo")
    act_map = {"1": "sedentario", "2": "ligero", "3": "moderado", "4": "activo", "5": "muy_activo"}
    actividad = act_map.get(input("   Elige nivel (1-5): ").strip(), "moderado")

    usuario_dict = {"nombre": nombre, "edad": edad, "peso": peso,
                    "altura": altura, "genero": genero, "objetivo": objetivo}

    # 2. Python guarda JSON de entrada
    print("\n" + "─" * 50)
    ruta_entrada = guardar_usuario_json(usuario_dict)

    # 3. Scala lee JSON, calcula rutinas y guarda resultado
    llamar_scala(ruta_entrada)
    resultado_scala = leer_resultado_scala(nombre)

    # 4. Reporte calórico (Python)
    print("\n" + "─" * 50)
    reporte = reporte_completo(nombre, peso, altura, edad, genero, actividad, objetivo)
    print(f"\n📊 REPORTE CALÓRICO - {nombre.upper()}")
    print(f"   TMB (Metabolismo Basal):            {reporte['tmb']} kcal/día")
    print(f"   Calorías de mantenimiento:          {reporte['calorias_mantenimiento']} kcal/día")
    print(f"   Calorías objetivo ({objetivo}):  {reporte['calorias_objetivo']} kcal/día")
    print(f"   IMC: {reporte['imc']} → {reporte['clasificacion_imc']}")

    if resultado_scala:
        print(f"\n   🏋️  Rutina (Scala): {resultado_scala.get('rutina', 'N/A')}")
        print(f"   ⏱️  Duración:        {resultado_scala.get('rutina_duracion_min', 0)} min")
        print(f"   🔥 Cal. quemadas:   ~{resultado_scala.get('rutina_calorias', 0)} kcal")

    # 5. Plan alimenticio (Python)
    print("\n" + "─" * 50)
    imprimir_plan(objetivo)

    # 6. Recomendaciones Prolog
    print("\n" + "─" * 50)
    print("\n🧠 RECOMENDACIONES (motor Prolog):")
    ejercicios = recomendar_ejercicios(objetivo)
    alimentos_prolog = recomendar_alimentos(objetivo)
    if ejercicios:
        print(f"   Ejercicios: {', '.join(ejercicios)}")
        print(f"   Alimentos:  {', '.join(alimentos_prolog)}")
    else:
        print("   (SWI-Prolog no disponible)")

    # 7. Guardar resultado final
    plan = generar_plan(objetivo)
    resultado_final = {
        **reporte,
        "plan_alimenticio": plan,
        "ejercicios_prolog": ejercicios,
        "alimentos_prolog": alimentos_prolog,
        "scala": resultado_scala
    }
    guardar_resultado_python(resultado_final, nombre)

    print("\n✅ Flujo completo ejecutado:")
    print("   1. Python  → recopiló datos e inició el flujo")
    print("   2. Scala   → calculó rutinas y guardó resultado_scala.json")
    print("   3. Prolog  → recomendó ejercicios y alimentos")
    print("   4. Python  → unificó todo en resultado_python.json\n")


def demo_sin_input():
    print("╔══════════════════════════════════════════╗")
    print("║   APP GIMNASIO - Demo                    ║")
    print("╚══════════════════════════════════════════╝\n")
    usuarios = [
        ("Ana Lopez",   28, 65.0, 165.0, "femenino",  "moderado", "perder_peso"),
        ("Carlos Rios", 32, 80.0, 178.0, "masculino", "activo",   "ganar_musculo"),
    ]
    for nombre, edad, peso, altura, genero, actividad, objetivo in usuarios:
        reporte = reporte_completo(nombre, peso, altura, edad, genero, actividad, objetivo)
        print(f"👤 {nombre} | {reporte['calorias_objetivo']} kcal ({objetivo}) | IMC {reporte['imc']}")
    print()
    imprimir_plan("perder_peso")
    print("\n✅ Demo completada.\n")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo_sin_input()
    else:
        menu_interactivo()
