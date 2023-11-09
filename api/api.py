from core.api_util import api_util


def mobile_query(params):
    '''
    封装请求部分代码
    :param params:
    :return: 返回查询结果
    '''
    response = api_util.get_mobile_belong(params=params)
    return response.json()
