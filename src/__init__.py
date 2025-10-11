import os
from flask import Flask
from src.models import Tijuamon, Trainer
from src.extensions import db
import click

def create_app(config_object: str | None = None) -> Flask:
    """"Create a Flask application using the app factory pattern."""
    app = Flask(__name__)
    _load_config(app, config_object)
    _register_extensions(app)
    _register_blueprints(app)
    _register_error_handlers(app)
    _register_cli(app)
    return app


def _load_config(app: Flask, config_object: str | None) -> None:
    """Load default settings, optionally overriding with a named config."""
    app.config.from_object("src.config.BaseConfig")
    if config_object:
        app.config.from_object(config_object)
    else:
        env_config = os.environ.get("ENV_CONFIG", "DevelopmentConfig")
        app.config.from_object(f"src.config.{env_config}")


def _register_extensions(app: Flask) -> None:
    """Register Flask extensions."""
    from src.extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

def _register_blueprints(app: Flask) -> None:
    """Register Flask blueprints.
    Blueprints are a way to organize your Flask application into smaller and reusable components.
    """
    from src.api.tijuamones import blueprint as tijuamones_bp
    from src.api.trainers import blueprint as trainers_bp

    app.register_blueprint(tijuamones_bp, url_prefix="/tijuamones")
    app.register_blueprint(trainers_bp, url_prefix="/trainers")
    

def _register_error_handlers(app: Flask) -> None:
    """Register error handlers."""
    pass

    # Example error handler:
    # @app.errorhandler(404)
    # def not_found_error(error):
    #     return render_template("404.html"), 404

def _register_cli(app: Flask) -> None:
    @app.cli.command("seed")
    def seed():
        """Seed the database with initial data."""
        if Tijuamon.query.first():
            print("Database already seeded.")
            return
        
        trainer = Trainer(username="ash", email="ash@example.com", password_hash="hashedpassword")
        tijuamones = [
            Tijuamon(name="Caguamon", element_type="Water", level=5, hp=30, attack=15, defense=10),
            Tijuamon(name="Choloko", element_type="Fire", level=7, hp=40, attack=12, defense=14),
        ]
        # Associate Tijuamones with the trainer
        trainer.tijuamones.extend(tijuamones)
        db.session.add(trainer)
        db.session.commit()
        click.echo("Database seeded!")