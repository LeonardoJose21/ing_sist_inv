import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__, static_folder='../../static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('TRACK_MODIFICATIONS')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)