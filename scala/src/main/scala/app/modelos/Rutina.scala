package app.modelos

case class Ejercicio(
  nombre: String,
  series: Int,
  repeticiones: Int,
  caloriasAprox: Double
)

case class Rutina(
  nombre: String,
  objetivo: String,
  nivel: String,           // "principiante" | "intermedio" | "avanzado"
  ejercicios: List[Ejercicio],
  duracionMinutos: Int
) {
  def totalCalorias: Double = ejercicios.map(_.caloriasAprox).sum

  override def toString: String =
    s"Rutina: $nombre | Objetivo: $objetivo | Nivel: $nivel | " +
    s"Duración: ${duracionMinutos}min | Calorías quemadas: ~${"%.0f".format(totalCalorias)} kcal"
}
