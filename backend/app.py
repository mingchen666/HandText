# 导入Flask
from flask import jsonify

from app import create_app

app=create_app()


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Too Many Requests",
        "message": "You have exceeded the allowed number of requests. Please try again later.",
        "details": str(e.description)
    }), 429

if __name__ == '__main__':
    # 启动服务器
    app.run(debug=True)
    # run() 参数
    # debug=True 默认值，自动检测代码的修改，并重新加载服务器
    # port=5000 默认值，端口号
    # host='0.0.0.0' 默认值，监听所有ip地址
