from flask import Flask
# Import extensions lazily here once you add them.
# from src.extensions import db

def create_app(config_object: str | None = None) -> Flask:
    """"Create a Flask application using the app factory pattern."""
    app = Flask(__name__)
    _load_config(app, config_object)
    _register_extensions(app)
    _register_blueprints(app)
    _register_error_handlers(app)
    return app



def _load_config(app: Flask, config_object: str | None) -> None:
    """Load default settings, optionally overriding with a named config."""
    app.config.from_mapping(
        SECRET_KEY="dev",
        JSON_SORT_KEYS=False,  # To keep the order of JSON responses as defined
    )
    if config_object:
        app.config.from_object(config_object)


def _register_extensions(app: Flask) -> None:
    """Register Flask extensions."""
    # db.init_app(app)
    pass

def _register_blueprints(app: Flask) -> None:
    """Register Flask blueprints.
    Blueprints are a way to organize your Flask application into smaller and reusable components.
    """
    from src.api.tijuamones import blueprint as tijuamones_bp

    app.register_blueprint(tijuamones_bp, url_prefix="/tijuamones")
    

def _register_error_handlers(app: Flask) -> None:
    """Register error handlers."""
    pass

    # Example error handler:
    # @app.errorhandler(404)
    # def not_found_error(error):
    #     return render_template("404.html"), 404
