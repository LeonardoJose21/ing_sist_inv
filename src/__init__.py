from src.database.db_connection import app

# Routes
from .routes import landing, rol, submit_role, sign_up, sign_up_validation, log_in, student, evaluator, admin

# app = Flask(__name__)


def init_app():
    # Configuration
    # app.config.from_object(config)

    # Blueprints
    app.register_blueprint(landing.main)
    app.register_blueprint(rol.main)
    app.register_blueprint(submit_role.main)
    app.register_blueprint(sign_up.main)
    app.register_blueprint(sign_up_validation.main)
    app.register_blueprint(log_in.main)
    app.register_blueprint(student.main)
    app.register_blueprint(evaluator.main)
    app.register_blueprint(admin.main)