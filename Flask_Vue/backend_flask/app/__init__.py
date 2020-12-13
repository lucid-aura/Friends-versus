import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../config")
from config import FlaskConfig
from flask import Flask 
from .views import main_views
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(import_name=__name__,
                template_folder='templates')
    
    app.config['JSON_AS_ASCII'] = False # utf-8 제대로 표현    
    app.config.from_object(FlaskConfig)

    CORS(app, resources={r'*': {'origins': '*'}})

    app.register_blueprint(main_views.bp)

    return app 

# from . import routes 


