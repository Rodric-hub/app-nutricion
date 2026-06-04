package app.servicios

import app.modelos.Usuario

object CaloriasService {
  def calcularCalorias(u: Usuario): Int = {
    // Fórmula Harris-Benedict
    val tmb = 10 * u.peso + 6.25 * u.altura - 5 * u.edad + 5
    val calorias = u.objetivo match {
      case "perder" => (tmb * 1.2 * 0.85).toInt
      case "ganar"  => (tmb * 1.2 * 1.15).toInt
      case _        => (tmb * 1.2).toInt
    }
    calorias
  }

  def mostrarCalorias(u: Usuario): Unit = {
    val cal = calcularCalorias(u)
    println(s"\n--- Calorías Diarias ---")
    println(s"Objetivo '${u.objetivo}': $cal kcal/día")
  }
}
