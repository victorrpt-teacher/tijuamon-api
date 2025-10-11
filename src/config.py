import os
"""
Módulo de configuración para la aplicación.
Descripción general
- Provee rutas y configuraciones reutilizables para entornos (desarrollo, pruebas, producción).
- Usa pathlib.Path para gestionar rutas de forma portátil y os.environ para leer variables de entorno.
- Incluye una función auxiliar para construir URIs de SQLite y tres clases de configuración (BaseConfig, DevelopmentConfig, TestingConfig, ProductionConfig).
BASE_DIR (explicación detallada y clara)
- Expresión: Path(__file__).resolve().parent.parent
    1. __file__: nombre de archivo del módulo actual (ej. "/C:/.../src/config.py").
    2. Path(__file__): crea un objeto pathlib.Path apuntando al archivo actual.
    3. .resolve(): convierte la ruta a su forma absoluta y canónica (resuelve enlaces simbólicos y referencias relativas),
         garantizando una ruta completa y sin ambigüedades.
    4. .parent: sube un nivel — devuelve el directorio que contiene el archivo (ej. la carpeta "src").
    5. .parent.parent: sube un segundo nivel — habitualmente el directorio raíz del proyecto.
- Resultado: BASE_DIR es un objeto Path que representa la raíz del proyecto. Usar Path facilita unir rutas (p. ej. BASE_DIR / "instance")
    y trabajar de forma consistente entre sistemas operativos (Windows, macOS, Linux).
Otras variables y utilidades
- INSTANCE_DIR: BASE_DIR / "instance"
    - Carpeta dedicada a datos locales y configuraciones que no deberían ir a control de versiones.
    - Es aconsejable crear esta carpeta al desplegar o arrancar la aplicación si no existe.
- _sqlite_uri(filename: str) -> str
    - Construye una cadena con la URI usada por SQLAlchemy para SQLite, ubicando el archivo dentro de INSTANCE_DIR.
    - Devuelve una cadena del tipo "sqlite:///<ruta_al_archivo>" construida con pathlib para obtener la ruta correcta por plataforma.
Clases de configuración
- BaseConfig
    - SECRET_KEY: leído desde la variable de entorno "SECTRET_KEY" (nota: parece haber un typo; normalmente se usa "SECRET_KEY").
    - JSON_SORT_KEYS = False: mantiene el orden de las claves en las respuestas JSON tal como fueron definidas.
    - SQLALCHEMY_TRACK_MODIFICATIONS = False: desactiva el seguimiento de modificaciones para evitar overhead si se usa SQLAlchemy.
- DevelopmentConfig (hereda BaseConfig)
    - DEBUG = True
    - SQLALCHEMY_DATABASE_URI: toma DATABASE_URL de entorno o por defecto usa un SQLite local en instance/dev.sqlite3.
- TestingConfig
    - TESTING = True
    - SQLALCHEMY_DATABASE_URI: uso de SQLite en memoria (útil para pruebas aisladas y rápidas).
- ProductionConfig
    - SQLALCHEMY_DATABASE_URI: toma DATABASE_URL de entorno o usa un valor por defecto.
    - Atención: en el código fuente el valor por defecto pasado a _sqlite_uri es "sqlite:///prod.db", lo que parece duplicar el prefijo URI;
        lo más habitual sería pasar solo el nombre de archivo "prod.db" a _sqlite_uri.
Notas y recomendaciones
- Verificar y corregir el nombre de la variable de entorno SECRET_KEY si procede (evitar el typo "SECTRET_KEY").
- Asegurarse de que INSTANCE_DIR exista en tiempo de ejecución (crear la carpeta si no existe).
- Al formar URIs de SQLite en Windows hay que prestar atención al número de barras y a la representación de la unidad (p. ej. "C:\\..."),
    por eso usar pathlib para componer rutas y después convertir a string es una práctica recomendada.
"""
from pathlib import Path

# 
BASE_DIR = Path(__file__).resolve().parent.parent
# Instance dir is for configurations and local data that shouldn't be in version control
INSTANCE_DIR = BASE_DIR / "instance"

def _sqlite_uri(filename: str) -> str:
    """Construye la URI de SQLite dentro de la carpeta instance/."""
    return f"sqlite:///{INSTANCE_DIR / filename}"

class BaseConfig:
    SECRET_KEY = os.environ.get("SECTRET_KEY", "dev")
    JSON_SORT_KEYS = False  # To keep the order of JSON responses as defined
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # If using SQLAlchemy

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("dev.sqlite3")
    )

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("sqlite:///prod.db")
    )

# You can add more configurations as needed
# DATABASE_URL  = "postgresql+psycopg2://user:password@localhost/dbname"
# DATABASE_URL  = "mysql+pymysql://user:password@localhost/dbname"
# DATABASE_URL  = "sqlite:////absolute/path/to/database.db"
# DATABASE_URL  = "mariadb+pymysql://user:password@localhost/dbname"
# Si utilizan SQLServer>
# DATABASE_URL  = "mssql+pyodbc://user:password@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server"