
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from app.forms import LoginForm
from app.models import User
from app import db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/")
def index():
    return redirect(url_for("auth.login"))

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print("user:", user)
            print("check_password:", user.check_password(form.password.data) if user else None)
            return redirect(url_for("admin.dashboard"))
        flash("Invalid credentials")
    return render_template("login.html", form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
