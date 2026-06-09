package app.servicios

import app.modelos.Rutina

object RutinasService {

  def recomendar(objetivo: String): Rutina = objetivo match {

    case "perder" =>
      Rutina(
        "Cardio + Fuerza",
        60,
        "Mixto",
        List(
          "Caminata rápida",
          "Bicicleta",
          "Sentadillas",
          "Plancha abdominal"
        )
      )

    case "ganar" =>
      Rutina(
        "Pesas - Hipertrofia",
        75,
        "Fuerza",
        List(
          "Press banca",
          "Sentadillas",
          "Peso muerto",
          "Dominadas"
        )
      )

    case _ =>
      Rutina(
        "Mantenimiento activo",
        45,
        "Moderado",
        List(
          "Trote ligero",
          "Flexiones",
          "Abdominales",
          "Estiramientos"
        )
      )
  }

  def mostrarRutina(objetivo: String): Unit = {

    val r = recomendar(objetivo)

    println("\n--- Rutina Recomendada ---")
    println(s"Nombre    : ${r.nombre}")
    println(s"Duración  : ${r.duracion} minutos")
    println(s"Tipo      : ${r.tipo}")

    println("\nEjercicios:")

    r.ejercicios.foreach { ejercicio =>
      println(s"• $ejercicio")
    }
  }
}