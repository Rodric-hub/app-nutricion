 package app.modelos

case class Rutina(
    nombre: String,
    duracion: Int,
    tipo: String,
    ejercicios: List[String]
)