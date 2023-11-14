# 优化mobile_query的response
import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    '''
    优化工具
    :param response:
    :return:
    '''
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        # 封装body
        ResultResponse.body = response.json()
        logger.info('接口的返回内容>>>>' + json.dumps(response.json(), ensure_ascii=False))
    else:
        ResultResponse.success = False
        logger.info('接口状态码不是2开头，请检查body' + json.dumps(response.json(), ensure_ascii=False))

    return ResultResponse