class Feed:
    __tablename__ = 'feed'
    id = self.db.Column(db.Integer, primary_key=True)
    wx_id = self.db.Column(db.String(50), unique=True)
    wx_title = self.db.Column(db.String(100), unique=True)
    scraping_time = self.db.Column(db.Integer)

    def __init__(self, db):
        self.db = db
    # scraping_time = db.Column(db.String(100))

    def __repr__(self):
        return '<Feed %r>' % self.wx_id


class FeedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'wx_id', 'wx_title', 'scraping_time')
        model = Feed
