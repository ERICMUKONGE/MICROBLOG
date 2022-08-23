from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from .models import User, Post

@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'User': User, 'Post': Post}

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

from app import routes, models
