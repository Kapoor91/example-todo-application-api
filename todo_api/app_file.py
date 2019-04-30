import connexion


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
    app.app.config.from_object(config_object)

    return app
