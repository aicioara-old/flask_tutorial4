from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns
from .controller.auth_controller import api as auth_ns

bp = Blueprint('api', __name__)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(bp,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          security='Bearer Auth',
          authorizations=authorizations,
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
