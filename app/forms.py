
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Save')

class SubjectForm(FlaskForm):
    name = StringField('Subject Name', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Save')

class NoteForm(FlaskForm):
    student_id = SelectField('Student', coerce=int, validators=[DataRequired()])
    subject_id = SelectField('Subject', coerce=int, validators=[DataRequired()])
    value = FloatField('Note', validators=[DataRequired()])
    submit = SubmitField('Save')
