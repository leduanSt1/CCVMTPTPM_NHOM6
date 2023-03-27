from flask import Flask
from flask_login import LoginManager

from app.config import Config
from app.extensions import db
from app.model.user import User


def createApp():

  app = Flask(__name__)

  # Using login manager
  loginManager = LoginManager()
  loginManager.init_app(app=app)
  loginManager.login_view = 'authen.index'
  @loginManager.user_loader
  def loadUser(id):
      return User.query.get(int(id))

  # Config app
  defaultConfig = Config()
  app.config.from_object(defaultConfig)
  
  # Initialize Flask extensions here if code block using testcases
  if app.config['SQLALCHEMY_DATABASE_URI'] is None:
    # Do not change code below => If you change, can not merge code
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ubuntu:1@localhost:5432/apiDashboard"
  db.init_app(app)

  return app
