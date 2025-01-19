from flask import Flask, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api
from .api.urls import initialize_routes
# from .config import Config
from .extensions import init_exts

'''
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://example.com", "http://localhost:3000"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})
'''

def create_app():

    app = Flask(__name__)
    # app.config.from_object(Config)
    # db_url = 'mysql+pymysql://root:xiaoluo@localhost:3306/flaskdb'
    # 配置数据库链接路径url
    # app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    # 可选：禁用追踪修改，减少内存消耗
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_exts(app)


    # 初始化路由
    api = Api(app)
    initialize_routes(api)
    # 配置跨域
    CORS(app)
    # CORS(app, resources={r"/*": {"origins": "*"}})
    # 自定义 429 错误处理


    return app