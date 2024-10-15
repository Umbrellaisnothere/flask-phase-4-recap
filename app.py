from flask import Flask
from flask_migrate import Migrate
from models import db, User, Post, Group, user_groups
from flask_sqlalchemy import SQLAlchemy
from flask import make_response, request
from flask import jsonify

# Flask is a lightweight Python web framework for building web applications
# Flask is a micro-framework, which means it does not include a lot of features
# Flask is designed to be simple and easy to get started with

# Database = "sqlite:///recap.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recap.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    return "<h1>Welcome to Flask</h1>"

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":    
        users = User.query.all()
        response = [user.to_dict() for user in users]
        return make_response(response, 200)
    elif request.method == "POST":


# @app.route("/posts", method = ["GET", "POST"])
# def posts():
#     if request.method == "GET":
#         posts = Post.query.all()
#         response = [post.to_dict() for post in posts]
#         return make_response(response, 200)
#     elif request.method == "POST":

@app.route("/posts/<int:id>", methods=["GET", "POST"])
def posts(id):
    if request.method == "GET":
        post = Post.query.all()
        response = [post.to_dict() for post in posts]
        return make_response(response, 200)
    elif request.method == "POST":

        

if __name__ == '__main__':
    app.run(port=5555, debug=True)