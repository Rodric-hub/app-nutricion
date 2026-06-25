package app.modelos

case class Usuario(
  nombre: String,
  edad: Int,
  peso: Double,      // kg
  altura: Double,    // cm
  genero: String,    // "masculino" | "femenino"
  objetivo: String   // "perder_peso" | "ganar_musculo" | "mantenimiento"
) {
  def imc: Double = peso / Math.pow(altura / 100.0, 2)

  def clasificacionIMC: String = imc match {
    case x if x < 18.5 => "Bajo peso"
    case x if x < 25.0 => "Normal"
    case x if x < 30.0 => "Sobrepeso"
    case _             => "Obesidad"
  }

  override def toString: String =
    s"Usuario($nombre, $edad años, ${peso}kg, ${altura}cm, IMC: ${"%.2f".format(imc)} - $clasificacionIMC)"
}
