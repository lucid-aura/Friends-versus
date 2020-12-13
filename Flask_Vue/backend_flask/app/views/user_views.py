import requests 
from ..services.user_service import UserService


from flask import (
    request,
    Blueprint,
    jsonify
)

class UserView:
    user_app = Blueprint('user_app', __name__, url_prefix='/user')

    @user_app.route('/sign-in', methods=['POST'])
    def signin():
        user_service = UserService()
        data = request.json 

        response = user_service.create_new_user(data)

        return response, 200