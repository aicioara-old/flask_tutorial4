import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flaskr.main import create_app, db

# Add all models individually here
from flaskr.main.model import user, blacklist
from flaskr.main.blueprint import bp

app = create_app(os.getenv('PYTHON_ENVIRONMENT') or 'dev')
app.register_blueprint(bp)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('flaskr/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
