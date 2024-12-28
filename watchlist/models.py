from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Document,UserMixin): # 表名将会是 user（自动生成，小写处理）    
    name = db.StringField(required=True)
    username = db.StringField(required=True)  # 用户名
    password_hash = db.StringField(required=True)  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(
            password
        )  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值


class Movie(db.Document):  # 表名将会是 movie    
    title = db.StringField(required=True)  # 电影标题
    year = db.StringField(required=True,max_length=4)  # 电影年份