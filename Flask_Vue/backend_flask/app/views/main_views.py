from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

class MainView:
    main_app = Blueprint('main_app', __name__, url_prefix='/')
    @main_app.route('/', methods=["GET", "POST"]) 
    def index():
        if request.method == 'GET':
            #language = request.form['language']
            #framework = request.args.get('framework')
            #framework = request.form['framework']
            #print(language)
            #print(framework)
            
            name = request.args.get('playerinfo')
            
            if name is not None:
                return redirect('/riot/playerinfo?name=' + name)

        return render_template('index.html')
