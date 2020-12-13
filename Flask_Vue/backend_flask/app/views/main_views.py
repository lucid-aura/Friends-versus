from flask import (
    Blueprint,
    render_template
)

class MainView:
    main_app = Blueprint('main_app', __name__, url_prefix='/')
    @main_app.route('/') 
    def index():
        return render_template('index.html')