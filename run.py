from flask import Flask
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import app.models
import app.api
import app.view

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jsglue = JSGlue()
# 让JS文件中可以使用url_for方法
jsglue.init_app(app)


if __name__ == '__main__':
    app.debug = True
    # 删除旧的表
    # db.drop_all()
    # db.create_all()
    app.run()
