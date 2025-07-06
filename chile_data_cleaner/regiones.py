"""
Librería de Limpieza de Datos para Chile
=======================================

Una librería Python para normalizar y limpiar datos específicos de Chile.
Comenzamos con la normalización de regiones según la codificación oficial del INE.
"""

import re
from typing import Optional, Union
import unicodedata

class ChileDataCleaner:
    """
    Clase principal para limpiar datos específicos de Chile.
    """
    
    def __init__(self):
        # Códigos oficiales del INE para las regiones de Chile
        self.regiones_ine = {
            # Código INE: (nombre_oficial, variantes_comunes)
            15: ("Arica y Parinacota", [
                "arica y parinacota", "arica", "region de arica y parinacota",
                "xv region", "xv", "region xv", "15"
            ]),
            1: ("Tarapacá", [
                "tarapaca", "iquique", "region de tarapaca",
                "i region", "i", "region i", "1"
            ]),
            2: ("Antofagasta", [
                "antofagasta", "region de antofagasta",
                "ii region", "ii", "region ii", "2"
            ]),
            3: ("Atacama", [
                "atacama", "copiapo", "region de atacama",
                "iii region", "iii", "region iii", "3"
            ]),
            4: ("Coquimbo", [
                "coquimbo", "la serena", "region de coquimbo",
                "iv region", "iv", "region iv", "4"
            ]),
            5: ("Valparaíso", [
                "valparaiso", "valpo", "region de valparaiso",
                "v region", "v", "region v", "5"
            ]),
            13: ("Metropolitana de Santiago", [
                "metropolitana", "santiago", "rm", "region metropolitana",
                "metropolitana de santiago", "stgo", "13"
            ]),
            6: ("Libertador General Bernardo O'Higgins", [
                "ohiggins", "o'higgins", "libertador general bernardo o'higgins",
                "rancagua", "vi region", "vi", "region vi", "6"
            ]),
            7: ("Maule", [
                "maule", "talca", "region del maule",
                "vii region", "vii", "region vii", "7"
            ]),
            16: ("Ñuble", [
                "ñuble", "nuble", "chillan", "region de ñuble",
                "xvi region", "xvi", "region xvi", "16"
            ]),
            8: ("Biobío", [
                "biobio", "bio bio", "concepcion", "region del biobio",
                "viii region", "viii", "region viii", "8"
            ]),
            9: ("Araucanía", [
                "araucania", "temuco", "region de la araucania",
                "ix region", "ix", "region ix", "9"
            ]),
            14: ("Los Ríos", [
                "los rios", "rios", "valdivia", "region de los rios",
                "xiv region", "xiv", "region xiv", "14"
            ]),
            10: ("Los Lagos", [
                "los lagos", "lagos", "puerto montt", "region de los lagos",
                "x region", "x", "region x", "10"
            ]),
            11: ("Aysén del General Carlos Ibáñez del Campo", [
                "aysen", "aisen", "coyhaique", "region de aysen",
                "xi region", "xi", "region xi", "11"
            ]),
            12: ("Magallanes y de la Antártica Chilena", [
                "magallanes", "punta arenas", "antartica", "antártica",
                "region de magallanes", "xii region", "xii", "region xii", "12"
            ])
        }
        
        # Crear diccionario inverso para búsqueda rápida
        self._variantes_a_codigo = {}
        for codigo, (nombre_oficial, variantes) in self.regiones_ine.items():
            # Agregar el nombre oficial también
            self._variantes_a_codigo[self._normalizar_texto(nombre_oficial)] = codigo
            # Agregar todas las variantes
            for variante in variantes:
                self._variantes_a_codigo[self._normalizar_texto(variante)] = codigo
    
    def _normalizar_texto(self, texto: str) -> str:
        """
        Normaliza texto removiendo acentos, convirtiendo a minúsculas y limpiando espacios.
        """
        if not texto:
            return ""
        
        # Remover acentos
        texto_sin_acentos = unicodedata.normalize('NFD', texto)
        texto_sin_acentos = ''.join(c for c in texto_sin_acentos if unicodedata.category(c) != 'Mn')
        
        # Convertir a minúsculas y limpiar espacios
        texto_limpio = re.sub(r'\s+', ' ', texto_sin_acentos.lower().strip())
        
        return texto_limpio
    
    def normalizar_region(self, region_input: Union[str, int]) -> Optional[dict]:
        """
        Normaliza una región de Chile al código y nombre oficial del INE.
        
        Args:
            region_input: Nombre, código o variante de la región (str o int)
            
        Returns:
            dict: Diccionario con 'codigo' y 'nombre_oficial', o None si no se encuentra
            
        Examples:
            >>> cleaner = ChileDataCleaner()
            >>> cleaner.normalizar_region("valpo")
            {'codigo': 5, 'nombre_oficial': 'Valparaíso'}
            
            >>> cleaner.normalizar_region("RM")
            {'codigo': 13, 'nombre_oficial': 'Metropolitana de Santiago'}
            
            >>> cleaner.normalizar_region(8)
            {'codigo': 8, 'nombre_oficial': 'Biobío'}
        """
        if region_input is None:
            return None
        
        # Si es un número, verificar si es un código válido
        if isinstance(region_input, int):
            if region_input in self.regiones_ine:
                return {
                    'codigo': region_input,
                    'nombre_oficial': self.regiones_ine[region_input][0]
                }
            return None
        
        # Convertir a string y normalizar
        region_str = str(region_input)
        region_normalizada = self._normalizar_texto(region_str)
        
        # Buscar en el diccionario de variantes
        codigo = self._variantes_a_codigo.get(region_normalizada)
        
        if codigo is not None:
            return {
                'codigo': codigo,
                'nombre_oficial': self.regiones_ine[codigo][0]
            }
        
        return None
    
    def listar_regiones(self) -> list:
        """
        Retorna una lista de todas las regiones con sus códigos y nombres oficiales.
        
        Returns:
            list: Lista de diccionarios con 'codigo' y 'nombre_oficial'
        """
        regiones = []
        for codigo, (nombre_oficial, _) in self.regiones_ine.items():
            regiones.append({
                'codigo': codigo,
                'nombre_oficial': nombre_oficial
            })
        
        # Ordenar por código
        return sorted(regiones, key=lambda x: x['codigo'])
    
    def validar_region(self, region_input: Union[str, int]) -> bool:
        """
        Valida si una región existe en la codificación del INE.
        
        Args:
            region_input: Nombre, código o variante de la región
            
        Returns:
            bool: True si la región es válida, False en caso contrario
        """
        return self.normalizar_region(region_input) is not None


# Función de conveniencia para uso directo
def normalizar_region_chile(region: Union[str, int]) -> Optional[dict]:
    """
    Función de conveniencia para normalizar una región de Chile.
    
    Args:
        region: Nombre, código o variante de la región
        
    Returns:
        dict: Diccionario con 'codigo' y 'nombre_oficial', o None si no se encuentra
    """
    cleaner = ChileDataCleaner()
    return cleaner.normalizar_region(region)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia del limpiador
    cleaner = ChileDataCleaner()
    
    # Ejemplos de uso
    print("=== Ejemplos de Normalización de Regiones ===")
    
    ejemplos = [
        "valpo",
        "RM",
        "bio bio",
        "Arica",
        "VIII región",
        "Ñuble",
        13,
        "región del maule",
        "Los Lagos",
        "region inexistente"
    ]
    
    for ejemplo in ejemplos:
        resultado = cleaner.normalizar_region(ejemplo)
        if resultado:
            print(f"'{ejemplo}' -> Código: {resultado['codigo']}, Nombre: {resultado['nombre_oficial']}")
        else:
            print(f"'{ejemplo}' -> No encontrado")
    
    print("\n=== Lista de Todas las Regiones ===")
    for region in cleaner.listar_regiones():
        print(f"Código {region['codigo']}: {region['nombre_oficial']}")
