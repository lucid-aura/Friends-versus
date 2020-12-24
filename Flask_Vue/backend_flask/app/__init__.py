import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/../../config")
from config import FlaskConfig
from flask import Flask 
from flask_jwt_extended import *
from .views import (
    main_views,
    user_views,
    riot_views
)
from flask_cors import (
    CORS, 
    cross_origin
)
from termcolor import colored

def create_app():
    app = Flask(import_name=__name__,
                template_folder='templates')
    
    app.config['JSON_AS_ASCII'] = False # utf-8 제대로 표현    
    app.config.from_object(FlaskConfig('Develop.json'))

    app.config['JWT_SECRET_KEY'] = 'friends-versus'
    jwt_manager = JWTManager()
    jwt_manager.init_app(app)



    # app.config.from_object(FlaskConfig('Test.json'))

    print(colored(app.config, 'green'))
    print(colored(app.config['DATABASE'], 'red'))
    print(colored(app.config['RIOTAPI'], 'blue'))
    print(colored(app.config['DATA'], 'yellow'))

    CORS(app, supports_credentials=True, resources={r'*': {'origins': '*'}})

    app.register_blueprint(main_views.MainView.main_app)
    app.register_blueprint(user_views.UserView.user_app)
    app.register_blueprint(riot_views.RiotView.riot_app)

    return app 

# from . import routes 


