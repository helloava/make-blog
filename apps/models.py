"""
models.py

"""

from apps import db

# each Model and each database are connected. 1:1
class Article(db.Model):
    #db.Model is already defined by module.
    id = db.Column(db.Integer, primary_key=True)
    #db.Column, id is received as Column and its format is Integer
    #db.Column can make setting of table column
    title = db.Column(db.String(255))
    # String is limited to  255 alphabets
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    #article_id is class Article's id. ,
    #small article is not class but var'article' in class Comment. 
    # bring it from below

    article = db.relationship(
        'Article', backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
    #setting relationship between Models(in this case, between article and comment)
    # if we want to access comment's Model's data, use 'article.comments'
    #cascade is like falls from Article class, when delete Article, its comments will be deleted

    author = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    content = db.Column(db.Text())
    #contents of comment
    date_created = db.Column(db.DateTime(), default=db.func.now())
