
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


##WTForm
class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField("Submit Post")
