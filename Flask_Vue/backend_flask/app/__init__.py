from config import Config
from flask import Flask 

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # utf-8 제대로 표현
app.config.from_object(Config)

from . import routes 