from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='User email address'),
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User password'),
        'public_id': fields.String(description='User ID')
    })



class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
