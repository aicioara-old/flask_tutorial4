from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns

bp = Blueprint('api', __name__, url_prefix='/api')

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(bp,
    title='Flask Restplus Api Boiler-plate with JWT',
    description='A boilerplate for Flask-RESTplus web service',
    version='1.0',
    security='Bearer Auth',
    authorizations=authorizations,
    license='MIT',
    license_url='https://opensource.org/licenses/MIT',
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
