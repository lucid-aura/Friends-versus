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
        return token
        # return redirect(url_for('user_app.friendlist'), token = token[result])

    @user_app.route('/sign-up', methods=['POST'])
    def signup():
        print("signup")
        user_service = UserService()
        info = json.loads(request.get_data())
        print(info)
        check = info['check'] # id, pw, lolname, nickname, submit
        if check == 'id':
            id = info['id']
            if user_service.check_duplicate_id(id) is True:        
                return {'result':'success'}
            else:
                return {'result':'fail'}
        elif check == 'nickname':
            nickname = info['nickname']
            if user_service.check_duplicate_nickname(nickname) is True:        
                return {'result':'success'}
            else:
                return {'result':'fail'}
        elif check == 'lolname':
            lolname = info['lolname']
            if user_service.check_duplicate_lolname(lolname) is True and user_service.check_exist_lolname(lolname) is True:        
                return {'result':'success'}
            else:
                return {'result':'fail'}
        else: # submit
            userInfo = dict()
            userInfo['userid'] = info['id']
            userInfo['password'] = info['pw']
            userInfo['nickname'] = info['nickname']
            userInfo['lolname'] = info['lolname']
            userInfo['friendslist'] = []
            res = user_service.create_new_user(userInfo)
            if res is not None:
                return {'result':'success'}
            else:
                return {'result':'fail'}

    @user_app.route('/friendlist', methods=['GET', 'POST'])
    @jwt_required
    def friendlist():
        user_service = UserService()
        id = get_jwt_identity()
        if request.method == 'POST':
            print("frinedlist come")
            user = user_service.get_userinfo_by_userid(id)
            nickname = user['nickname']
            print(nickname)
            return jsonify(nickname, user_service.get_friendslist_by_id(id))
        else:
            func = request.args.get('call')
            if func == 'insert':
                print("Insert 실행")
                
                friend_info = dict()
                friend_info['realname'] = request.args.get('realname')
                friend_info['lolname'] = request.args.get('lolname')
                friend_info['memo'] = request.args.get('memo') 

                if user_service.check_exist_lolname(friend_info['lolname']) is False:
                    return jsonify({'error':"존재하지 않는 소환사 이름"})
                check = user_service.get_friendslist_by_id(id)    
                # if check is None:
                if len(check) != 0: # 중복검사
                    for i in check:
                        if i['lolname'] == request.args.get('lolname'):
                            return jsonify({'error':"이미 존재하는 롤 친구입니다."})
                            
                user_service.save_friend_info(id, friend_info)
            elif func == 'delete':
                print("Delete 실행")
                lolname = request.args.get('lolname')
                user_service.delete_friend_info(id, lolname)
            return jsonify(user_service.get_friendslist_by_id(id))
            # return jsonify(
            #     {
            #         'realname' : realName,
            #         'lolname' : nickName,
            #         'memo' : memo
            #     }
            # )

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

