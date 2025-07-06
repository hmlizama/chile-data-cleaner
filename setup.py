from setuptools import setup, find_packages

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
