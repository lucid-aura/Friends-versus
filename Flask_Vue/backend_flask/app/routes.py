import flask
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from app import app
import sys
import os
from .RouteHandler import RouteHandler
import time
import datetime



#from ..logging.logging import log_time


@app.route('/', methods=["GET", "POST"])

def home():
    if request.method == 'GET':
        #language = request.form['language']
        #framework = request.args.get('framework')
        #framework = request.form['framework']
        #print(language)
        #print(framework)
        
        name = request.args.get('playerinfo')
        print("playerinfo 왔음")
        print(name)
        if name is not None:
            route_handler = RouteHandler.init_by_name(name)
            playerinfo = route_handler.searchPlayerInfo(name)
            print(playerinfo["revisionDate"])
            playerinfo["revisionDate"] = str(datetime.datetime.fromtimestamp(int(playerinfo["revisionDate"])/1000.0))
            print(playerinfo["revisionDate"])
            return playerinfo
        #####################################
        # 정말 긴 시간 끝에 알아낸 사실....
        # GET 방식은 request.args.get('name') 으로 받아오고
        # POST는 request.form['name'] 으로 받아온다....
        # 문제는 form 형식이 아닐때는 어떻게 받아오는가??
        #  -> axios로 request 날린다.
        #####################################


        # nickname = request.form['nickname']
        # print(nickname)
    #my_res = flask.Response(jsonify(test[0]))
    #my_res.headers["Access-Control-Allow-Origin"] = "*"

    a = jsonify({'error':"noting loaded"})
    return a

@app.route('/playerinfo', methods=["GET"])
def playerinfo():
    # name = request.form['data']
    # rH = routeHandler.init_by_name(name)
    # playerinfo = rH.test(name)
    # return playerinfo
    # data = request.get_json()
    # print(data)
    if request.method == 'GET': 
        name = request.form['playerinfo']
        print(name)
        route_handler = RouteHandler.init_by_name(name)
        playerinfo = route_handler.searchPlayerInfo(name)
        return playerinfo
            
    return jsonify('')
    

@app.route('/friendlist')
def friendlist():
    friend_list = [
        {
            'real_name' : '현상현',
            'nick_name' : '휘랑',
        },
        {
            'real_name' : '안상원',
            'nick_name' : '피곤한통닭'
        }
    ]
    return jsonify(
        {
            'status' : 'success',
            'friend_list' : friend_list
        }
    )