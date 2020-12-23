import requests 
from ..services.user_service import UserService
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import json
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
        info = json.loads(request.get_data())
        id = info['id']
        pw = info['pw']
        print(id)
        data = request.json 

        response = user_service.create_new_user(data)

        return response, 200

    @user_app.route('/sign-up')
    def signup():
        user_service = UserService()
        data = request.json 

        response = user_service.create_new_user(data)

        return response, 200