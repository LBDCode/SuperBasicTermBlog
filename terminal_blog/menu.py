from database import Database
from models.blogs import Blog



class Menu(object):

    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog["id"])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog (author=sef.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        command = input("Do you want to READ (R) or WRITE(W)? ")
        if command == "R":
            self._list_blogs()
            self._view_blog()
        elif command == "W":
            self.user_blog.new_post()
        else:
            print("Thanks for blogging!")

    def _list_blogs(self):
        blogs = Database.find("blogs", query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you want to view: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['date'], post['title'], post['content']))


