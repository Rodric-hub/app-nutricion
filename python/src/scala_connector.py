import os
import shlex
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional


class ScalaConnector:
    """Conecta el backend Python con la aplicación Scala mediante subprocess."""

    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = Path(project_root).resolve() if project_root else self._detect_project_root()

    def _detect_project_root(self) -> Path:
        return Path(__file__).resolve().parents[2]

    def ejecutar_usuario(self, usuario: Dict[str, Any]) -> Dict[str, Any]:
        """Ejecuta la app Scala con los datos del usuario como argumentos."""
        nombre = str(usuario.get("nombre", "Usuario"))
        edad = int(usuario.get("edad", 0))
        peso = float(usuario.get("peso", 0.0))
        altura = float(usuario.get("altura", 0.0))
        objetivo = str(usuario.get("objetivo", "mantener"))

        comando = [
            "sbt",
            "-batch",
            " ".join(
                [
                    "runMain app.Main",
                    f"--nombre {shlex.quote(nombre)}",
                    f"--edad {shlex.quote(str(edad))}",
                    f"--peso {shlex.quote(str(peso))}",
                    f"--altura {shlex.quote(str(altura))}",
                    f"--objetivo {shlex.quote(objetivo)}",
                ]
            ),
        ]
        env = os.environ.copy()
        env.setdefault("JAVA_OPTS", "-Xms256m -Xmx512m")

        try:
            resultado = subprocess.run(
                comando,
                cwd=str(self.project_root),
                text=True,
                capture_output=True,
                timeout=240,
                env=env,
            )
        except FileNotFoundError as exc:
            raise RuntimeError("No se encontró sbt en el entorno. Instálelo para ejecutar la app Scala.") from exc
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("El proceso de Scala tardó demasiado en responder.") from exc

        if resultado.returncode != 0:
            detalle = resultado.stderr.strip() or resultado.stdout.strip()
            raise RuntimeError(f"La ejecución de Scala falló: {detalle}")

        return {
            "exitoso": True,
            "comando": " ".join(comando),
            "salida": resultado.stdout.strip(),
            "errores": resultado.stderr.strip(),
        }

    def ejecutar(self, nombre: str, edad: int, peso: float, altura: float, objetivo: str) -> Dict[str, Any]:
        return self.ejecutar_usuario({
            "nombre": nombre,
            "edad": edad,
            "peso": peso,
            "altura": altura,
            "objetivo": objetivo,
        })
