import requests

from utils.read import base_data

api_root_url = base_data.read_ini()['host']['api_sit_url']


def get(url, **kwargs):
    '''
    发起get请求
    :param url:
    :param params:
    :param kwargs: 入参的params会进入这个参数。所以不传params也可以
    :return:返回请求
    '''
    return requests.get(api_root_url + url, **kwargs)
