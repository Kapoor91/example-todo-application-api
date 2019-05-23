import os

ENV = 'production'


def get_conf_value(variable_name):
    """ Allow to give file path to set environnment variable.
    This will mostly be used to read docker secret
    """
    var_file_path = os.environ[variable_name+'_FILE']
    if var_file_path:
        return open(var_file_path, 'r').read().strip()
    else:
        return os.environ[variable_name]


_DB_USERNAME = get_conf_value('DB_USERNAME')
_DB_PASSWORD = get_conf_value('DB_PASSWORD')
_DB_IP = os.environ['DB_IP']
_DB_PORT = os.getenv('DB_PORT', '5432')
_DB_NAME = os.getenv('DB_NAME', 'todo_app_db')

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' \
    + '{db_username}:{db_password}@{db_ip}:{db_port}/{db_name}'.format(
        db_username=_DB_USERNAME,
        db_password=_DB_PASSWORD,
        db_ip=_DB_IP,
        db_port=_DB_PORT,
        db_name=_DB_NAME,
    )

SQLALCHEMY_TRACK_MODIFICATIONS = False
