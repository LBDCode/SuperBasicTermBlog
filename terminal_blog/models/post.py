import uuid
from database import Database
import datetime

class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), post_id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    def save_post(self):
        Database.insert(collection="posts",
                        data=self.post_info())

    def post_info(self):
        return {
            'post_id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find(collection='posts', query={'post_id': id})

        return cls(blog_id=post_data["blog_id"],
                   post_id=post_data["post_id"],
                   author=post_data["author"],
                   content=post_data["content"],
                   title=post_data["title"],
                   date=post_data["date"])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]