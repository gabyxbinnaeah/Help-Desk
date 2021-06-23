from flask import render_template,request,redirect,url_for,flash
from . import main
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
# from .forms import updateProfile
from ..models import User

@main.route('/',methods = ['GET'])
def index():
   
    return render_template ('index.html')

