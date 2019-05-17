import os
from todo_api.app_file import get_app


def run_app():
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
    app.run(port=8000)


if __name__ == '__main__':
    run_app()
