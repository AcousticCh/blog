from http.client import NOT_EXTENDED
from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import db
import json
from .models import Pages

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/", methods=["POST"])
@login_required
def home_post():
    page = request.form.get("page")
    if len(page) < 1:
        flash("Page is empty")
    else:
        new_page = Pages(data=page, user_id=current_user.id)
        db.session.add(new_page)
        db.session.commit()
        print("Page added")
        flash("Page added")
    return render_template("home.html", user=current_user)

@views.route("/delete-page", methods=["POST"])
def delete_page():
    page = json.loads(request.data)
    pageId = page["pageId"]
    page = Pages.query.get(pageId)
    if page:
        if page.user_id == current_user.id:
            db.session.delete(page)
            db.session.commit()
    return jsonify({})
