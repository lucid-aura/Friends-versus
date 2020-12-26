import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/model")
from data_dao import DataDAO
import json
from bson import json_util

class UserService:
    def __init__(self):
        self.data_dao = DataDAO()
    
    def insert_userinfo(self, userInfo):
        result = self.data_dao.insert_item("USER", "INFO", userInfo)
        return result

    def get_userinfo_by_userid(self, userId):
        result = self.data_dao.find_item("USER", "INFO", "userid", userId)
        #print(list(collection.find()))
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
