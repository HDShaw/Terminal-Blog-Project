import uuid
import datetime
from database import Database
from models.post import Post

__author__="Huidan Xiao"

class Blog(object):
    def __init__(self,author,title,description,id=None):
        self.author=author
        self.title=title
        self.description=description
        self.id=uuid.uuid4().hex if id is None else id

    def new_post(self):
        title=input("enter your post title:")
        content=input("enter your post content:")
        date=input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        post=Post(blog_id=self.id,
                  title=title,
                  content=content,
                  author=self.author,
                  date=datetime.datetime.strptime(date, "%d%m%Y")
                  )

        post.save_to_mongo()

    def get_posts(self):
        #return Database.find(collection="posts",query={"blog_id":self.id})
        return Post.from_blogid(self.id)

    def save_to_mongo(self):
         return Database.insert(collection="blogs",data=self.jason())

    def jason(self):
        return {
            "author":self.author,
            "title":self.title,
            "description":self.description,
            "id":self.id
        }

    @classmethod
    def get_from_mongo(cls,id):
        blog_data=Database.find_one(collection="blogs",query={"id":id})

        return cls(author=blog_data["author"],
                    title=blog_data["title"],
                    description=blog_data["description"],
                    id=blog_data["id"])






