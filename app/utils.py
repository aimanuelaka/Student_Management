from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != "admin":
            flash("Accès réservé à l’administrateur.")
            return redirect(url_for("note.student_averages"))
        return f(*args, **kwargs)
    return decorated_function
