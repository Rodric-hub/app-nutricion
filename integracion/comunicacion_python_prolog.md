# Comunicación Python ↔ Prolog

## Mecanismo: subprocess (SWI-Prolog CLI)

Python llama a SWI-Prolog como proceso externo usando `subprocess.run()`.

### Flujo

```
Python (prolog_connector.py)
    │
    └── subprocess.run(["swipl", ...])
            │
            └── SWI-Prolog ejecuta recomendaciones.pl
                    │
                    └── Retorna resultados por stdout → Python los parsea
```

### Ejemplo de llamada

```python
import subprocess

query = "recomendar_ejercicios(perder_peso, Lista), format('~w~n', [Lista])"
script = f"""
:- consult('prolog/recomendaciones.pl').
:- {query}, halt.
:- halt(1).
"""
result = subprocess.run(["swipl", "--quiet", "-g", "true"],
                        input=script, capture_output=True, text=True)
print(result.stdout)  # [burpees,correr,bicicleta,saltar_cuerda]
```

## Mecanismo alternativo: pyswip

`pyswip` permite llamar a Prolog directamente desde Python sin subprocess:

```bash
pip install pyswip
```

```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("prolog/recomendaciones.pl")
resultados = list(prolog.query("recomendar_ejercicios(perder_peso, X)"))
print(resultados)
```

## Instalación de SWI-Prolog

| Sistema Operativo | Comando                                |
|-------------------|----------------------------------------|
| Ubuntu/Debian     | `sudo apt install swi-prolog`          |
| macOS             | `brew install swi-prolog`              |
| Windows           | Descargar desde https://www.swi-prolog.org/Download.html |
