import pytest

from config import conf_testing
from todo_api.app_file import get_app, db

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()


@pytest.yield_fixture(scope='session')
def flask_app():
    app = get_app(conf_testing)
    db.app = app.app
    db.create_all()

    ctx = app.app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope='function')
def session():
    session = db.session()

    yield session

    session.rollback()
    session.close()


@pytest.fixture
def client_app(flask_app):
    return flask_app.app.test_client()
