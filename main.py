from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Exercise 1 16/07/2023 - Part I forms


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = ...


class RegistrationForm(FlaskForm):
    """Fields from wtforms

    validators:

        username: should be required
        password: SHould be required as well and you have to use the Equalto 'confirm'
        confirm: same as previous
        submit: another different field
    """

    username = ...
    password = ...
    confirm = ...
    submit = ...


class LoginForm(FlaskForm):
    """Fields from wtforms

    username: should be required
    password: SHould be required
    submit: another different field
    """

    username = ...
    password = ...
    sumbit = ...


# Exercise 1 16/07/2023 - Part II routes
@login_manager.user_loader
def load_user(user_id):
    """Return que query filtered by user id"""
    ...


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register route where the user can register a new username

    HINTS:
        RegistrationForm()
            validate_on_submit()

        Interact with the db User class

        return
            redirect if the registration is valid
        register
    """
    return "Register route"


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login route where the user can login

    HINTS:
        LoginForm()
            validate_on_submit()

        Interact with the db User class
            login_user()
        return
            redirect if the registration is valid
        login
    """
    return "Login route"


@app.route("/logout")
@login_required
def logout():
    """Lgout routem where the users logout

    HINTS:
        logout_user()
        redirect -> login
    """
    return "Logout route"


@app.route("/users")
@login_required
def users():
    """Users can check all the users from the db

    HINTS:
        interact with the User class
            query.all()
        return tenokate + object
    """
    return "users route"


if __name__ == "__main__":
    db.create_all()
    app.run(
        debug=True,
    )
