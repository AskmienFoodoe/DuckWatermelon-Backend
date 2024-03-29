import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.score import Score

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
CORS(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route("/")
def home():
    return "Hello World"

api.add_resource(Score, '/scores')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
