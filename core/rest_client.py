import requests

from utils.read import base_data

api_root_url = base_data.read_ini()['host']['api_sit_url']


class RestClient:

    def __init__(self):
        self.api_root_url = api_root_url

    def get(self, url, **kwargs):
        '''
        发起get请求
        :param url:
        :param params:
        :param kwargs: 入参的params会进入这个参数。所以不传params也可以
        :return:返回请求
        '''
        return requests.get(self.api_root_url + url, **kwargs)

    def post(self, url, **kwargs):
        '''
        发起post请求
        :param url:
        :param kwargs:
        :return:
        '''
        return requests.post(self.api_root_url + url, **kwargs)
