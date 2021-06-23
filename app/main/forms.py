from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, StringField,SubmitField,TextAreaField,DateField
from wtforms.validators import Required

class ProblemForm(FlaskForm):
  
    category = SelectField("What is your issue related to", choices=[('Adminstration','Adminstration'),('Academic','Academic'),('Student Affairs','Student Affairs'),('Health', 'Health'),('Counselling', 'Counselling'), ('Hostel', 'Hostel'), ('Finance', 'Finance')], validators=[Required()])
    title = StringField("Student Name", validators=[Required()])
    submit =SubmitField("Submit Your Issue")
    