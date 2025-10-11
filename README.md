# Tijuamon API

API REST educativa construida con **Python + Flask** para practicar fundamentos de backend gestionando criaturas ficticias llamadas **Tijuamones**.

## Objetivos
- Practicar desarrollo backend con Flask y SQLAlchemy.
- Exponer endpoints CRUD básicos sobre un modelo sencillo.
- Aprender a versionar la base de datos con Flask-Migrate (Alembic).
- Reforzar colaboración con Git (commits, ramas, PRs).

## Instalación
```bash
git clone https://github.com/<usuario>/tijuamon-api.git
cd tijuamon-api
python -m venv .venv          # Windows: py -3 -m venv .venv
.venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración de entorno
```bash
set FLASK_APP=app.py                 # Mac/Linux: export FLASK_APP=app.py
set ENV_CONFIG=DevelopmentConfig     # Mac/Linux: export ENV_CONFIG=DevelopmentConfig
```

## Migraciones de base de datos
```bash
flask db init              # Ejecutar una sola vez
flask db migrate -m "Inicial"
flask db upgrade
```

> Asegúrate de haber creado `src/extensions.py` con `db = SQLAlchemy()` y `migrate = Migrate()`
> y de inicializarlos en `src/__init__.py` antes de correr los comandos.

## Cargar datos iniciales (seed)
```bash
flask seed                 # Inserta entrenadores y tijuamones de ejemplo
```

> El comando `seed` vive en `src/__init__.py` y puedes editarlo para agregar más registros.

## Ejecutar la aplicación
```bash
flask run                  # Servidor de desarrollo
```

## Entidades principales
- **Tijuamon**
  - `id`: int (autoincremental)
  - `name`: str (nombre público)
  - `element_type`: str (por ejemplo: water, fire, electric)
  - `level`: int (rango 1–100 sugerido)
  - `hp`, `attack`, `defense`: ints > 0
  - `habilities`: lista de strings
- **Trainer**
  - `id`: int
  - `username`: str único
  - `email`: str único
  - `password_hash`: str

## Endpoints previstos
- `POST /tijuamones` — Crear un Tijuamon
- `GET /tijuamones` — Listar Tijuamones
  - filtros sugeridos: `?element_type=water`, `?name=pi`, `?min_level=30`
- `GET /tijuamones/<id>` — Consultar uno
- `PUT /tijuamones/<id>` — Actualizar
- `DELETE /tijuamones/<id>` — Eliminar
- (Opcional) `POST /batalla` — Simulación de combate
- (Opcional) `GET /estadisticas` — Estadísticas agregadas

## Equipo
Proyecto guía desarrollado por el profesor Ricardo Pérez Torres para la materia Backend I (CESUN).
