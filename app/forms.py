from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired
from wtforms import  TextAreaField

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(message='A description is required')])
    upload = FileField('',validators=[FileRequired('File required for upload'),FileAllowed(['jpg', 'png'], 'Images only!')])
    
