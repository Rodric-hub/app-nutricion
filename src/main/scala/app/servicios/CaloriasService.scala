package app.servicios

import app.modelos.{Usuario, Dieta}

object CaloriasService {

  def calcularCalorias(u: Usuario): Int = {
    val tmb = 10 * u.peso + 6.25 * u.altura - 5 * u.edad + 5
    u.objetivo match {
      case "perder"   => (tmb * 1.2 * 0.85).toInt
      case "ganar"    => (tmb * 1.2 * 1.15).toInt
      case "mantener"         => (tmb * 1.2).toInt
    }
  }

  def mostrarCalorias(u: Usuario): Unit = {
    val cal = calcularCalorias(u)
    println(s"\n--- Calorías Diarias ---")
    println(s"Objetivo '${u.objetivo}': $cal kcal/día")
  }

  def generarDieta(u: Usuario): Dieta = {
    val cal = calcularCalorias(u).toDouble
    u.objetivo match {
      case "perder" => Dieta("Pérdida de peso",    cal, Dieta.alimentosPerder)
      case "ganar"  => Dieta("Ganancia muscular",  cal, Dieta.alimentosGanar)
      case "mantener" => Dieta("Mantenimiento",       cal, Dieta.alimentosMantener)
    }
  }

  def mostrarDieta(u: Usuario): Unit = {
    val dieta = generarDieta(u)

    println(s"\n========== PLAN DE DIETA ==========")
    println(dieta)

    dieta.comidas.foreach { comida =>
      println(s"\n  [${comida.nombre.toUpperCase}]  → ${"%.0f".format(comida.totalCalorias)} kcal")
      comida.alimentos.foreach { a =>
        println(f"    • ${a.nombre}%-45s | ${"%.0f".format(a.calorias)}%4s kcal | P:${a.proteinas}%4.1fg C:${a.carbohidratos}%4.1fg G:${a.grasas}%4.1fg")
      }
    }

    val diff = dieta.caloriasObjetivo - dieta.totalCalorias
    val balance = if (diff >= 0) f"+$diff%.0f kcal disponibles" else f"$diff%.0f kcal sobre el objetivo"
    println(s"\n  Balance: $balance")
    println(s"====================================\n")
  }
}