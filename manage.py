from xmlrpc.server import ServerHTMLDoc
from app import create_app

# Creating app instance
app = create_app('development')

# Creating app instance
app = create_app('development')
manager = (app)
manager.add_command('server')

if __name__ == '__main__':
    manager.run()