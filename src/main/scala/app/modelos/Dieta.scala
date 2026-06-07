package app.modelos

case class Alimento(
  nombre: String,
  calorias: Double,
  proteinas: Double,
  carbohidratos: Double,
  grasas: Double
)

case class Comida(
  nombre: String, // "Desayuno" | "Almuerzo" | "Cena" | "Snack"
  alimentos: List[Alimento]
) {
  def totalCalorias: Double = alimentos.map(_.calorias).sum
}

case class Dieta(
  objetivo: String,
  caloriasObjetivo: Double,
  comidas: List[Comida]
) {
  def totalCalorias: Double = comidas.map(_.totalCalorias).sum

  override def toString: String =
    s"Dieta para: $objetivo | Objetivo: ${"%.0f".format(caloriasObjetivo)} kcal | " +
    s"Total plan: ${"%.0f".format(totalCalorias)} kcal"
}

object Dieta {
  val alimentosPerder: List[Comida] = List(
    Comida("Desayuno", List(
      Alimento("Claras de huevo (4 und.)",   70,  17,  1,  0.5),
      Alimento("Avena en agua (50g)",        180,  6,  32,  3.5),
      Alimento("Manzana mediana",             80,  0.4, 21,  0.2),
      Alimento("Té verde sin azúcar",          2,  0,   0,   0)
    )),
    Comida("Almuerzo", List(
      Alimento("Pechuga de pollo plancha (150g)", 165, 31,  0,  3.5),
      Alimento("Arroz integral cocido (80g)",     104,  2,  22,  0.8),
      Alimento("Brócoli al vapor (150g)",          50,  4,   8,  0.5),
      Alimento("Ensalada de pepino y tomate",      30,  1,   6,  0.2)
    )),
    Comida("Snack", List(
      Alimento("Yogur natural sin azúcar (150g)", 90, 10,  6,  1.0),
      Alimento("Zanahoria baby (100g)",            41,  0.9, 10,  0.2),
      Alimento("Fresas (100g)",                    32,  0.7,  8,  0.3)
    )),
    Comida("Cena", List(
      Alimento("Pescado al horno (150g)",    140, 28,  0,  3.0),
      Alimento("Espinaca salteada (100g)",    23,  2.9, 3.6, 0.4),
      Alimento("Papa sancochada (100g)",      85,  2,  19,  0.1),
      Alimento("Limón y aceite de oliva",     45,  0,   0,   5.0)
    ))
  )

  val alimentosMantener: List[Comida] = List(
    Comida("Desayuno", List(
      Alimento("Huevos revueltos (2 und.)",  140, 12,  1,  9.0),
      Alimento("Pan integral (2 rebanadas)", 160,  6,  30,  2.0),
      Alimento("Jugo de naranja natural",     90,  1,  21,  0.2),
      Alimento("Yogur con granola (100g)",   150,  5,  22,  4.0)
    )),
    Comida("Almuerzo", List(
      Alimento("Quinoa cocida (100g)",         120,  4,  21,  2.0),
      Alimento("Pechuga de pavo (150g)",       150, 28,   0,  3.0),
      Alimento("Lenteja guisada (100g)",       116,  9,  20,  0.4),
      Alimento("Verduras salteadas con oliva", 100,  2,  10,  6.0)
    )),
    Comida("Snack", List(
      Alimento("Almendras (25g)",             145,  5,   5,  12.5),
      Alimento("Pera mediana",                 85,  0.5, 22,   0.2),
      Alimento("Leche descremada (200ml)",     70,  7,  10,   0.4)
    )),
    Comida("Cena", List(
      Alimento("Salmón al horno (150g)",      220, 30,   0,  11.0),
      Alimento("Arroz integral (80g)",        104,  2,  22,   0.8),
      Alimento("Camote sancochado (100g)",     86,  1.6, 20,  0.1),
      Alimento("Espárragos a la plancha (100g)", 20, 2,   4,  0.1)
    ))
  )

  val alimentosGanar: List[Comida] = List(
    Comida("Desayuno", List(
      Alimento("Huevos enteros revueltos (3 und.)", 210, 18,  2, 14.0),
      Alimento("Avena con leche entera (80g)",      310, 11,  54,  6.0),
      Alimento("Plátano mediano",                   105,  1.3, 27,  0.4),
      Alimento("Mantequilla de maní (20g)",         120,  5,   4,  10.0)
    )),
    Comida("Almuerzo", List(
      Alimento("Arroz blanco cocido (200g)",        260,  5,  57,  0.5),
      Alimento("Filete de res magra (180g)",        270, 36,   0,  13.0),
      Alimento("Frijoles negros (100g)",            132,  9,  24,   0.5),
      Alimento("Aguacate (media unidad)",           120,  1.5,  6,  11.0),
      Alimento("Papa sancochada (150g)",            128,  3,  29,   0.2)
    )),
    Comida("Snack", List(
      Alimento("Batido proteína con leche (1 scoop)", 280, 28, 22,  6.0),
      Alimento("Nueces (30g)",                        196,  4,   4,  19.0),
      Alimento("Pan integral con atún (1 porción)",   200, 20,  22,   3.0)
    )),
    Comida("Cena", List(
      Alimento("Pechuga de pollo (200g)",          220, 41,   0,  4.8),
      Alimento("Lentejas guisadas (100g)",         116,  9,  20,  0.4),
      Alimento("Arroz blanco (150g)",              195,  4,  43,  0.4),
      Alimento("Ensalada con aceite de oliva",      80,  1,   5,  7.0),
      Alimento("Leche entera (250ml)",             150,  8,  12,  8.0)
    ))
  )
}