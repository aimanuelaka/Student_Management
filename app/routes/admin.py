
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Student, Subject, Note
from app.utils import admin_required

bp = Blueprint("admin", __name__,url_prefix="/admin")

@bp.route("/dashboard")
@login_required
@admin_required
def dashboard():
    return render_template("dashboard.html")

