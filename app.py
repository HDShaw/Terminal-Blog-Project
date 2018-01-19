from database import Database
from models.post import Post
from models.blog import Blog
__author__ = "Huidan Xiao"

Database.initialize()

#post=Post(blog_id="111",
          #title="when i was young",
          #content="i was just 18",
          #author="an interesting person",
          #)

#post.save_to_mongo()

#posts=Post.from_blogid('111')

#for post in posts:
    #print(post)

blog=Blog(author="huidan xiao",
          title="i love sjx",
          description="i am lying to myself")

blog.new_post()

blog.save_to_mongo()

from_database= Blog.get_from_mongo(blog.id)

print(blog.get_posts())


