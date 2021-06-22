from werkzeug.security import genarate_password_hash,check_password_hash
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
     
