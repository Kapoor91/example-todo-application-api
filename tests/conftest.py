import pytest
from sqlalchemy import Table

from config import conf_testing
from todo_api.app_file import get_app, db
from tests.fixtures.todos import todos_fixture


@pytest.yield_fixture(scope='session')
def flask_app():
    app = get_app(conf_testing)
    db.app = app.app
    db.create_all()

    ctx = app.app.app_context()
    ctx.push()

    conn = db.engine.connect()
    table = Table(todos_fixture['table'], db.metadata)
    conn.execute(table.insert(), todos_fixture['records'])

    yield app
    ctx.pop()


@pytest.fixture
def client_app(flask_app):
    return flask_app.app.test_client()
