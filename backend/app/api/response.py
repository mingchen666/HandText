from flask import jsonify, make_response

class ApiResponse:
    @staticmethod
    def success(data, message="请求成功", status_code=200):
        response = {
            "code": status_code,
            "statue": 'success',
            "message": message,
            "data": data
        }
        return make_response(jsonify(response), status_code)

    @staticmethod
    def error(message='请求失败', status_code=404):
        response = {
            "code": status_code,
            "statue": 'fail',
            "message": message,
            # "data": None
        }
        return make_response(jsonify(response), status_code)

    @staticmethod
    def unauthorized(message='用户信息无效', status_code=401):
        response = {
            "code": status_code,
            "statue": 'fail',
            "message": message
        }
        return make_response(jsonify(response), status_code)

    @staticmethod
    def invalid(message='请求参数错误或无效', status_code=400):
        response = {
            "code": status_code,
            "statue": 'fail',
            "message": message
        }
        return make_response(jsonify(response), status_code)

    @staticmethod
    def notmethod(message='当前请求方法不被允许', status_code=405):
        response = {
            "code": status_code,
            "statue": 'fail',
            "message": message
        }
        return make_response(jsonify(response), status_code)
