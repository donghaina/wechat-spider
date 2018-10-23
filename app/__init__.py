from flask import Flask
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tww'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/wechat_spider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

jsglue = JSGlue()
jsglue.init_app(app)  # 让JS文件中可以使用url_for方法
result = []
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import models
from app import views
from app import api
