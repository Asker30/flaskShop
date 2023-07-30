from flask import Flask
from flask_sqlalchemy import SQLAlchemy

store = Flask(__name__)
store.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy()
db.init_app(store)
