# Chile Data Cleaner

Una librería Python para normalizar y limpiar datos específicos de Chile. Comenzamos con la normalización de regiones según la codificación oficial del INE (Instituto Nacional de Estadísticas).

## 🚀 Características

- ✅ Normalización de regiones de Chile al código oficial del INE
- ✅ Soporte para múltiples variantes y formas de escribir las regiones
- ✅ Manejo de acentos y caracteres especiales
- ✅ Validación de regiones existentes
- ✅ API simple y fácil de usar

## 📦 Instalación

```bash
pip install chile-data-cleaner
```

O para desarrollo:

```bash
git clone https://github.com/tu-usuario/chile-data-cleaner.git
cd chile-data-cleaner
pip install -e .
```

## 🔧 Uso

### Normalización de Regiones

```python
from chile_data_cleaner import ChileDataCleaner

# Crear instancia
cleaner = ChileDataCleaner()

# Normalizar diferentes variantes
result = cleaner.normalizar_region("valpo")
print(result)  # {'codigo': 5, 'nombre_oficial': 'Valparaíso'}

result = cleaner.normalizar_region("RM")
print(result)  # {'codigo': 13, 'nombre_oficial': 'Metropolitana de Santiago'}

result = cleaner.normalizar_region("bio bio")
print(result)  # {'codigo': 8, 'nombre_oficial': 'Biobío'}

# También funciona con códigos numéricos
result = cleaner.normalizar_region(13)
print(result)  # {'codigo': 13, 'nombre_oficial': 'Metropolitana de Santiago'}
```

### Función de Conveniencia

```python
from chile_data_cleaner import normalizar_region_chile

# Uso directo sin crear instancia
result = normalizar_region_chile("VIII región")
print(result)  # {'codigo': 8, 'nombre_oficial': 'Biobío'}
```

### Validación de Regiones

```python
cleaner = ChileDataCleaner()

# Validar si una región existe
is_valid = cleaner.validar_region("Valparaíso")
print(is_valid)  # True

is_valid = cleaner.validar_region("Region Inexistente")
print(is_valid)  # False
```

### Listar Todas las Regiones

```python
cleaner = ChileDataCleaner()

# Obtener lista completa de regiones
regiones = cleaner.listar_regiones()
for region in regiones:
    print(f"Código {region['codigo']}: {region['nombre_oficial']}")
```

## 🗺️ Regiones Soportadas

La librería reconoce todas las 16 regiones de Chile según la codificación oficial del INE:

| Código | Región |
|--------|--------|
| 15 | Arica y Parinacota |
| 1 | Tarapacá |
| 2 | Antofagasta |
| 3 | Atacama |
| 4 | Coquimbo |
| 5 | Valparaíso |
| 13 | Metropolitana de Santiago |
| 6 | Libertador General Bernardo O'Higgins |
| 7 | Maule |
| 16 | Ñuble |
| 8 | Biobío |
| 9 | Araucanía |
| 14 | Los Ríos |
| 10 | Los Lagos |
| 11 | Aysén del General Carlos Ibáñez del Campo |
| 12 | Magallanes y de la Antártica Chilena |

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Confirma tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Empuja a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

Tu Nombre - tu.email@ejemplo.com

Link del Proyecto: [https://github.com/tu-usuario/chile-data-cleaner](https://github.com/tu-usuario/chile-data-cleaner)
