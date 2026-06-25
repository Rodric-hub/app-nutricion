# App Gimnasio Multilenguaje

Aplicación multilenguaje para gestión de gimnasio que integra **Scala**, **Prolog** y **Python**.

## Tecnologías
| Módulo   | Lenguaje | Responsabilidad                              |
|----------|----------|----------------------------------------------|
| Core     | Scala    | Lógica principal, gestión de usuarios        |
| IA       | Prolog   | Recomendaciones inteligentes de rutinas      |
| Utils    | Python   | Cálculo de calorías, planes alimenticios     |

## Estructura
```
app-gimnasio-multilenguaje/
├── docs/           → Documentación
├── scala/          → Módulo principal (Scala + sbt)
├── prolog/         → Motor de inferencia (SWI-Prolog)
├── python/         → Integración y cálculos (Python 3)
├── integracion/    → Documentación de comunicación entre módulos
└── data/           → Archivos de entrada/salida (JSON)
```

## Requisitos
- Scala 2.13+ y sbt 1.x
- Python 3.8+
- SWI-Prolog 9.x

## Cómo ejecutar

### 1. Módulo Python (entrada principal)
```bash
cd python
pip install -r requirements.txt
python src/main.py
```

### 2. Módulo Scala (opcional, standalone)
```bash
cd scala
sbt run
```

### 3. Consultar Prolog directamente
```bash
swipl prolog/hechos.pl prolog/reglas.pl prolog/recomendaciones.pl
```
