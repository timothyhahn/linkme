from . import db
from sqlalchemy import Column, Integer, Text, ForeignKey

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    link = Column(Text, unique=False)
    score = Column(Integer, unique=False)
    comments = db.relationship('Comment', backref='post')

    def __init__(self, title, link):
        self.score = 0
        self.title = title
        self.link = link


class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    content = Column(Text, unique=False)
    score = Column(Integer, unique=False)

    def __init__(self, post_id, content):
        self.score = 0
        self.post_id = post_id
        self.content = content
