import flask
from flask import Flask, render_template, request, jsonify, Response, send_file, make_response
from flask_cors import CORS, cross_origin
from app import app
import sys
import os
from .RouteHandler import RouteHandler
import time
import datetime
import base64
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

        if name is not None:
            route_handler = RouteHandler.init_playerinfo_by_name(name)
            if route_handler is not None:
                print("존재하는 소환사 이름")
                playerinfo = route_handler.searchPlayerInfo(name)
                playerinfo["revisionDate"] = str(datetime.datetime.fromtimestamp(int(playerinfo["revisionDate"])/1000.0))
                return jsonify(playerinfo)
            
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

    e = jsonify({'name':""})
    return e

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
        route_handler = RouteHandler.init_playerinfo_by_name(name)
        playerinfo = route_handler.searchPlayerInfo(name)
        return playerinfo
            
    return jsonify('')
    
@app.route('/championlist', methods=["POST"])
def championlist():
    if request.method == 'POST':
        route_handler = RouteHandler()
        if route_handler.countSummaryChampions() == 0:
            route_handler.createSummaryChampions()
            route_handler.createChampioninfoData()
        result = route_handler.getSummaryChampions()
        return jsonify(result)

    e = jsonify({'erroring':"noting loaded..."})
    return e

@app.route('/championinfo', methods=["GET"])
def championinfo():
    print("enter championinfo")
    if request.method == 'GET':
        id = request.args.get('championinfo')
        print("championinfo GET")
        route_handler = RouteHandler()
        result = route_handler.getChampioninfoData(id)
        return jsonify(result)
    
    e = jsonify({'erroring':"noting loaded!"})
    return e

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

@app.route('/itemlist', methods=["GET"])
def itemlist():
    #if request.method == 'GET':

    # 첫 실행 시.
    route_handler = RouteHandler()
    # res = route_handler.create_loading_images()
    # res = route_handler.create_splash_images()
    # res = route_handler.create_square_images()
    res = route_handler.create_champion_spell_images()

    # if route_handler.checkSummaryChampions() == 0:
    #     print("요약에 챔피언 넣습니다.")
    #     route_handler.createSummaryChampions()
    # print(res)
    # DB 체크가 필요하다.
    # route_handler.insert_loading_image_by_champion_skin_id("Zoe", "Zoe_19")

    if route_handler.count_loading_champion_image() != 0:
        binary_image = route_handler.get_loading_image_by_champion_skin_id("Zoe_19")['img']
        payload= base64.b64encode(binary_image).decode('utf-8')
    return jsonify({"raw":payload})
