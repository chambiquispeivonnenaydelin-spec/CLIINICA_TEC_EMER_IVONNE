from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config.setdefault("TEMPLATES_AUTO_RELOAD", True)
    app.jinja_env.auto_reload = True

    db.init_app(app)
    login_manager.init_app(app)

    from .controllers.main_controller import main_bp
    from .controllers.medico_controller import medico_bp
    from .controllers.paciente_controller import paciente_bp
    from .controllers.consulta_controller import consulta_bp
    from .controllers.auth_controller import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(medico_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(auth_bp)

    return app