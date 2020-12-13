from flask import jsonify

class UserService:
    def __init__(self):
        pass 
    def create_new_user(self,new_user):
        return jsonify(new_user)