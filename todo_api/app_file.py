import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from todo_api.models import db, load_models


def get_app(config_object):
    """
    Get an API instance of the Todo APP

    :param config_object: Flask configuration file for the API
    :type config_object: str
    :return: API instance configured with the openAPI file and given config_object
    :rtype: connexion.FlaskApp
    """
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('api.yaml')

    flask_app = app.app
    flask_app.config.from_object(config_object)
    setup_db(flask_app)

    return app


def setup_db(flask_app):
    """
    Setup the Flask-SQLAlchemy database with the given Flask application

    :param flask_app: Flask application to init
    :type flask_app: connexion.FlaskApp.app
    """
    db.init_app(flask_app)
    load_models()
    Migrate(flask_app, db)
