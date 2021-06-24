from .forms import ProblemForm, CommentForm
from flask import render_template, url_for, request, abort, flash, redirect
from . import main
from ..models import Problem, ProblemComments,User,Admin
from flask_login import login_required, current_user
from ..import db


@main.route('/',methods = ['GET'])
def index():
   
    return render_template ('index.html')


@main.route('/student', methods=['GET','POST'])
def student():
    problems = Problem.get_problems()
    title = 'student issues'

    return render_template('student.html', title = title, problems = problems)

@main.route('/new_problem/new', methods=['GET','POST'])
def new_post():
    problem_form = ProblemForm()
    if problem_form.validate_on_submit():
        title = problem_form.title.data
        admission_number=problem_form.admission_number.data
        category = problem_form.category.data
        problemComment= problem_form.ProblemComment.data
        new_problem = Problem( title=title, category=category, problemComment=problemComment, admission_number=admission_number)
        

        db.session.add(new_problem)
        db.session.commit()

        return redirect(url_for('main.student'))

    return render_template('problem.html', problem_form = problem_form)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
def new_Comment(id):
    comment_form = CommentForm()
    problem =Problem.query.filter_by(id=id).all()
    descriptions = ProblemComments.query.filter_by(problem_id=id).all()
    if comment_form.validate_on_submit():
        description=comment_form.description.data
        name= comment_form.name.data
        department=comment_form.department.data
        
        new_comment=ProblemComments(description = description,name=name,department=department, problem_id=id)
        

        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html', comment_form=comment_form, descriptions=descriptions, problem=problem)

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def deleteComment(id):
    comment =ProblemComments.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect (url_for('main.new_Comment', id=id)) 


@main.route('/update/<int:id>', methods=['GET', 'POST'])

def updateProblem(id):
    problem = Problem.query.get_or_404(id)
    form = ProblemForm()
    if form.validate_on_submit():
        problem.title = form.title.data
        problem.admission_number= form.admission_number.data
        problem.problemComment=form.ProblemComment.data
        problem.category=form.category.data
        db.session.add(problem)
        db.session.commit()
        return redirect(url_for('main.student'))
    elif request.method == 'GET':
        form.title.data = problem.title
        form.ProblemComment.data =problem.problemComment
        form.admission_number.data=problem.admission_number
        form.category.data=problem.category
    return render_template('update_problem.html', form=form)

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def deleteProblem(id):
    problem =Problem.query.get_or_404(id)
    db.session.delete(problem)
    db.session.commit()
    flash('comment succesfully deleted')
    return redirect (url_for('main.index'))
