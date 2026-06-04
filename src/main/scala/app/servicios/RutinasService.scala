package app.servicios

import app.modelos.Rutina

object RutinasService {
  def recomendar(objetivo: String): Rutina = objetivo match {
    case "perder" => Rutina("Cardio + Fuerza", 60, "Mixto")
    case "ganar"  => Rutina("Pesas - Hipertrofia", 75, "Fuerza")
    case _        => Rutina("Mantenimiento activo", 45, "Moderado")
  }

  def mostrarRutina(objetivo: String): Unit = {
    val r = recomendar(objetivo)
    println(s"\n--- Rutina Recomendada ---")
    println(s"Nombre  : ${r.nombre}")
    println(s"Duración: ${r.duracion} minutos")
    println(s"Tipo    : ${r.tipo}")
  }
}
