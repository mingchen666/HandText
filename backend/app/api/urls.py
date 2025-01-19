# 路由管理
from flask_restful import Api

from .fonts import FontsResource
from .text2write import WriteResource
from .iamge import ImageResource
from .upload import FileUploadResource
from .textfile import TextResource
from .write2text import Write2Text


# 初始化路由
def initialize_routes(api: Api):
    api.add_resource(WriteResource, '/api/generate_handwriting')
    api.add_resource(ImageResource,'/api/imagefileprocess')
    api.add_resource(FontsResource, '/api/fonts','/api/fonts_info')
    api.add_resource(TextResource, '/api/textfileprocess')
    api.add_resource(FileUploadResource, '/upload')
    api.add_resource(Write2Text,'/api/write/to/text')