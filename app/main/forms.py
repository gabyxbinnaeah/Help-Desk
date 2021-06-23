from re import sub
from wtforms.widgets.core import TextArea
from app.models import ProblemComments
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, StringField,SubmitField,TextAreaField,DateField
from wtforms.validators import Required

class ProblemForm(FlaskForm):
    title = StringField("Student Name", validators=[Required()])
    category = SelectField("What is your issue related to", choices=[('Adminstration','Adminstration'),('Academic','Academic'),('Student Affairs','Student Affairs'),('Health', 'Health'),('Counselling', 'Counselling'), ('Hostel', 'Hostel'), ('Finance', 'Finance')], validators=[Required()])
    ProblemComment=TextAreaField("Describe ypur issue here", validators=[Required()])
    submit =SubmitField("Submit Your Issue")
    
class CommentForm(FlaskForm):
    name= StringField("Name", validators=[Required()])
    description= TextAreaField('Your Comment on the issue', validators=[Required()])
    submit= SubmitField('Comment')
