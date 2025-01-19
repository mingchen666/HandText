# exts.py 插件管理
# 扩展的第三方插件
# 1.导入第三方插件
from flask import jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 2.初始化
db = SQLAlchemy()  # ORM
migrate = Migrate()
# 配置 Flask-Limiter
limiter = Limiter(
    get_remote_address,  # 以ip地址作为流量控制条件
    default_limits=["200 per day", "50 per hour"] , # 默认限速策略,
# on_breach=lambda limit: make_response(jsonify(error="Too Many Requests", detail=f"Rate limit {limit.limit} exceeded"), 429)
)

# 3.和app绑定
def init_exts(app):
    # db.init_app(app=app)
    # migrate.init_app(app=app, db=db)
    limiter.init_app(app)
    # 自定义 429 错误处理
