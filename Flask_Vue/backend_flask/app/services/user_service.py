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
# from security import authenticate, identity

class UserService:
    def __init__(self):
        pass 
    def create_new_user(self,new_user):
        return jsonify(new_user)

    def authenticate(username, password):
        if (id == "qwe" and
                pw == "123"):
                return jsonify(
                    result = "success",
                    # 검증된 경우, access 토큰 반환
                    access_token = create_access_token(identity = id,
                                                    expires_delta = False)
                )
	
        # 아이디, 비밀번호가 일치하지 않는 경우
        else:
            return jsonify(
                result = "Invalid Params!"
            )

    def identity(payload):
        user_id = payload['identity']
        return userid_mapping.get(user_id, None)
