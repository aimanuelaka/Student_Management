
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models import Student, Note, Subject
from app.forms import StudentForm
from app.utils import admin_required
from app import db

bp = Blueprint("student", __name__, url_prefix="/students")

@bp.route("/")
@login_required
@admin_required
def list_students():
    students = Student.query.all()
    return render_template("students/list.html", students=students)

@bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("student.list_students"))
    return render_template("students/create.html", form=form)

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        db.session.commit()
        return redirect(url_for("student.list_students"))
    return render_template("students/edit.html", form=form, student=student)
