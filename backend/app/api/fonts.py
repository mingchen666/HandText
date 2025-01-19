from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest

from .response import ApiResponse
from ..utils.file import get_fonts_list
from ..utils.log import global_logger

# 创建一个请求解析器
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True,location='args',
                    help='Title is required and must be a string')


class FontsResource(Resource):
    # 获取字体列表
    def get(self):
        try:
            # 解析请求体中的参数
            # args = parser.parse_args()
            # title = args['title']
            try:
                filenames = get_fonts_list(directory='app/public/fonts')
                # logger.info(f"filenames: {filenames}")
                if filenames == []:
                    return ApiResponse.error('字体文件未找到！')
            except Exception as e:
                print(e)
                return ApiResponse.error('系统发送错误,请稍后再试',500)
            # return {
            #     "code": 200,
            #     "message": "success",
            #     "data": filenames
            # }
            return jsonify(filenames)
            # return ApiResponse.success(filenames)
        except BadRequest as e:
            print(e.data)
            global_logger.info("搞什么飞机")
            error_message = e.data.get('message', 'Bad Request')
            # 返回自定义响应
            return ApiResponse.error(error_message, 400)
            # return ApiResponse.error('系统发送错误,请稍后再试',500)
        except Exception as e:
            # 捕获并处理异常
            global_logger.error(f"An error occurred: {str(e)}")
            return {'message': 'Internal Server Error', 'error': str(e)}, 500