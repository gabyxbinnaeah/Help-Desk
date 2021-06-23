from .forms import ProblemForm
from flask import render_template, url_for, request, abort, flash, redirect
from . import main
from ..models import Problem
from flask_login import login_required, current_user
from ..import db

@main.route('/', methods=['GEt','POST'])
def index():
    problems = Problem.get_problems()
    title = 'student issues'

    return render_template('index.html', title = title, problems = problems)

@main.route('/new_post/new', methods=['GET','POST'])
def new_post():
    problem_form = ProblemForm()
    if problem_form.validate_on_submit():
        title = problem_form.title.data
        desscription = problem_form.description.data
        user_id = current_user._get_current_object().id
        new_proble = Problem(user_id=user_id, title=title, desscription=desscription)
    

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('problem.html', problem_form = problem_form)