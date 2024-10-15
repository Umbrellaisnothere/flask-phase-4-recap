from flask import Flask
from flask_migrate import Migrate

# Flask is a lightweight Python web framework for building web applications
# Flask is a micro-framework, which means it does not include a lot of features
# Flask is designed to be simple and easy to get started with

Database = "sqlite:///recap.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = Database

migrate = Migrate(app)

@app.route("/")
def index():
    return "<h1>Welcome to Flask</h1>"


if __name__ == '__main__':
    app.run(port=5500, debug=True)