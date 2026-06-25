package app.servicios

import app.modelos.Usuario

object UsuarioService {

  private var usuarios: List[Usuario] = List()

  def registrarUsuario(usuario: Usuario): Unit = {
    usuarios = usuario :: usuarios
    println(s"✅ Usuario registrado: ${usuario.nombre}")
  }

  def buscarUsuario(nombre: String): Option[Usuario] =
    usuarios.find(_.nombre.equalsIgnoreCase(nombre))

  def listarUsuarios(): Unit = {
    if (usuarios.isEmpty) println("No hay usuarios registrados.")
    else usuarios.foreach(u => println(s"  - $u"))
  }

  def eliminarUsuario(nombre: String): Boolean = {
    val antes = usuarios.length
    usuarios = usuarios.filterNot(_.nombre.equalsIgnoreCase(nombre))
    usuarios.length < antes
  }
}
