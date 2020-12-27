import os
import sys
from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity, get_raw_jwt
) 
from flask_restful import Resource, Api, reqparse
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../../mongodb")
from MongoDBHandler import MongoDBHandler

class UserService:
    def __init__(self):
        self.dbHandler = MongoDBHandler()

    def check_duplicate_id(self, submit_id):
        return self.dbHandler.check_duplicate_id(submit_id)

    def check_duplicate_nickname(self, submit_nickname):
        return self.dbHandler.check_duplicate_nickname(submit_nickname)

    def check_duplicate_lolname(self, submit_lolname):
        return self.dbHandler.check_duplicate_lolname(submit_lolname)

    def create_new_user(self, userInfo):
        print(userInfo)
        return self.dbHandler.insert_userinfo(userInfo)

    def authenticate(self, id, pw):
        # lol name 2글자면 가운데 공백 변환 필요
        # 회원가입시 -> self.dbHandler.insert_userinfo({'userid':id, 'password':pw, 'nickname':"테스트", 'lolname':"휘랑", 'friendslist': []})
        # self.dbHandler.insert_userinfo({'userid':id, 'password':pw, 'nickname':"테스트", 'lolname':"휘랑", 'friendslist': []})
        userInfo = self.dbHandler.get_userinfo_by_userid(id)
        if userInfo is not None:
            if userInfo['password'] == pw:
                return jsonify(
                    result = "success",
                    # 검증된 경우, access 토큰 반환
                    access_token = create_access_token(identity = id,
                                                    expires_delta = False)
                )
            else:
                return jsonify(
                result = "Worng Password!"
            )
	
        # 아이디, 비밀번호가 일치하지 않는 경우
        else:
            return jsonify(
                result = "Not Exist ID!"
            )

    def identity(payload):
        user_id = payload['identity']
        return userid_mapping.get(user_id, None)

    def get_userinfo_by_userid(self, id):
        return self.dbHandler.get_userinfo_by_userid(id)

    def get_friendslist_by_id(self, id):
        #userinfo = self.dbHandler.get_userinfo_by_userid(id)
        return self.dbHandler.get_friendslist_by_id(id)
        # lolname = userinfo['lolname']

    def save_friend_info(self, id, friend_info):
        return self.dbHandler.save_friend_info(id, friend_info)

    def delete_friend_info(self, id, lolname):
        return self.dbHandler.delete_friend_info(id, lolname)
