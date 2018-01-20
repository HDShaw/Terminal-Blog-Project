from database import Database
from models.blog import Blog

__author__="Huidan Xiao"

class Menu(object):
    def __init__(self):
       #Ask user for user name
       #check if they have already got an account
       #if not, prompt them to creat one
       self.user=input("enter your author name")
       self.user_blog=None
       if self._user_has_account():
           print("welcome back {}".format(self.user))
       else:
           self._prompt_user_for_account()

    def _user_has_account(self):
        blog=Database.find_one("blogs",{"author":self.user})
        if blog is not None:
            self.user_blog=blog
            return True
        else:
            return False

    def _promt_user_for_account(self):
        title=input("enter your title")
        description=input("enter your description")
        blog=Blog(author=self.user,
                  title=title,
                  description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        #user read or write blogs?
        #if read:
            #list blogs in database
            #allow user to read one
            #display posts
        #if write:
            #check if user has a blog
            #if they do, prompt to have a post
            #if not, prompt them to have a new blog

        read_or_write = input("do you want to read(R) or write(W) blogs?")
        if read_or_write=="R":
            pass
        elif read_or_write=="W":
            pass
        else:
            print("thank you for logging!")

        pass