from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from importlib import import_module

db = SQLAlchemy()
ma = Marshmallow()

MODELS = {'Todos'}


def load_models():
    """ To allow multiple models file we need to import them before the Migrate command"""
    # todo: use an auto loader
    for model in MODELS:
        import_module('todo_api.models.{}'.format(model))
