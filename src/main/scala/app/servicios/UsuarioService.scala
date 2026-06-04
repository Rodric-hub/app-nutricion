package app.servicios

import app.modelos.Usuario

object UsuarioService {
  def crearUsuario(
      nombre: String,
      edad: Int,
      peso: Double,
      altura: Double,
      objetivo: String
  ): Usuario = {
    Usuario(nombre, edad, peso, altura, objetivo)
  }

  def mostrarUsuario(u: Usuario): Unit = {
    println(s"\n--- Datos del Usuario ---")
    println(s"Nombre  : ${u.nombre}")
    println(s"Edad    : ${u.edad} años")
    println(s"Peso    : ${u.peso} kg")
    println(s"Altura  : ${u.altura} cm")
    println(s"Objetivo: ${u.objetivo}")
  }
}
