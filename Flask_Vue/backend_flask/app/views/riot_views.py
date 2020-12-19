from flask import (
    Flask, 
    render_template, 
    request, 
    jsonify, 
    Response, 
    send_file, 
    make_response,
    Blueprint
)
from flask_cors import CORS, cross_origin
import sys, os, time, datetime, base64, flask
from ..services.riot_service import RiotService
#from ..logging.logging import log_time


class RiotView:
    riot_app = Blueprint('riot_app', __name__, url_prefix='/riot')

    # @riot_app.route('/', methods=["GET", "POST"])
    # def home():
    #     if request.method == 'GET':
    #         #language = request.form['language']
    #         #framework = request.args.get('framework')
    #         #framework = request.form['framework']
    #         #print(language)
    #         #print(framework)
            
    #         name = request.args.get('playerinfo')
            
    #         if name is not None:
    #             riot_service = RiotService.init_playerinfo_by_name(name)
    #             if riot_service is not None:
    #                 print("존재하는 소환사 이름")
    #                 playerinfo = riot_service.searchPlayerInfo(name)
    #                 playerinfo["revisionDate"] = str(datetime.datetime.fromtimestamp(int(playerinfo["revisionDate"])/1000.0))
    #                 return jsonify(playerinfo)
                
    #         #####################################
    #         # 정말 긴 시간 끝에 알아낸 사실....
    #         # GET 방식은 request.args.get('name') 으로 받아오고
    #         # POST는 request.form['name'] 으로 받아온다....
    #         # 문제는 form 형식이 아닐때는 어떻게 받아오는가??
    #         #  -> axios로 request 날린다.
    #         #####################################


    #         # nickname = request.form['nickname']
    #         # print(nickname)
    #     #my_res = flask.Response(jsonify(test[0]))
    #     #my_res.headers["Access-Control-Allow-Origin"] = "*"

    #     return render_template('index.html')

    @riot_app.route('/playerinfo', methods=["GET"])
    def playerinfo():
        # name = request.form['data']
        # rH = RiotService.init_by_name(name)
        # playerinfo = rH.test(name)
        # return playerinfo
        # data = request.get_json()
        # print(data)
        if request.method == 'GET': 
            name = request.args.get('name')
            print(name)
            riot_service = RiotService.init_playerinfo_by_name(name)
            playerinfo = riot_service.searchPlayerInfo(name)
            playerinfo["revisionDate"] = str(datetime.datetime.fromtimestamp(int(playerinfo["revisionDate"])/1000.0))
            return playerinfo
                
        return jsonify('')
    
    @riot_app.route('/championlist', methods=["POST"])
    def championlist():
        print("championList")
        if request.method == 'POST':
            riot_service = RiotService()
            if riot_service.countSummaryChampions() == 0:
                riot_service.createSummaryChampions()
                riot_service.createChampioninfoData()
            result = riot_service.getSummaryChampions()
            return jsonify(result)

        e = jsonify({'erroring':"noting loaded..."})
        return e

    @riot_app.route('/championinfo', methods=["GET"])
    def championinfo():
        print("enter championinfo")
        if request.method == 'GET':
            id = request.args.get('championinfo')
            print("championinfo GET")
            riot_service = RiotService()
            result = riot_service.getChampioninfoData(id)
            return jsonify(result)
        return e

    @riot_app.route('/friendlist')
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

    @riot_app.route('/itemlist', methods=["GET"])
    def itemlist():
        #if request.method == 'GET':
        riot_service = RiotService()

        # if riot_service.checkSummaryChampions() == 0:
        #     print("요약에 챔피언 넣습니다.")
        #     riot_service.createSummaryChampions()

        # riot_service.insert_loading_image_by_champion_skin_id("Zoe", "Zoe_19")
        binary_image = riot_service.get_loading_image_by_champion_skin_id("Zoe_19")['img']
        payload= base64.b64encode(binary_image).decode('utf-8')
        return jsonify({"raw":payload})
