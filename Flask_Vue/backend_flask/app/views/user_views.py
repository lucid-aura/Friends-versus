import requests 
from ..services.user_service import UserService
import json
from flask import (
    request,
    Blueprint,
    jsonify
)
from flask_jwt_extended import *

class UserView:
    user_app = Blueprint('user_app', __name__, url_prefix='/user')

    @user_app.route('/sign-in', methods=['POST'])
    def signin():
        user_service = UserService()
        info = json.loads(request.get_data())
        id = info['id']
        pw = info['pw']
        print(id)

        user_service.authenticate(username, password)
        

        # return response, 200

    # @user_app.route('/sign-up', methods=['POST'])

    # def signup():
    #     @Auth.expect(user_fields_auth)
    #     @Auth.doc(responses={200: 'Success'})
    #     @Auth.doc(responses={500: 'Register Failed'})

    #     name = request.json['name']
    #     password = request.json['password']
    #     if name in users:
    #         return {
    #             "message": "Register Failed"
    #         }, 500
    #     else:
    #         users[name] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())  # 비밀번호 저장
    #         return {
    #             'Authorization': jwt.encode({'name': name}, "secret", algorithm="HS256").decode("UTF-8")  # str으로 반환하여 return
    #         }, 200
    #     user_service = UserService()
    #     data = request.json 

    #     response = user_service.create_new_user(data)

    #     return response, 200

    # @jwt_required()
    # def get(self, name):

    #     item = next(filter(lambda x: x['name'] == name, items), None)

    #     return {'item': item}, 200 if item else 404

