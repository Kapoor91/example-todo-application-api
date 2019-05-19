import pytest

from deepdiff import DeepDiff
from sqlalchemy import Table

from todo_api.app_file import db
from tests.fixtures.todos import todos_fixture


@pytest.fixture(scope='function')
def todos_session(session):
    table = Table(todos_fixture['table'], db.metadata)
    session.execute(table.insert(), todos_fixture['records'])


def test_find_todos_with_fixture(client_app, todos_session):
    expected = {
        'todos': todos_fixture['records']
    }

    req = client_app.get('/v0/todos')

    assert req.status_code == 200
    assert req.is_json
    assert DeepDiff(expected, req.json, ignore_order=True) == {}


def test_find_without_fixture(client_app, session):
    expected = {
        'todos': []
    }

    req = client_app.get('/v0/todos')

    assert req.status_code == 200
    assert req.is_json
    assert DeepDiff(expected, req.json, ignore_order=True) == {}
