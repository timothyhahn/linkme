from flask.ext.script import Manager, Server

from linkme import app

manager = Manager(app)
manager.add_command('runserver', Server())

@manager.command
def init_db():
    from linkme import db
    db.create_all()
    
if __name__ == "__main__":
    manager.run()


