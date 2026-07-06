package app

import app.servicios._
import scala.io.StdIn.readLine

object Main extends App {
  System.setOut(new java.io.PrintStream(System.out, true, "UTF-8"))
  println("=== APP GIMNASIO ===")

  val datosUsuario = parseArgs(args) match {
    case Some(datos) => datos
    case None =>
      print("Nombre: ")
      val nombre = readLine()

      print("Edad: ")
      val edad = readLine().toInt

      print("Peso (kg): ")
      val peso = readLine().toDouble

      print("Altura (cm): ")
      val altura = readLine().toDouble

      println("Objetivo (perder / ganar / mantener): ")
      val objetivo = readLine()

      (nombre, edad, peso, altura, objetivo)
  }

  val (nombre, edad, peso, altura, objetivo) = datosUsuario

  val usuario =
    UsuarioService.crearUsuario(nombre, edad, peso, altura, objetivo)

  UsuarioService.mostrarUsuario(usuario)
  CaloriasService.mostrarCalorias(usuario)
  RutinasService.mostrarRutina(objetivo)

  private def parseArgs(args: Array[String]): Option[(String, Int, Double, Double, String)] = {
    val valores = scala.collection.mutable.Map.empty[String, String]
    var i = 0

    while (i < args.length) {
      args(i) match {
        case "--nombre" if i + 1 < args.length => valores("nombre") = args(i + 1)
        case "--edad" if i + 1 < args.length => valores("edad") = args(i + 1)
        case "--peso" if i + 1 < args.length => valores("peso") = args(i + 1)
        case "--altura" if i + 1 < args.length => valores("altura") = args(i + 1)
        case "--objetivo" if i + 1 < args.length => valores("objetivo") = args(i + 1)
        case _ =>
      }
      i += 1
    }

    (
      valores.get("nombre"),
      valores.get("edad"),
      valores.get("peso"),
      valores.get("altura"),
      valores.get("objetivo")
    ) match {
      case (Some(nombre), Some(edad), Some(peso), Some(altura), Some(objetivo)) =>
        try Some((nombre, edad.toInt, peso.toDouble, altura.toDouble, objetivo))
        catch {
          case _: NumberFormatException => None
        }
      case _ => None
    }
  }
}
