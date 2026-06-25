# Comunicación Scala ↔ Python

## Mecanismo: Archivos JSON

La comunicación entre Scala y Python se realiza a través de archivos JSON
almacenados en la carpeta `data/`.

### Flujo

```
Python (main.py)
    │
    ├── Escribe datos del usuario en:  data/entrada/usuario_<nombre>.json
    │
    └── Lee resultados de Scala en:    data/salida/resultado_<nombre>.json

Scala (Main.scala)
    │
    ├── Lee datos del usuario desde:   data/entrada/usuario_<nombre>.json
    │
    └── Escribe resultados en:         data/salida/resultado_<nombre>.json
```

### Formato del archivo de entrada (Python → Scala)

```json
{
  "nombre": "Ana López",
  "edad": 28,
  "peso": 65.0,
  "altura": 165.0,
  "genero": "femenino",
  "objetivo": "perder_peso"
}
```

### Formato del archivo de salida (Scala → Python)

```json
{
  "nombre": "Ana López",
  "tmb": 1432.5,
  "calorias_mantenimiento": 2220.4,
  "calorias_objetivo": 1720.4,
  "rutina_recomendada": "Cardio Básico",
  "imc": 23.88,
  "clasificacion_imc": "Normal"
}
```

## Alternativa: API REST local

Para proyectos más grandes, se puede levantar un servidor HTTP simple con
`http.server` en Python o un servidor Akka HTTP en Scala para intercomunicación
por REST/JSON.
