"""
Chile Data Cleaner - Librería para limpiar datos específicos de Chile
====================================================================

Una librería Python para normalizar y limpiar datos específicos de Chile.
Comenzamos con la normalización de regiones según la codificación oficial del INE.

Ejemplos básicos:
    >>> from chile_data_cleaner import normalizar_region_chile
    >>> normalizar_region_chile("valpo")
    {'codigo': 5, 'nombre_oficial': 'Valparaíso'}
    
    >>> from chile_data_cleaner import ChileDataCleaner
    >>> cleaner = ChileDataCleaner()
    >>> cleaner.normalizar_region("RM")
    {'codigo': 13, 'nombre_oficial': 'Metropolitana de Santiago'}
"""

from .regiones import ChileDataCleaner, normalizar_region_chile
from .version import __version__

__all__ = ['ChileDataCleaner', 'normalizar_region_chile', '__version__']

# Información del paquete
__author__ = 'Tu Nombre'
__email__ = 'tu.email@ejemplo.com'
__description__ = 'Librería para limpiar y normalizar datos específicos de Chile'
