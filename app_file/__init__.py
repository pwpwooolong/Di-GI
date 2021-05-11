from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(pjdir, 'data.sqlite')
app.config['SECRET_KEY'] = os.urandom(24)

bootstrape = Bootstrap(app)
db = SQLAlchemy(app)

from app_file import route