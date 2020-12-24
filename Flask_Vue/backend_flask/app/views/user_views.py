import requests 
from ..services.user_service import UserService
import json
from flask import (
    request,
    Blueprint,
    jsonify,
    redirect,
    url_for
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

        token = user_service.authenticate(id, pw)
        cur_user = get_jwt_identity()
        print(cur_user)
        return token
        return redirect(url_for('user_app.friendlist'), token = token[result])

    @user_app.route('/friendlist', methods=['POST'])
    @jwt_required
    def friendlist():
        return jsonify({'a':'b'})
        info = json.loads(request.get_data())
        friend_list = [
            {
                'real_name' : 'a',
                'nick_name' : 'b',
            },
            {
                'real_name' : 'c',
                'nick_name' : 'd'
            }
        ]

        cur_user = get_jwt_identity()
        if cur_user is None:
            return "User Only!"
        else:
            return jsonify(
                {
                    'friend_list' : friend_list,
                }
            )

        return response, 200

        return jsonify(
            {
                'friend_list' : friend_list,
            }
        )

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

