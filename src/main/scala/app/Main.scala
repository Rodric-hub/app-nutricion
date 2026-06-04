package app

import app.servicios._
import scala.io.StdIn.readLine

object Main extends App {
  System.setOut(new java.io.PrintStream(System.out, true, "UTF-8"))
  println("=== APP GIMNASIO ===")

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

  val usuario =
    UsuarioService.crearUsuario(nombre, edad, peso, altura, objetivo)

  UsuarioService.mostrarUsuario(usuario)
  CaloriasService.mostrarCalorias(usuario)
  RutinasService.mostrarRutina(objetivo)
}
