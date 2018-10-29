#!/usr/local/bin/python3
from app import app

if __name__ == '__main__':
    # app.debug = True
    # 删除旧的表
    # db.drop_all()
    # db.create_all()
    app.run()
