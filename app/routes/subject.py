
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models import Subject
from app.forms import SubjectForm
from app.utils import admin_required
from app import db

bp = Blueprint("subject", __name__, url_prefix="/subjects")

@bp.route("/")
@login_required
@admin_required
def list_subjects():
    subjects = Subject.query.all()
    return render_template("subjects/list.html", subjects=subjects)

@bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_subject():
    form = SubjectForm()
    if form.validate_on_submit():
        subject = Subject(name=form.name.data)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for("subject.list_subjects"))
    return render_template("subjects/create.html", form=form)

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_subject(id):
    subject = Subject.query.get_or_404(id)
    form = SubjectForm(obj=subject)
    if form.validate_on_submit():
        subject.name = form.name.data
        db.session.commit()
        return redirect(url_for("subject.list_subjects"))
    return render_template("subjects/edit.html", form=form, subject=subject)
