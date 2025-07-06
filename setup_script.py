#!/usr/bin/env python3
"""
Script para crear automáticamente el proyecto chile-data-cleaner
Ejecutar: python setup_project.py
"""

import os
import sys

def create_directory_structure():
    """Crea la estructura de directorios"""
    directories = [
        "chile_data_cleaner",
        "tests", 
        "docs",
        ".github/workflows"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Creado directorio: {directory}")

def create_files():
    """Crea todos los archivos con su contenido"""
    
    files_content = {
        # Archivo principal de la librería
        "chile_data_cleaner/regiones.py": '''"""
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
        texto_limpio = re.sub(r'\\s+', ' ', texto_sin_acentos.lower().strip())
        
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
    
    print("\\n=== Lista de Todas las Regiones ===")
    for region in cleaner.listar_regiones():
        print(f"Código {region['codigo']}: {region['nombre_oficial']}")
''',

        # __init__.py del paquete
        "chile_data_cleaner/__init__.py": '''"""
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
''',

        # Version
        "chile_data_cleaner/version.py": '''"""
Información de versión del paquete
"""

__version__ = "0.1.0"
''',

        # Tests
        "tests/__init__.py": '''"""
Tests para la librería Chile Data Cleaner
"""
''',

        # Setup.py (versión simplificada para el script)
        "setup.py": '''from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chile-data-cleaner",
    version="0.1.0",
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Librería para limpiar y normalizar datos específicos de Chile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/chile-data-cleaner",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Sin dependencias externas por ahora
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    keywords="chile data cleaning normalization regions ine",
    project_urls={
        "Bug Reports": "https://github.com/tu-usuario/chile-data-cleaner/issues",
        "Source": "https://github.com/tu-usuario/chile-data-cleaner",
        "Documentation": "https://github.com/tu-usuario/chile-data-cleaner#readme",
    },
)
''',

        # Requirements
        "requirements.txt": '''# Dependencias de producción
# Por ahora no hay dependencias externas requeridas
# La librería usa solo módulos de la biblioteca estándar de Python
''',

        "requirements-dev.txt": '''# Dependencias de desarrollo y testing
pytest>=6.0
pytest-cov>=2.0
black>=22.0
flake8>=4.0
mypy>=0.910

# Dependencias opcionales para desarrollo
twine>=4.0  # Para subir a PyPI
wheel>=0.37  # Para crear distribuciones
setuptools>=60.0  # Para empaquetado
''',

        # .gitignore
        ".gitignore": '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
''',

        # LICENSE
        "LICENSE": '''MIT License

Copyright (c) 2025 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''',

        # GitHub Actions CI
        ".github/workflows/ci.yml": '''name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
        pip install -e .

    - name: Run tests with pytest
      run: |
        pytest --cov=chile_data_cleaner --cov-report=xml

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install black flake8 mypy

    - name: Run black
      run: black --check .

    - name: Run flake8
      run: flake8 .

    - name: Run mypy
      run: mypy chile_data_cleaner/
''',

        # README.md
        "README.md": '''# Chile Data Cleaner

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
'''
    }
    
    # Crear archivos
    for file_path, content in files_content.items():
        # Crear directorio padre si no existe
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        
        # Escribir archivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Creado archivo: {file_path}")

def main():
    """Función principal"""
    print("🚀 Creando proyecto chile-data-cleaner...")
    print("=" * 50)
    
    # Verificar si ya existe el directorio
    if os.path.exists("chile_data_cleaner"):
        response = input("⚠️  El directorio ya existe. ¿Sobrescribir? (y/N): ")
        if response.lower() != 'y':
            print("❌ Operación cancelada")
            return
    
    try:
        # Crear estructura
        create_directory_structure()
        print()
        
        # Crear archivos
        create_files()
        print()
        
        print("✅ Proyecto creado exitosamente!")
        print()
        print("📋 Próximos pasos:")
        print("1. cd chile-data-cleaner")
        print("2. python -m venv venv")
        print("3. source venv/bin/activate  # En Windows: venv\\Scripts\\activate")
        print("4. pip install -e .")
        print("5. pip install -r requirements-dev.txt")
        print("6. pytest  # Para ejecutar tests")
        print("7. git init && git add . && git commit -m 'Initial commit'")
        print()
        print("🎉 ¡Listo para usar!")
        
    except Exception as e:
        print(f"❌ Error creando proyecto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
