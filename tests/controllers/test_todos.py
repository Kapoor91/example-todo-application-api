from deepdiff import DeepDiff

from todo_api.models.Todos import Todos
from tests.fixtures.todos import todos_fixture


def test_find_todos(client_app):
    expected = {
        'todos': todos_fixture['records']
    }

    req = client_app.get('/v0/todos')

    assert req.status_code == 200
    assert req.is_json == True
    assert DeepDiff(expected, req.json, ignore_order=True) == {}
