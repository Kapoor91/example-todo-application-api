import pytest
from flask import json

from deepdiff import DeepDiff
from sqlalchemy import Table

from todo_api.app_file import db
from tests.fixtures.todos import todos_fixture
from todo_api.models.Todos import Todos


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


@pytest.mark.parametrize('payload, expected', [
    (
        {'title': 'MyTitleTest1', 'description': 'MyDescriptionTest1'},
        {'title': 'MyTitleTest1', 'description': 'MyDescriptionTest1'}
    ),
    (
        {'title': 'MyTitleTest2'},
        {'title': 'MyTitleTest2', 'description': ''}
    )
])
def test_create_todos(payload, expected, client_app, session):
    req = client_app.post('/v0/todos', json=payload)

    assert req.status_code == 201
    assert req.json['todo']['title'] == expected['title']
    assert req.json['todo']['description'] == expected['description']
    assert req.json['todo']['done'] == False  # noqa: E712,E261


def test_find_todos_by_id(client_app, todos_session):
    todo_id = 1
    expected = {
        'todo': {
            'id': 1,
            'title': 'Todo 1',
            'description': 'Description 1',
            'done': False
        }
    }

    req = client_app.get('/v0/todos/{todo_id}'.format(todo_id=todo_id))

    assert req.status_code == 200
    assert DeepDiff(expected, req.json, ignore_order=True) == {}


def test_update_todos_by_id(client_app, todos_session):
    todo_id = 1
    payload = {
        'title': 'Blablo'
    }
    expected = {
        'todo': {
            'id': 1,
            'title': 'Blablo',
            'description': 'Description 1',
            'done': False
        }
    }

    # BUG: when using json=payload, call don't find the todo by id
    req = client_app.put('/v0/todos/{todo_id}'.format(todo_id=todo_id),
                         data=json.dumps(payload),
                         headers={"Content-Type": "application/json"})

    assert req.status_code == 200
    assert DeepDiff(expected, req.json, ignore_order=True) == {}


def test_update_todos_by_id_create(client_app, todos_session):
    todo_id = 9999

    payload = {
        'title': 'SomeTitle'
    }
    expected = {
        'title': 'SomeTitle',
        'description': '',
        'done': False
    }

    req = client_app.put('/v0/todos/{todo_id}'.format(todo_id=todo_id),
                         data=json.dumps(payload),
                         headers={"Content-Type": "application/json"})

    assert req.status_code == 201
    assert req.json['todo']['title'] == expected['title']
    assert req.json['todo']['description'] == expected['description']
    assert req.json['todo']['done'] == expected['done']


def test_delete_todos_by_id_200(client_app, todos_session):
    todo_id = 2
    expected = {
        'todo': {
            'id': 2,
            'title': 'Todo 2',
            'description': 'Description 2',
            'done': True
        }
    }

    req = client_app.delete('/v0/todos/{todo_id}'.format(todo_id=todo_id))

    assert req.status_code == 200
    assert DeepDiff(expected, req.json, ignore_order=True) == {}
    assert Todos.query.get(todo_id) is None


def test_delete_todos_by_id_404(client_app, session):
    todo_id = 2

    req = client_app.delete('/v0/todos/{todo_id}'.format(todo_id=todo_id))

    assert req.status_code == 404
