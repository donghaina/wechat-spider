from flask import Flask
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from . import models
from . import api
from . import views

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jsglue = JSGlue()
# 让JS文件中可以使用url_for方法
jsglue.init_app(app)