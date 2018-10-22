from . import app


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
