import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../config")
from config import FlaskConfig
from flask import Flask 

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # utf-8 제대로 표현
app.config.from_object(FlaskConfig)

from . import routes 