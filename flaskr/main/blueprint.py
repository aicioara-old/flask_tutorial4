from flask_restplus import Api
from flask import Blueprint

from .controller.user_controller import api as user_ns

bp = Blueprint('api', __name__)

api = Api(bp,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
