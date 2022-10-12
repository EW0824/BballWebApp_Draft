# Package structure approach - will be imported from here when called project

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# For Security
app.config['SECRET_KEY'] = 'asgcgxedmondsdaghjkwang08asdght24sdkgho08sdjfh03'
# Database - relative path from the current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# A database instance  
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Telling login_manager where the login is located
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' # Aesthetics 

# To prevent circular imports
from project import routes