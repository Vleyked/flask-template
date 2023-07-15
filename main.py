from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class User(db.Model):
    """
    id: db columns -> db.Integer, primary key
    name: db columns -> db.String, unique
    """


@app.before_request_funcs
def create_tables():
    db.create_all()


@app.route("/")
def home():
    """Functionalities for the users

    1. Add a new user
        functions to use
            User
            db.session.add
            db.session.commit
    2. Get all users
            User.query.all
            produce the output -> create a output variable to return
    """
    return render_template("home.html")


if __name__ == "__main__":
    app.run(
        debug=True,
    )
