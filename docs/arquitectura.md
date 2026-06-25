# Arquitectura del Sistema

## Diagrama general

```
┌─────────────────────────────────────────────────────┐
│                  USUARIO / CLI                       │
└──────────────┬──────────────┬───────────────────────┘
               │              │
               ▼              ▼
  ┌────────────────┐   ┌─────────────────┐
  │  Módulo Scala  │   │  Módulo Python  │
  │  (Core/Lógica) │   │  (Integración)  │
  └───────┬────────┘   └────────┬────────┘
          │                     │
          │  JSON (data/)        │  subprocess
          │◄────────────────────►│
          │                     │
          │              ┌──────▼────────┐
          │              │ Módulo Prolog │
          │              │ (Inferencia)  │
          │              └───────────────┘
          │
  ┌───────▼────────────────────┐
  │  data/entrada/  data/salida/ │
  └─────────────────────────────┘
```

## Responsabilidades por módulo

### Scala
- Gestión de usuarios (CRUD)
- Cálculo de calorías (TMB, Harris-Benedict)
- Gestión de rutinas de entrenamiento
- Coordinación general del sistema

### Python
- Punto de entrada principal (`main.py`)
- Cálculo nutricional detallado
- Generación de planes alimenticios
- Comunicación con Prolog (subprocess/pyswip)
- Lectura/escritura de JSON para comunicación con Scala

### Prolog
- Base de hechos (ejercicios, alimentos, niveles)
- Reglas de inferencia lógica
- Recomendaciones inteligentes de rutinas
- Clasificación de perfiles de usuario
- Planes semanales de entrenamiento
