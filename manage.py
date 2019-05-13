from flask_script import Manager
from flask_migrate import MigrateCommand

from api import get_configured_app

app = get_configured_app()
manager = Manager(app.app)

manager.add_command('db', MigrateCommand)


@manager.option('-h', '--host', default='127.0.0.1',
                help='host to bind the server (default: 127.0.0.1)')
@manager.option('-p', '--port', default='8000',
                help='port to bind the server (default: 8000)')
def runserver(host, port):
    """Run an instance of the server"""
    app.run(host=host, port=port)


if __name__ == '__main__':
    manager.run()
