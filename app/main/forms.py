
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,SubmitField,TextAreaField,DateField,TimeField
from wtforms.validators import Required

class ProblemForm(FlaskForm):
    title = StringField("Student Name", validators=[Required()])
    admission_number=StringField("Student Admission Number",validators=[Required()])
    category = SelectField("What is your issue related to", choices=[('Adminstration','Adminstration'),('Academic','Academic'),('Student Affairs','Student Affairs'),('Health', 'Health'),('Counselling', 'Counselling'), ('Hostel', 'Hostel'), ('Finance', 'Finance')], validators=[Required()])
    ProblemComment=TextAreaField("Describe ypur issue here", validators=[Required()])
    submit =SubmitField("Submit Your Issue")
    
class CommentForm(FlaskForm):
    name= StringField("Name", validators=[Required()])
    description= TextAreaField('Your Comment on the issue', validators=[Required()])
    department=SelectField("Reply from", choices=[('Adminstration','Adminstration'),('Academic','Academic'),('Student Affairs','Student Affairs'),('Health', 'Health'),('Counselling', 'Counselling'), ('Hostel', 'Hostel'), ('Finance', 'Finance')], validators=[Required()])
    submit= SubmitField('Comment')
