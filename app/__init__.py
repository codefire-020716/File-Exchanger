import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.secret_key = '8e2d49ae00ac038adf51e309776f609132e11cc7'
application.config.from_object('config')

if not os.path.exists(application.config.get('STORE_PATH')):
    os.mkdir(application.config.get('STORE_PATH'))

db = SQLAlchemy(application)

import views