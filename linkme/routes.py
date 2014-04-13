from . import app, db
from models import Post, Comment
from flask.ext.restless import APIManager

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Post, methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=None)
api_manager.create_api(Comment, methods=['GET', 'POST', 'DELETE', 'PUT'], results_per_page=None)

@app.route('/')
def index():
    return app.send_static_file('index.html')
