from flask import request
from flask_restplus import Resource

from ..service.auth_service import Auth
from ..util.serializers import AuthSerializer

api = AuthSerializer.api
dto = AuthSerializer.dto


@api.route('/login')
class UserLogin(Resource):
    @api.expect(dto, validate=True)
    def post(self):
        """Login and retrieve JWT token"""
        post_data = request.json
        return Auth.login_user(data=post_data)



@api.route('/logout')
class LogoutAPI(Resource):
    def post(self):
        """Logout and invalidate JWT token"""
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)