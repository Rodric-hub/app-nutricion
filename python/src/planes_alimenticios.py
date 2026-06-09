"""
Módulo de gestión de planes alimenticios
"""

from datetime import datetime
from prolog_connector import PrologConnector
import json


class PlanAlimenticio:
    """Clase para representar un plan alimenticio individual"""
    
    def __init__(self, usuario_id, genero, edad, peso, altura, actividad, objetivo):
        """
        Inicializa un nuevo plan alimenticio
        
        Args:
            usuario_id: ID único del usuario
            genero: 'hombre' o 'mujer'
            edad: edad en años
            peso: peso en kg
            altura: altura en cm
            actividad: nivel de actividad
            objetivo: objetivo nutricional
        """
        self.usuario_id = usuario_id
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.actividad = actividad
        self.objetivo = objetivo
        self.fecha_creacion = datetime.now().isoformat()
        self.plan_data = None
        self.calorias_diarias = 0
        self.macros = None
    
    def __repr__(self):
        return f"<PlanAlimenticio usuario={self.usuario_id} objetivo={self.objetivo}>"


class GeneradorPlanesAlimenticios:
    """Clase principal para generar y gestionar planes alimenticios"""
    
    def __init__(self, prolog_dir=None):
        """
        Inicializa el generador
        
        Args:
            prolog_dir: Ruta al directorio con archivos Prolog
        """
        self.conector = PrologConnector(prolog_dir)
        self.planes_activos = {}  # usuario_id -> PlanAlimenticio
        self.historial_planes = []  # Historial de todos los planes
    
    def crear_plan(self, usuario_id, genero, edad, peso, altura, actividad, objetivo):
        """
        Crea un nuevo plan alimenticio personalizado
        
        Args:
            usuario_id: ID único del usuario
            genero: 'hombre' o 'mujer'
            edad: edad en años
            peso: peso en kg
            altura: altura en cm
            actividad: 'sedentario', 'ligero', 'moderado', 'intenso', 'muy_intenso'
            objetivo: 'ganancia_muscular', 'perdida_peso', 'mantenimiento'
        
        Returns:
            PlanAlimenticio: Plan creado o None si hay error
        """
        # Validar datos
        if not self._validar_datos_usuario(genero, edad, peso, altura, actividad, objetivo):
            return None
        
        # Crear objeto del plan
        plan = PlanAlimenticio(usuario_id, genero, edad, peso, altura, actividad, objetivo)
        
        # Calcular calorías diarias
        calorias = self.conector.calcular_tmr(genero, edad, peso, altura, actividad)
        if calorias is None:
            print("Error: No se pudo calcular las calorías diarias")
            return None
        
        plan.calorias_diarias = calorias
        
        # Generar plan completo
        plan_data = self.conector.generar_plan(genero, edad, peso, altura, actividad, objetivo)
        if plan_data is None:
            print("Error: No se pudo generar el plan alimenticio")
            return None
        
        plan.plan_data = plan_data
        plan.macros = self._calcular_macros(objetivo, calorias)
        
        # Guardar en registro activo
        self.planes_activos[usuario_id] = plan
        self.historial_planes.append(plan)
        
        return plan
    
    def obtener_plan(self, usuario_id):
        """
        Obtiene el plan activo de un usuario
        
        Args:
            usuario_id: ID del usuario
        
        Returns:
            PlanAlimenticio: Plan del usuario o None
        """
        return self.planes_activos.get(usuario_id)
    
    def actualizar_plan(self, usuario_id, nuevo_peso=None, nuevo_objetivo=None):
        """
        Actualiza un plan existente con nuevos parámetros
        
        Args:
            usuario_id: ID del usuario
            nuevo_peso: Nuevo peso en kg (opcional)
            nuevo_objetivo: Nuevo objetivo (opcional)
        
        Returns:
            PlanAlimenticio: Plan actualizado o None
        """
        plan = self.planes_activos.get(usuario_id)
        if plan is None:
            print(f"No hay plan activo para usuario {usuario_id}")
            return None
        
        # Actualizar parámetros
        if nuevo_peso is not None:
            plan.peso = nuevo_peso
        
        objetivo_anterior = plan.objetivo
        if nuevo_objetivo is not None:
            plan.objetivo = nuevo_objetivo
        
        # Recalcular plan con nuevos parámetros
        calorias = self.conector.calcular_tmr(
            plan.genero, plan.edad, plan.peso, plan.altura, plan.actividad
        )
        
        if calorias is None:
            print("Error recalculando calorías")
            plan.objetivo = objetivo_anterior
            return None
        
        plan.calorias_diarias = calorias
        plan.plan_data = self.conector.generar_plan(
            plan.genero, plan.edad, plan.peso, plan.altura, plan.actividad, plan.objetivo
        )
        plan.macros = self._calcular_macros(plan.objetivo, calorias)
        plan.fecha_creacion = datetime.now().isoformat()
        
        return plan
    
    def obtener_recomendaciones(self, usuario_id):
        """
        Obtiene recomendaciones personalizadas para el usuario
        
        Args:
            usuario_id: ID del usuario
        
        Returns:
            dict: Recomendaciones personalizadas
        """
        plan = self.planes_activos.get(usuario_id)
        if plan is None:
            return None
        
        recomendacion = self.conector.recomendar_objetivo(plan.objetivo)
        
        return {
            'objetivo': plan.objetivo,
            'recomendacion': recomendacion,
            'calorias_diarias': plan.calorias_diarias,
            'macros': plan.macros
        }
    
    def obtener_alimentos_recomendados(self, categoria):
        """
        Obtiene lista de alimentos recomendados por categoría
        
        Args:
            categoria: Categoría de alimento
        
        Returns:
            list: Lista de alimentos
        """
        return self.conector.obtener_alimentos_categoria(categoria)
    
    def obtener_info_alimento(self, nombre_alimento):
        """
        Obtiene información nutricional de un alimento
        
        Args:
            nombre_alimento: Nombre del alimento
        
        Returns:
            dict: Información del alimento
        """
        return self.conector.obtener_propiedades_alimento(nombre_alimento)
    
    def exportar_plan_json(self, usuario_id):
        """
        Exporta el plan en formato JSON
        
        Args:
            usuario_id: ID del usuario
        
        Returns:
            str: Plan en formato JSON
        """
        plan = self.planes_activos.get(usuario_id)
        if plan is None:
            return None
        
        plan_dict = {
            'usuario_id': plan.usuario_id,
            'fecha_creacion': plan.fecha_creacion,
            'datos_personales': {
                'genero': plan.genero,
                'edad': plan.edad,
                'peso': plan.peso,
                'altura': plan.altura
            },
            'objetivo': plan.objetivo,
            'nivel_actividad': plan.actividad,
            'calorias_diarias': plan.calorias_diarias,
            'macronutrientes': plan.macros,
            'plan': plan.plan_data
        }
        
        return json.dumps(plan_dict, indent=2, ensure_ascii=False)
    
    def listar_planes_usuario(self, usuario_id):
        """
        Lista todos los planes del historial de un usuario
        
        Args:
            usuario_id: ID del usuario
        
        Returns:
            list: Lista de planes históricos
        """
        return [p for p in self.historial_planes if p.usuario_id == usuario_id]
    
    def _validar_datos_usuario(self, genero, edad, peso, altura, actividad, objetivo):
        """Valida que los datos del usuario sean válidos"""
        if genero not in ['hombre', 'mujer']:
            print("Género inválido. Use 'hombre' o 'mujer'")
            return False
        
        if edad < 10 or edad > 120:
            print("Edad inválida. Debe estar entre 10 y 120 años")
            return False
        
        if peso < 20 or peso > 300:
            print("Peso inválido. Debe estar entre 20 y 300 kg")
            return False
        
        if altura < 100 or altura > 250:
            print("Altura inválida. Debe estar entre 100 y 250 cm")
            return False
        
        actividades_validas = ['sedentario', 'ligero', 'moderado', 'intenso', 'muy_intenso']
        if actividad not in actividades_validas:
            print(f"Actividad inválida. Use una de: {actividades_validas}")
            return False
        
        objetivos_validos = ['ganancia_muscular', 'perdida_peso', 'mantenimiento']
        if objetivo not in objetivos_validos:
            print(f"Objetivo inválido. Use uno de: {objetivos_validos}")
            return False
        
        return True
    
    def _calcular_macros(self, objetivo, calorias_totales):
        """Calcula la distribución de macronutrientes según objetivo"""
        distribucion = {
            'ganancia_muscular': {'proteina': 0.30, 'carbos': 0.45, 'grasas': 0.25},
            'perdida_peso': {'proteina': 0.35, 'carbos': 0.40, 'grasas': 0.25},
            'mantenimiento': {'proteina': 0.25, 'carbos': 0.50, 'grasas': 0.25}
        }
        
        dist = distribucion.get(objetivo, distribucion['mantenimiento'])
        
        return {
            'proteina': {
                'gramos': round((calorias_totales * dist['proteina']) / 4, 1),
                'calorias': round(calorias_totales * dist['proteina'], 1),
                'porcentaje': round(dist['proteina'] * 100, 1)
            },
            'carbohidratos': {
                'gramos': round((calorias_totales * dist['carbos']) / 4, 1),
                'calorias': round(calorias_totales * dist['carbos'], 1),
                'porcentaje': round(dist['carbos'] * 100, 1)
            },
            'grasas': {
                'gramos': round((calorias_totales * dist['grasas']) / 9, 1),
                'calorias': round(calorias_totales * dist['grasas'], 1),
                'porcentaje': round(dist['grasas'] * 100, 1)
            }
        }


# Funciones de utilidad
def crear_generador(prolog_dir=None):
    """Factory function para crear instancia del generador"""
    return GeneradorPlanesAlimenticios(prolog_dir)