from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
# db = SQLAlchemy(app)


@app.route("/")
def home():
    return "Hello SDA students!"


@app.route("/explore")
def explore():
    return "Hello explore!"


@app.route("/notifications")
def notifications():
    return "Hello notifications!"


@app.route("/messages")
def messages():
    return "Hello messages!"


if __name__ == "__main__":
    app.run(
        debug=True,
    )
