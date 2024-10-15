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
    if request.method == "POST":
        data = request.get_json()
        new_user = User(username=data["username"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()

        return make_response(new_user.to_dict(), 201)
    

@app.route("/users/<int:id>", methods=["GET", "PATCH"])
def user_detail(id):
    user = User.query.get(id)
    if not user:
        return make_response({"error": "User not found"}, 404)
    
    if request.method == "GET":
        return make_response(user.to_dict(), 200)

    if request.method == "PATCH":
        data = request.get_json()
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        db.session.commit()
        return make_response(user.to_dict(), 200)



@app.route("/posts", methods= ["GET", "POST"])
def posts():
    if request.method == "GET":
        posts = Post.query.all()
        response = [post.to_dict() for post in posts]

        return make_response(response, 200)
    if request.method == "POST":
        data = request.get_json()
        new_post = Post(title=data["title"], content=data["content"])
        db.session.add(new_post)
        db.session.commit()

        return make_response(new_post.to_dict(), 201)


@app.route("/posts/<int:id>", methods=["GET", "PATCH"])
def post_detail(id):
    post = Post.query.get(id)
    if not post:
        return make_response({"error": "Post not found"}, 404)

    if request.method == "GET":
        return make_response(post.to_dict(), 200)

    if request.method == "PATCH":
        data = request.get_json()
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        db.session.commit()
        return make_response(post.to_dict(), 200)

        

if __name__ == '__main__':
    app.run(port=5555, debug=True)