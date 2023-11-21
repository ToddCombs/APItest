#  注册接口json_data

from core.api_util import api_util
from utils.response_util import process_response


def send_code(json_data):
    '''
    获取短信验证码
    :param json_data:
    :return:
    '''
    response = api_util.get_code(json=json_data)
    # 引入response处理工具并返回
    return process_response(response)