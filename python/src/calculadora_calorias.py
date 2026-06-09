"""
calculadora_calorias.py
Módulo para cálculos nutricionales básicos.
"""

def calcular_calorias(edad, peso, altura, objetivo):
    """
    Calcula las calorías diarias estimadas.
    """

    tmb = 10 * peso + 6.25 * altura - 5 * edad + 5

    if objetivo == "perder":
        return int(tmb * 1.2 * 0.85)
    elif objetivo == "ganar":
        return int(tmb * 1.2 * 1.15)
    else:
        return int(tmb * 1.2)


def calcular_imc(peso, altura_cm):
    """
    Calcula el Índice de Masa Corporal.
    """
    altura_m = altura_cm / 100
    return round(peso / (altura_m ** 2), 2)


def clasificar_imc(imc):
    """
    Clasifica el IMC según OMS.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


if __name__ == "__main__":
    edad = 20
    peso = 55
    altura = 158
    objetivo = "ganar"

    calorias = calcular_calorias(edad, peso, altura, objetivo)
    imc = calcular_imc(peso, altura)

    print("Calorías recomendadas:", calorias)
    print("IMC:", imc)
    print("Clasificación:", clasificar_imc(imc))