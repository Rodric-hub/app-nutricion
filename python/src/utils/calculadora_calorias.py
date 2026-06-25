"""
calculadora_calorias.py
Cálculo de TMB, calorías diarias y objetivo usando Harris-Benedict.
"""


def calcular_tmb(peso: float, altura: float, edad: int, genero: str) -> float:
    """Retorna el Metabolismo Basal en kcal/día."""
    genero = genero.lower()
    if genero == "masculino":
        return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    elif genero == "femenino":
        return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    else:
        raise ValueError("Género no válido. Usar 'masculino' o 'femenino'.")


FACTORES_ACTIVIDAD = {
    "sedentario":  1.2,
    "ligero":      1.375,
    "moderado":    1.55,
    "activo":      1.725,
    "muy_activo":  1.9,
}


def calcular_calorias_diarias(tmb: float, nivel_actividad: str) -> float:
    """Aplica el factor de actividad sobre el TMB."""
    factor = FACTORES_ACTIVIDAD.get(nivel_actividad.lower(), 1.55)
    return tmb * factor


AJUSTES_OBJETIVO = {
    "perder_peso":   -500,
    "ganar_musculo": +300,
    "mantenimiento":    0,
}


def calcular_calorias_objetivo(calorias_diarias: float, objetivo: str) -> float:
    """Ajusta las calorías según el objetivo del usuario."""
    ajuste = AJUSTES_OBJETIVO.get(objetivo.lower(), 0)
    return calorias_diarias + ajuste


def calcular_imc(peso: float, altura_cm: float) -> float:
    """Calcula el IMC dado peso en kg y altura en cm."""
    altura_m = altura_cm / 100
    return peso / (altura_m ** 2)


def clasificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def reporte_completo(nombre: str, peso: float, altura: float, edad: int,
                     genero: str, nivel_actividad: str, objetivo: str) -> dict:
    """Genera un diccionario con todos los cálculos para un usuario."""
    tmb       = calcular_tmb(peso, altura, edad, genero)
    diarias   = calcular_calorias_diarias(tmb, nivel_actividad)
    obj_cal   = calcular_calorias_objetivo(diarias, objetivo)
    imc       = calcular_imc(peso, altura)
    clasif    = clasificar_imc(imc)

    return {
        "nombre":               nombre,
        "tmb":                  round(tmb, 1),
        "calorias_mantenimiento": round(diarias, 1),
        "calorias_objetivo":    round(obj_cal, 1),
        "objetivo":             objetivo,
        "imc":                  round(imc, 2),
        "clasificacion_imc":    clasif,
    }


if __name__ == "__main__":
    reporte = reporte_completo(
        nombre="Ana López", peso=65, altura=165, edad=28,
        genero="femenino", nivel_actividad="moderado", objetivo="perder_peso"
    )
    print("\n📊 Reporte calórico:")
    for k, v in reporte.items():
        print(f"   {k}: {v}")
