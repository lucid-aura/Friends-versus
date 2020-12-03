import flask
from flask import jsonify
from app import app
#from ..logging.logging import log_time

@app.route('/', methods=["GET", "OPTIONS"])
def home():
    
    test = [
        {
            'name' : 'test',
            'value' : 'test'
        }
    ]
    #my_res = flask.Response(jsonify(test[0]))
    #my_res.headers["Access-Control-Allow-Origin"] = "*"

    return jsonify(test[0])

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