import os
import unittest
from flask import render_template
from app import blueprint
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from app.main import create_app, db
from app.main.controller.coupon_controller import routes_blueprint


load_dotenv()

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.register_blueprint(routes_blueprint)
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    print(f"Running on {os.getenv('BOILERPLATE_ENV')} environment")
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
