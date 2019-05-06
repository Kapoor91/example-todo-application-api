import os

ENV = 'production'

_DB_USERNAME = os.environ['DB_USERNAME']
_DB_PASSWORD = os.environ['DB_PASSWORD']
_DB_IP = os.environ['DB_IP']
_DB_PORT = os.environ['DB_PORT']
_DB_NAME = os.environ['DB_NAME']

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://' \
    + '{db_username}:{db_password}@{db_ip}:{db_port}/{db_name}'.format(
        db_username=_DB_USERNAME,
        db_password=_DB_PASSWORD,
        db_ip=_DB_IP,
        db_port=_DB_PORT,
        db_name=_DB_NAME,
    )
