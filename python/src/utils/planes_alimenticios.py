"""
planes_alimenticios.py
Genera planes alimenticios diarios personalizados según el objetivo.
"""

ALIMENTOS = {
    "pollo_a_la_plancha": {"calorias": 165, "proteinas": 31, "carbs": 0,  "grasas": 3.6},
    "arroz_integral":     {"calorias": 216, "proteinas": 5,  "carbs": 45, "grasas": 1.8},
    "brocoli":            {"calorias": 55,  "proteinas": 4,  "carbs": 11, "grasas": 0.6},
    "avena":              {"calorias": 303, "proteinas": 13, "carbs": 51, "grasas": 5.0},
    "huevo_entero":       {"calorias": 78,  "proteinas": 6,  "carbs": 1,  "grasas": 5.0},
    "salmon":             {"calorias": 208, "proteinas": 20, "carbs": 0,  "grasas": 13.0},
    "batata":             {"calorias": 86,  "proteinas": 2,  "carbs": 20, "grasas": 0.1},
    "manzana":            {"calorias": 52,  "proteinas": 0,  "carbs": 14, "grasas": 0.2},
    "almendras":          {"calorias": 579, "proteinas": 21, "carbs": 22, "grasas": 50.0},
    "yogur_griego":       {"calorias": 100, "proteinas": 10, "carbs": 4,  "grasas": 0.7},
    "pechuga_pavo":       {"calorias": 135, "proteinas": 30, "carbs": 0,  "grasas": 1.0},
    "lentejas":           {"calorias": 116, "proteinas": 9,  "carbs": 20, "grasas": 0.4},
    "platano":            {"calorias": 89,  "proteinas": 1,  "carbs": 23, "grasas": 0.3},
    "espinaca":           {"calorias": 23,  "proteinas": 3,  "carbs": 4,  "grasas": 0.4},
}

PLANES = {
    "perder_peso": {
        "desayuno": ["avena", "manzana", "yogur_griego"],
        "almuerzo": ["pollo_a_la_plancha", "brocoli", "espinaca"],
        "cena":     ["salmon", "espinaca", "brocoli"],
        "snack":    ["manzana", "yogur_griego"],
    },
    "ganar_musculo": {
        "desayuno": ["avena", "huevo_entero", "platano"],
        "almuerzo": ["pollo_a_la_plancha", "arroz_integral", "batata"],
        "cena":     ["salmon", "lentejas", "brocoli"],
        "snack":    ["almendras", "yogur_griego", "pechuga_pavo"],
    },
    "mantenimiento": {
        "desayuno": ["avena", "huevo_entero", "manzana"],
        "almuerzo": ["pollo_a_la_plancha", "arroz_integral", "espinaca"],
        "cena":     ["pechuga_pavo", "batata", "brocoli"],
        "snack":    ["yogur_griego", "almendras"],
    },
}


def generar_plan(objetivo: str) -> dict:
    """Devuelve el plan alimenticio para el objetivo dado."""
    objetivo = objetivo.lower()
    if objetivo not in PLANES:
        raise ValueError(f"Objetivo '{objetivo}' no válido. Usa: {list(PLANES.keys())}")

    plan_raw = PLANES[objetivo]
    plan = {}
    total = {"calorias": 0, "proteinas": 0, "carbs": 0, "grasas": 0}

    for comida, alimentos in plan_raw.items():
        detalle = []
        for nombre in alimentos:
            info = ALIMENTOS[nombre]
            detalle.append({"alimento": nombre, **info})
            for key in total:
                total[key] += info[key]
        plan[comida] = detalle

    plan["totales_dia"] = {k: round(v, 1) for k, v in total.items()}
    return plan


def imprimir_plan(objetivo: str) -> None:
    plan = generar_plan(objetivo)
    print(f"\n🥗 Plan alimenticio para: {objetivo.upper()}")
    print("─" * 50)
    for comida, items in plan.items():
        if comida == "totales_dia":
            print(f"\n📊 TOTALES DEL DÍA: {items}")
        else:
            print(f"\n🍽️  {comida.upper()}:")
            for item in items:
                print(f"   - {item['alimento']}: {item['calorias']} kcal | "
                      f"P:{item['proteinas']}g C:{item['carbs']}g G:{item['grasas']}g")


if __name__ == "__main__":
    imprimir_plan("perder_peso")
    imprimir_plan("ganar_musculo")
