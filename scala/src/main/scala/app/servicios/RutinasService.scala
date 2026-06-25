package app.servicios

import app.modelos.{Ejercicio, Rutina, Usuario}

object RutinasService {

  private val rutinas: Map[String, Rutina] = Map(

    "perder_peso_principiante" -> Rutina(
      nombre = "Cardio Básico",
      objetivo = "perder_peso",
      nivel = "principiante",
      ejercicios = List(
        Ejercicio("Caminata rápida", 1, 0, 200),
        Ejercicio("Sentadillas", 3, 15, 80),
        Ejercicio("Flexiones rodillas", 3, 10, 60),
        Ejercicio("Jumping jacks", 3, 20, 100)
      ),
      duracionMinutos = 40
    ),

    "perder_peso_intermedio" -> Rutina(
      nombre = "Cardio + Fuerza",
      objetivo = "perder_peso",
      nivel = "intermedio",
      ejercicios = List(
        Ejercicio("Carrera continua", 1, 0, 350),
        Ejercicio("Burpees", 4, 12, 150),
        Ejercicio("Sentadillas con salto", 4, 15, 120),
        Ejercicio("Plancha", 3, 0, 50)
      ),
      duracionMinutos = 55
    ),

    "ganar_musculo_principiante" -> Rutina(
      nombre = "Fuerza Inicial",
      objetivo = "ganar_musculo",
      nivel = "principiante",
      ejercicios = List(
        Ejercicio("Sentadillas con peso", 4, 12, 100),
        Ejercicio("Press banca", 4, 10, 90),
        Ejercicio("Peso muerto", 3, 8, 120),
        Ejercicio("Remo con barra", 3, 10, 80)
      ),
      duracionMinutos = 60
    ),

    "ganar_musculo_avanzado" -> Rutina(
      nombre = "Hipertrofia Avanzada",
      objetivo = "ganar_musculo",
      nivel = "avanzado",
      ejercicios = List(
        Ejercicio("Sentadillas pesadas", 5, 5, 150),
        Ejercicio("Press banca inclinado", 4, 8, 110),
        Ejercicio("Dominadas lastradas", 4, 6, 100),
        Ejercicio("Press militar", 4, 8, 90),
        Ejercicio("Peso muerto rumano", 4, 8, 130)
      ),
      duracionMinutos = 75
    ),

    "mantenimiento_moderado" -> Rutina(
      nombre = "Fitness General",
      objetivo = "mantenimiento",
      nivel = "intermedio",
      ejercicios = List(
        Ejercicio("Trote", 1, 0, 250),
        Ejercicio("Circuito de calistenia", 3, 12, 150),
        Ejercicio("Yoga / Stretching", 1, 0, 80)
      ),
      duracionMinutos = 45
    )
  )

  def recomendarRutina(usuario: Usuario, nivel: String): Option[Rutina] = {
    val clave = s"${usuario.objetivo}_$nivel"
    rutinas.get(clave).orElse(
      rutinas.find { case (k, _) => k.startsWith(usuario.objetivo) }.map(_._2)
    )
  }

  def listarRutinas(): Unit =
    rutinas.values.foreach(r => println(s"  - $r"))
}
