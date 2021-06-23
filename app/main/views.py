from .forms import ProblemForm
from flask import render_template, url_for, request, abort, flash, 
from . import main
from ..models import Problem
from flask_login import login_required, current_user
from ..import db

@main.route('/', methods=['GEt','POST'])
def index():