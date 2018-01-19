import uuid
import datetime
from database import Database

__author__="Huidan Xiao"

class Post(object):

    def __init__(self,blog_id,title,content,author,date=datetime.datetime.utcnow(),id=None):
        """
        :param blog_id: whose blog this post belongs to. AMY,JOE,etc
        :param title: post's title
        :param content: post's title
        :param author: post's author
        :param id: identifier of this post, in case 2 post has same title
        """
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author
        self.createdDate=date
        self.id=uuid.uuid4().hex if id is None else id

        # post=Post(blog_id="123",title="love is a splendid thing",content="just love",author="XHD")


    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return{
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'title':self.title,
            'content':self.content,
            'createdDate':self.createdDate

        }

    @staticmethod
    def from_postid(id):
        return Database.find_one(collection="posts", query={"id": id})

    @staticmethod
    def from_blogid(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]







