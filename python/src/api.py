from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from scala_connector import ScalaConnector


app = FastAPI(title="API Nutrición", version="1.0.0")
scala_connector = ScalaConnector()


class UsuarioRequest(BaseModel):
    nombre: str
    edad: int
    peso: float
    altura: float
    objetivo: str


class RespuestaEjecutar(BaseModel):
    exitoso: bool
    comando: str
    salida: str
    errores: Optional[str] = None


@app.get("/")
def health_check() -> dict:
    return {"status": "ok", "service": "api-nutricion"}


@app.post("/ejecutar-scala", response_model=RespuestaEjecutar)
def ejecutar_scala(usuario: UsuarioRequest) -> RespuestaEjecutar:
    try:
        resultado = scala_connector.ejecutar_usuario(usuario.model_dump())
        return RespuestaEjecutar(**resultado)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
