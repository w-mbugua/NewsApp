from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    # setting up configuration
    app.config.from_object(config_options[config_name])

    # extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app