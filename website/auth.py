from crypt import methods
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/sign-in", methods=["GET"])
def sign_in():
    return render_template("sign_in.html")

@auth.route("/sign-in", methods=["POST"])
def sign_in_post():
    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("username")
    remember = True if request.form.get("remember") else False
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again")
        return redirect(url_for("auth.sign_in"))
    login_user(user, remember=remember)
    return redirect(url_for("views.home", user=current_user))


@auth.route("/sign-up", methods=["GET"])
def sign_up():
    return render_template("sign_up.html")

@auth.route("/sign-up", methods=["POST"])
def sign_up_post():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    username = request.form.get("username")
    if password1 is None:
        return sign_in_post()
    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email Address already exists")
        return redirect(url_for("auth.sign_in"))
    
    new_user = User(email=email, username=username, password=generate_password_hash(password1, method="sha256"))
    
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.sign_in"))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.sign_in"))