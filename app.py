# coding = utf-8
from flask import Flask, render_template, jsonify, request, url_for
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import time

app = Flask('__name__')
app.config['SECRET_KEY'] = 'tww'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/wechat_spider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
jsglue = JSGlue()
jsglue.init_app(app)  # 让JS文件中可以使用url_for方法
result = []
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    wx_id = db.Column(db.String(50), unique=True)
    wx_title = db.Column(db.String(100), unique=True)
    scraping_time = db.Column(db.Integer)

    # scraping_time = db.Column(db.String(100))

    def __repr__(self):
        return '<Feed %r>' % self.wx_id


class FeedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'wx_id', 'wx_title', 'scraping_time')
        model = Feed


@app.route("/")
def index():
    return render_template('add_feed.html')


@app.route("/api/feed")
def get_feed_list():
    # print(db.session.query.order_by(Feed.id).all())
    feed_list = Feed.query.order_by(Feed.scraping_time).all()
    feed_schema = FeedSchema(many=True)
    print(feed_list)
    return jsonify({
        'feed_list': feed_schema.dump(feed_list)
    })


@app.route("/api/feed", methods=['POST'])
def add_feed():
    data = request.json
    result.append(data)
    print(data['wx_id'])
    print(data['wx_title'])
    print(data['scraping_time'])
    # feed_data = Feed(wx_id=data['wx_id'],wx_title=data['wx_title'],scraping_time=data['scraping_time'])
    feed_data = Feed(wx_id=data['wx_id'], wx_title=data['wx_title'], scraping_time=time.time())
    print(feed_data)
    db.session.add_all([feed_data])
    db.session.commit()
    return jsonify({'msg': '添加公众号成功'}), 200


@app.route('/api/feed/<feed_id>', methods=['PUT'])
def update_feed(feed_id):
    print(feed_id)
    data = request.json
    wx_id = data.get('wx_id')
    wx_title = data.get('wx_title')
    scraping_time = data.get('scraping_time')
    # print(data)
    update = Feed.query.filter_by(id=feed_id).first()
    update.wx_id = wx_id
    update.wx_title = wx_title
    update.scraping_time = scraping_time

    db.session.commit()
    return jsonify({'message': '编辑成功！'}), 200


@app.route('/api/feed/<feed_id>', methods=['DELETE'])
def delete_feed(feed_id):
    # result.remove(feed_id)
    delete = Feed.query.filter_by(id=feed_id).first()
    db.session.delete(delete)
    db.session.commit()
    return jsonify({'message': '删除成功！'}), 200


if __name__ == '__main__':
    app.debug = True
    # 删除旧的表
    # db.drop_all()
    # db.create_all()
    app.run()
