from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy_utils import database_exists


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SECRET_KEY"] = "0c1b2eedbcb0812cf6ad75783d751099"
app.config["UPLOAD_FOLDER"]="static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from Lions import routes