from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.secret_key = '8e2d49ae00ac038adf51e309776f609132e11cc7'
application.config.from_object('config')

db = SQLAlchemy(application)

import views