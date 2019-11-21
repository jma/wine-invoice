import os

from flask import Flask, render_template
from . import config
from .frontpage.views import blueprint as frontpage_blueprint

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    app.config.from_object(config)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        print('test config')
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # # a simple page that says hello
    # @app.route('/')
    # def index():
    #     return render_template('main/page.html')
    app.register_blueprint(frontpage_blueprint)

    return app