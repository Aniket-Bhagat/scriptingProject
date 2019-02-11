from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#connect to database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
app.secret_key='MrCX0y9DUFC5fwz8zDtBUg0kNGMkarij'

app.config['POSTS_PER_PAGE'] = 3

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#tables -- in models.py

#app module
from app import views