from flask import jsonify, request, url_for
from app import app
from .models import Feed
from .models import FeedSchema
import time

result = []


@app.route("/api/feed")
def get_feed_list():
    feed_list = Feed.query.order_by(Feed.scraping_time).all()
    feed_schema = FeedSchema(many=True)
    # print(feed_list)
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


@app.route('/api/feed/<int:feed_id>', methods=['PUT'])
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


@app.route('/api/feed/<int:feed_id>', methods=['DELETE'])
def delete_feed(feed_id):
    delete = Feed.query.filter_by(id=feed_id).first()
    db.session.delete(delete)
    db.session.commit()
    return jsonify({'message': '删除成功！'}), 200
