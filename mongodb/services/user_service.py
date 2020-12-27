import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/model")
from data_dao import DataDAO
import json
from bson import json_util

class UserService:
    def __init__(self):
        self.data_dao = DataDAO()
    
    def check_duplicate_id(self, submit_id):
        result = self.data_dao.find_item("USER", "INFO", "userid", submit_id)
        print(result)
        if result is None:
            return True
        else:
            return False

    def check_duplicate_nickname(self, submit_nickname):
        result = self.data_dao.find_item("USER", "INFO", "nickname", submit_nickname)
        print(result)
        if result is None:
            return True
        else:
            return False

    def check_duplicate_lolname(self, submit_lolname):
        result = self.data_dao.find_item("USER", "INFO", "lolname", submit_lolname)
        print(result)
        if result is None:
            return True
        else:
            return False

    def insert_userinfo(self, userInfo):
        print(userInfo)
        result = self.data_dao.insert_item("USER", "INFO", userInfo)
        return result

    def get_userinfo_by_userid(self, userId):
        result = self.data_dao.find_item("USER", "INFO", "userid", userId)
        return result

    def insert_friend_info(self, friendInfo):
        result = self.data_dao.insert_item("USER", "FRIENDS", friendInfo)

    def save_friend_info(self, id, friendInfo):
        # frienedInfo 는 딕셔너리
        userInfo = self.get_userinfo_by_userid(id)
        friendslist = userInfo['friendslist']

        friendslist.append(friendInfo)
        new = dict()
        new['friendslist'] = friendslist

        return self.data_dao.update_friendslist(id, new)
        #return self.data_dao.update_item("userid", userInfo['userid'], "friendslist", new, "USER", 'INFO')
        # return self.data_dao.update_friendslist(id, friendslist)

    def delete_friend_info(self, id, lolname):
        return self.data_dao.delete_friendslist(id, lolname)

    def find_friend_in_friendlist_by_realname(self, friendlist, realname):
        for idx in range(len(friendlist)):
            if friendlist[idx]['realname'] == realname:
                return friendlist[idx]

    def find_friend_in_friendlist_by_lolname(self, friendlist, lolname):
        for idx in range(len(friendlist)):
            if friendlist[idx]['lolname'] == lolname:
                return friendlist[idx]

    def find_friend_in_friendlist_by_memo(self, friendlist, memo):
        for idx in range(len(friendlist)):
            if friendlist[idx]['memo'] == memo:
                return friendlist[idx]
