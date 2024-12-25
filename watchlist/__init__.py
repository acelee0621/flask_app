from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
app.app_context().push()
login_manager = LoginManager(app)  # 实例化扩展类

@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接受用户 ID 作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user # 返回用户对象

login_manager.login_view = 'login'

#模板的上下文处理函数，返回的字典中的键值对可以在所有模板中直接使用
@app.context_processor
def inject_user():  # 函数名可以随意修改
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于 return {'user': user}

from watchlist import views, errors, commands