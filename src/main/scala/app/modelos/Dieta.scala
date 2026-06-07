package app.modelos

case class Dieta(
    nombre: String,
    calorias: Int,
    alimentos: List[String]
)

object Dieta {
  val dietaPerder: Dieta = Dieta(
    nombre = "Pérdida de peso",
    calorias = 1500,
    alimentos = List(
      "Pechuga de pollo a la plancha",
      "Ensalada de espinacas con tomate",
      "Avena con agua",
      "Manzana",
      "Yogur natural sin azúcar",
      "Brócoli al vapor",
      "Claras de huevo",
      "Pepino",
      "Zanahoria",
      "Té verde sin azúcar"
    )
  )

  val dietaMantener: Dieta = Dieta(
    nombre = "Mantenimiento",
    calorias = 2000,
    alimentos = List(
      "Arroz integral",
      "Pechuga de pavo",
      "Lenteja guisada",
      "Plátano",
      "Huevo entero",
      "Pan integral",
      "Leche descremada",
      "Quinoa",
      "Atún en agua",
      "Naranja",
      "Camote sancochado",
      "Almendras"
    )
  )

  val dietaGanar: Dieta = Dieta(
    nombre = "Ganancia muscular",
    calorias = 2800,
    alimentos = List(
      "Arroz blanco",
      "Filete de res",
      "Huevos enteros",
      "Avena con leche",
      "Papa sancochada",
      "Pechuga de pollo",
      "Mantequilla de maní",
      "Pan integral con atún",
      "Frijoles negros",
      "Aguacate",
      "Leche entera",
      "Nueces"
    )
  )
}
