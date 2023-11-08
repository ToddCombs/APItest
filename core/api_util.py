from core.rest_client import get


def get_mobile_belong(**kwargs):
    '''
    获取多个url并组装成请求
    :param params:
    :param kwargs:
    :return:返回请求
    '''
    return get('/shouji/query', **kwargs)