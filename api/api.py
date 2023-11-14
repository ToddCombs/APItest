

from core.api_util import api_util

from utils.response_util import process_response


def mobile_query(params):
    '''
    封装请求部分代码
    :param params:
    :return: 返回查询结果
    '''
    response = api_util.get_mobile_belong(params=params)
    result = process_response(response)
    # logger.info('接口的返回内容>>>>' + json.dumps(response.json(), ensure_ascii=False))
    return result


def test_json(json_data):
    '''
    测试json传参
    :param json_data:
    :return:
    '''
    response = api_util.post_data(json=json_data)
    return response.json()
