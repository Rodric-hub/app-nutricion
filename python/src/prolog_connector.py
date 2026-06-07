"""
Módulo conector entre Python y Prolog
"""

from pyswip import Prolog
from pathlib import Path
import os


class PrologConnector:
    """Clase para gestionar la conexión entre Python y Prolog"""
    
    def __init__(self, prolog_dir=None):
        """
        Inicializa el conector de Prolog
        
        Args:
            prolog_dir: Ruta al directorio con archivos .pl
        """
        self.prolog = Prolog()
        
        if prolog_dir is None:
            # Determinar ruta por defecto
            current_dir = Path(__file__).parent
            prolog_dir = current_dir.parent.parent / "prolog"
        
        self.prolog_dir = Path(prolog_dir)
        self.cargar_archivos()
    
    def cargar_archivos(self):
        """Carga los archivos Prolog (hechos y reglas)"""
        hechos_file = self.prolog_dir / "hechos.pl"
        reglas_file = self.prolog_dir / "reglas.pl"
        
        if hechos_file.exists():
            self.prolog.consult(str(hechos_file))
            print(f"✓ Hechos cargados: {hechos_file}")
        else:
            raise FileNotFoundError(f"No se encontró {hechos_file}")
        
        if reglas_file.exists():
            self.prolog.consult(str(reglas_file))
            print(f"✓ Reglas cargadas: {reglas_file}")
        else:
            raise FileNotFoundError(f"No se encontró {reglas_file}")
    
    def calcular_tmr(self, genero, edad, peso, altura, actividad):
        """
        Calcula la tasa metabólica en reposo (TMR)
        
        Args:
            genero: 'hombre' o 'mujer'
            edad: edad en años
            peso: peso en kg
            altura: altura en cm
            actividad: nivel de actividad (sedentario, ligero, moderado, intenso, muy_intenso)
        
        Returns:
            float: calorías diarias necesarias
        """
        query = f"calcular_tmr({genero}, {edad}, {peso}, {altura}, {actividad}, TMR)."
        
        try:
            for soln in self.prolog.query(query):
                return float(soln["TMR"])
        except Exception as e:
            print(f"Error en calcular_tmr: {e}")
            return None
    
    def generar_plan(self, genero, edad, peso, altura, actividad, objetivo):
        """
        Genera un plan alimenticio completo
        
        Args:
            genero: 'hombre' o 'mujer'
            edad: edad en años
            peso: peso en kg
            altura: altura en cm
            actividad: nivel de actividad
            objetivo: 'ganancia_muscular', 'perdida_peso' o 'mantenimiento'
        
        Returns:
            dict: plan alimenticio con desayuno, almuerzo, merienda y cena
        """
        query = f"generar_plan({genero}, {edad}, {peso}, {altura}, {actividad}, {objetivo}, Plan)."
        
        try:
            for soln in self.prolog.query(query):
                plan_str = str(soln["Plan"])
                return self._parsear_plan(plan_str)
        except Exception as e:
            print(f"Error en generar_plan: {e}")
            return None
    
    def obtener_alimentos_categoria(self, categoria):
        """
        Obtiene todos los alimentos de una categoría
        
        Args:
            categoria: categoría de alimento (proteina, carbohidrato, verdura, fruta, grasa, lacteo)
        
        Returns:
            list: lista de nombres de alimentos
        """
        query = f"alimentos_por_categoria({categoria}, Alimentos)."
        
        try:
            for soln in self.prolog.query(query):
                alimentos_str = str(soln["Alimentos"])
                return self._parsear_lista(alimentos_str)
        except Exception as e:
            print(f"Error en obtener_alimentos_categoria: {e}")
            return []
    
    def obtener_propiedades_alimento(self, nombre_alimento):
        """
        Obtiene las propiedades nutricionales de un alimento
        
        Args:
            nombre_alimento: nombre del alimento
        
        Returns:
            dict: propiedades del alimento (calorías, proteína, carbos, grasas, categoría)
        """
        query = f"alimento({nombre_alimento}, Cal, Pro, Car, Gra, Cat)."
        
        try:
            for soln in self.prolog.query(query):
                return {
                    'nombre': nombre_alimento,
                    'calorias': float(soln["Cal"]),
                    'proteina': float(soln["Pro"]),
                    'carbohidrato': float(soln["Car"]),
                    'grasa': float(soln["Gra"]),
                    'categoria': str(soln["Cat"])
                }
        except Exception as e:
            print(f"Error en obtener_propiedades_alimento: {e}")
            return None
    
    def recomendar_objetivo(self, objetivo):
        """
        Obtiene una recomendación para un objetivo específico
        
        Args:
            objetivo: 'ganancia_muscular', 'perdida_peso' o 'mantenimiento'
        
        Returns:
            str: recomendación personalizada
        """
        query = f"recomendar_objetivo({objetivo}, Recom)."
        
        try:
            for soln in self.prolog.query(query):
                return str(soln["Recom"]).strip("'")
        except Exception as e:
            print(f"Error en recomendar_objetivo: {e}")
            return None
    
    def _parsear_plan(self, plan_str):
        """Parsea la estructura de plan desde Prolog"""
        # Este método convierte la salida de Prolog en un diccionario Python
        plan_dict = {
            'desayuno': {},
            'almuerzo': {},
            'merienda': {},
            'cena': {}
        }
        # Aquí iría lógica para parsear el formato de Prolog
        return plan_dict
    
    def _parsear_lista(self, lista_str):
        """Parsea una lista desde Prolog"""
        # Extrae elementos de la representación de lista en Prolog
        lista_str = lista_str.strip('[]')
        if not lista_str:
            return []
        elementos = [e.strip() for e in lista_str.split(',')]
        return elementos
    
    def validar_plan(self, plan):
        """
        Valida que un plan sea nutritivamente correcto
        
        Args:
            plan: estructura del plan a validar
        
        Returns:
            bool: True si el plan es válido
        """
        # Verificación básica de que el plan tenga todos los componentes
        requeridos = ['desayuno', 'almuerzo', 'merienda', 'cena']
        return all(comp in plan for comp in requeridos)


# Exportar funciones principales
def conectar_prolog(prolog_dir=None):
    """Factory function para crear una instancia del conector"""
    return PrologConnector(prolog_dir)
