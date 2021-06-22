from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Problem(db.Model):
    '''
    problem class that define the problem objects 
    '''
    __tablename__ = 'problem'

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    title=db.Column(db.String(255))
    Category=db.Column(db.String(255))
    problemComment=db.Column(db.String())
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)


    @classmethod
    def get_problems(cls,id):
        problems=Problem.query.order_by(problem_id=id).desc().all() 
        return problems

    def __repr__(self):
        return f'Problem {self.description}'


class ProblemComments(db.Model):
    '''
    model that defines properties of problemcomment objects
    '''
    __tablename__="comments"
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String())
    date_posted=db.Column(db.DateTime,default=datetime.utcnow) 
    problem_id=db.Column(db.Integer,db.ForeignKey("problem.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))

class User(UserMixin,db.Model):
    '''
    models that defines properties of user class
    '''
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(),unique = True,index = True) 
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    problems=db.relationship('Problem', backref ='problem',lazy= "dynamic")
    problemcomments=db.relationship('ProblemComments',backref ='broplemcomments',lazy= "dynamic")


    @property
    def password(self):
        raise AttributeError('You can not access  the password attribute')

    @password.setter
    def  password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return f'User {self.username}'