package app.servicios

import app.modelos.Usuario

object CaloriasService {

  /**
   * Calcula el Metabolismo Basal (TMB) usando la fórmula de Harris-Benedict revisada.
   * Resultado en kcal/día.
   */
  def calcularTMB(usuario: Usuario): Double = usuario.genero.toLowerCase match {
    case "masculino" =>
      88.362 + (13.397 * usuario.peso) + (4.799 * usuario.altura) - (5.677 * usuario.edad)
    case "femenino" =>
      447.593 + (9.247 * usuario.peso) + (3.098 * usuario.altura) - (4.330 * usuario.edad)
    case _ =>
      throw new IllegalArgumentException("Género no válido. Usa 'masculino' o 'femenino'.")
  }

  /**
   * Calcula las calorías diarias según nivel de actividad.
   * Factores: sedentario=1.2, ligero=1.375, moderado=1.55, activo=1.725, muy_activo=1.9
   */
  def calcularCaloriasDiarias(usuario: Usuario, nivelActividad: String): Double = {
    val tmb = calcularTMB(usuario)
    val factor = nivelActividad.toLowerCase match {
      case "sedentario"  => 1.2
      case "ligero"      => 1.375
      case "moderado"    => 1.55
      case "activo"      => 1.725
      case "muy_activo"  => 1.9
      case _             => 1.55
    }
    tmb * factor
  }

  /**
   * Ajusta las calorías según el objetivo del usuario.
   */
  def calcularCaloriasObjetivo(usuario: Usuario, nivelActividad: String): Double = {
    val calorias = calcularCaloriasDiarias(usuario, nivelActividad)
    usuario.objetivo.toLowerCase match {
      case "perder_peso"     => calorias - 500
      case "ganar_musculo"   => calorias + 300
      case "mantenimiento"   => calorias
      case _                 => calorias
    }
  }

  def mostrarReporte(usuario: Usuario, nivelActividad: String): Unit = {
    val tmb      = calcularTMB(usuario)
    val diarias  = calcularCaloriasDiarias(usuario, nivelActividad)
    val objetivo = calcularCaloriasObjetivo(usuario, nivelActividad)

    println(s"\n📊 Reporte calórico para ${usuario.nombre}:")
    println(s"   TMB (Metabolismo Basal):      ${"%.0f".format(tmb)} kcal/día")
    println(s"   Calorías de mantenimiento:    ${"%.0f".format(diarias)} kcal/día")
    println(s"   Calorías para ${usuario.objetivo}: ${"%.0f".format(objetivo)} kcal/día")
    println(s"   IMC: ${"%.2f".format(usuario.imc)} (${usuario.clasificacionIMC})")
  }
}
