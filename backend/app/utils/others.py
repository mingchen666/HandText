# 捕获异常，记录日志并且返回500错误
import os

from flask import jsonify

# 异常处理
def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.info("An error occurred during the request: %s", e)
            return jsonify({"status": "error", "message": str(e)}), 500

    return decorated_function
