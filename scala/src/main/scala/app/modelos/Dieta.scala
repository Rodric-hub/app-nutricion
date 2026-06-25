package app.modelos

case class Alimento(
  nombre: String,
  calorias: Double,   // kcal por porción
  proteinas: Double,  // gramos
  carbohidratos: Double,
  grasas: Double
)

case class Comida(
  nombre: String,     // "Desayuno" | "Almuerzo" | "Cena" | "Snack"
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
    s"Dieta para: $objetivo | Objetivo: ${caloriasObjetivo} kcal | " +
    s"Total plan: ${"%.0f".format(totalCalorias)} kcal"
}
