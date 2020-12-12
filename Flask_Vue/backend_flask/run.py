from app import app 
from flask_cors import CORS, cross_origin
if __name__ == "__main__":
    CORS(app, resources={r'*': {'origins': '*'}})
    app.run(host='0.0.0.0', debug=True)