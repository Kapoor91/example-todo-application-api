import os
from todo_api.app_file import get_app


def get_configured_app():
    """
    Get an API instance and run with configuration object depending on
    `TODO_APP_API_ENV` environment variable
    """
    api_env = os.getenv('TODO_APP_API_ENV', 'PRODUCTION').lower()
    configuration_object = 'config.conf_prod'

    if api_env == 'development':
        configuration_object = 'config.conf_local'
    elif api_env == 'testing':
        configuration_object = 'config.conf_testing'

    app = get_app(configuration_object)

    return app
