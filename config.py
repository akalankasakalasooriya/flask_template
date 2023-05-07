import os
from flask_cors import CORS
from flask_uuid import FlaskUUID
from flask_session import Session
from routes import routes_blueprint
from flask_jwt_extended import JWTManager
from flask_log_request_id import RequestID
basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("create instance once")
            cls._instances[cls] = super(
                ConfigMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=ConfigMeta):
    DEPLOYMENT_ENV = os.getenv("DEPLOYMENT_ENV", "dev")


def config_app(app):
    # app.config['DEBUG'] = False
    app.config['DEBUG'] = True
    CORS(app)
    RequestID(app)
    flask_uuid = FlaskUUID()
    flask_uuid.init_app(app)
    app.register_blueprint(routes_blueprint)

    jwt = JWTManager(app)
    Session(app)
