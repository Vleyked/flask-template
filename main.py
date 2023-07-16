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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


@app.before_request
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
    # Add a new user
    new_user = User(name="Kadri Aldama")
    db.session.add(new_user)
    db.session.commit()

    # Get all users
    users = User.query.all()

    # Pass users to the template
    return render_template("home.html", users=users)


if __name__ == "__main__":
    app.run(
        debug=True,
    )
