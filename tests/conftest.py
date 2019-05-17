import pytest

from todo_api.app_file import get_app
from config import conf_testing


@pytest.fixture
def flask_app():
    app = get_app(conf_testing)
    yield app


@pytest.fixture
def client_app(flask_app):
    return flask_app.app.test_client()
