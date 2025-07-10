
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models import Note, Student, Subject
from app.forms import NoteForm
from app.utils import admin_required
from app import db

bp = Blueprint("note", __name__, url_prefix="/notes")

@bp.route("/")
@login_required
@admin_required
def list_notes():
    notes = Note.query.all()
    return render_template("notes/list.html", notes=notes)

@bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_note():
    form = NoteForm()
    form.student_id.choices = [(s.id, s.name) for s in Student.query.all()]
    form.subject_id.choices = [(s.id, s.name) for s in Subject.query.all()]
    if form.validate_on_submit():
        note = Note(student_id=form.student_id.data, subject_id=form.subject_id.data, value=form.value.data)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("note.list_notes"))
    return render_template("notes/create.html", form=form)

@bp.route("/averages")
@login_required
def student_averages():
    students = Student.query.all()
    averages = []
    for student in students:
        subjects = Subject.query.all()
        student_data = {"name": student.name, "subjects": []}
        for subject in subjects:
            notes = [n.value for n in student.notes if n.subject_id == subject.id]
            if notes:
                moyenne = round(sum(notes) / len(notes), 2)
            else:
                moyenne = "N/A"
            student_data["subjects"].append({"subject": subject.name, "average": moyenne})
        averages.append(student_data)
    return render_template("notes/averages.html", averages=averages)
