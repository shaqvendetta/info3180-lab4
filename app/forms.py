
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    photo = FileField('Upload a Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
