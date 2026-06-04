package app.modelos

case class Usuario(
  nombre: String,
  edad: Int,
  peso: Double,    // kg
  altura: Double,  // cm
  objetivo: String // "perder", "ganar", "mantener"
)