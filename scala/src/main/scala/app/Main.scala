package app

import app.modelos.Usuario
import app.servicios.{CaloriasService, RutinasService, UsuarioService}
import java.io.{File, PrintWriter}
import scala.io.Source

object Main extends App {

  // ── Leer archivo JSON de entrada generado por Python ─────────────────────
  val archivoEntrada = if (args.nonEmpty) args(0) else buscarUltimoJSON()

  if (archivoEntrada == null) {
    println("[Scala] No se encontro archivo de entrada. Usando datos de ejemplo.")
    ejecutarDemo()
  } else {
    println(s"[Scala] Leyendo datos desde: $archivoEntrada")
    val usuario = leerUsuarioJSON(archivoEntrada)
    procesarUsuario(usuario)
  }

  // ── Buscar el JSON mas reciente en data/entrada/ ──────────────────────────
  def buscarUltimoJSON(): String = {
    val dataDir = new File("../data/entrada")
    if (!dataDir.exists()) return null
    val archivos = dataDir.listFiles().filter(_.getName.endsWith(".json"))
    if (archivos.isEmpty) return null
    archivos.maxBy(_.lastModified()).getAbsolutePath
  }

  // ── Leer y parsear el JSON manualmente ───────────────────────────────────
  def leerUsuarioJSON(ruta: String): Usuario = {
    val contenido = Source.fromFile(ruta, "UTF-8").mkString
    def extraer(campo: String): String = {
      val patron = s""""$campo"\\s*:\\s*"?([^",}]+)"?""".r
      patron.findFirstMatchIn(contenido).map(_.group(1).trim).getOrElse("")
    }
    Usuario(
      nombre   = extraer("nombre"),
      edad     = extraer("edad").toInt,
      peso     = extraer("peso").toDouble,
      altura   = extraer("altura").toDouble,
      genero   = extraer("genero"),
      objetivo = extraer("objetivo")
    )
  }

  // ── Procesar usuario y guardar resultado JSON ─────────────────────────────
  def procesarUsuario(usuario: Usuario): Unit = {
    UsuarioService.registrarUsuario(usuario)

    val nivelActividad = "moderado"
    val tmb            = CaloriasService.calcularTMB(usuario)
    val mantenimiento  = CaloriasService.calcularCaloriasDiarias(usuario, nivelActividad)
    val objetivo       = CaloriasService.calcularCaloriasObjetivo(usuario, nivelActividad)
    val rutina         = RutinasService.recomendarRutina(usuario, "principiante")

    CaloriasService.mostrarReporte(usuario, nivelActividad)

    println("\n[Scala] Rutina recomendada:")
    rutina match {
      case Some(r) => println(s"  $r")
      case None    => println("  No se encontro rutina.")
    }

    // Guardar resultado en data/salida/
    val nombreArchivo = usuario.nombre.replace(" ", "_")
    val dirSalida = new File("../data/salida")
    dirSalida.mkdirs()
    val rutaJSON = s"../data/salida/resultado_scala_$nombreArchivo.json"
    val pw = new PrintWriter(new File(rutaJSON), "UTF-8")
    pw.write(
      s"""{
         |  "nombre": "${usuario.nombre}",
         |  "tmb": ${"%.1f".format(tmb)},
         |  "calorias_mantenimiento": ${"%.1f".format(mantenimiento)},
         |  "calorias_objetivo": ${"%.1f".format(objetivo)},
         |  "objetivo": "${usuario.objetivo}",
         |  "imc": ${"%.2f".format(usuario.imc)},
         |  "clasificacion_imc": "${usuario.clasificacionIMC}",
         |  "rutina": "${rutina.map(_.nombre).getOrElse("N/A")}",
         |  "rutina_duracion_min": ${rutina.map(_.duracionMinutos).getOrElse(0)},
         |  "rutina_calorias": ${"%.0f".format(rutina.map(_.totalCalorias).getOrElse(0.0))}
         |}""".stripMargin
    )
    pw.close()
    println(s"\n[Scala] Resultado guardado en: $rutaJSON")
    println("[Scala] Modulo completado. Python puede continuar.")
  }

  // ── Demo sin JSON (comportamiento anterior) ───────────────────────────────
  def ejecutarDemo(): Unit = {
    val ana = Usuario("Ana Lopez", 28, 65.0, 165.0, "femenino", "perder_peso")
    val carlos = Usuario("Carlos Rios", 32, 80.0, 178.0, "masculino", "ganar_musculo")
    UsuarioService.registrarUsuario(ana)
    UsuarioService.registrarUsuario(carlos)
    CaloriasService.mostrarReporte(ana, "moderado")
    CaloriasService.mostrarReporte(carlos, "activo")
  }
}
