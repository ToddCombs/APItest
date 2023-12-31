import json

import requests

from utils.log_util import logger
from utils.read import base_data

api_root_url = base_data.read_ini()['host']['api_sit_url']


class RestClient:

    def __init__(self):
        self.api_root_url = api_root_url
        self.session = requests.Session()

    def get(self, url, **kwargs):
        """
        发起get请求
        :param url:
        :param params:
        :param kwargs: 入参的params会进入这个参数。所以不传params也可以
        :return:返回请求
        """
        # return requests.get(self.api_root_url + url, **kwargs)
        return self.request(url, "GET", **kwargs)

    def post(self, url, **kwargs):
        """
        发起post请求
        :param url:
        :param kwargs:
        :return:
        """
        # return requests.post(self.api_root_url + url, **kwargs)
        return self.request(url, "POST", **kwargs)

    def put(self, url, **kwargs):
        """
        发put请求
        :param url:
        :param kwargs:
        :return:
        """
        return self.request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        """
        发delect请求
        :param url:
        :param kwargs:
        :return:
        """
        return self.request(url, 'DELETE', **kwargs)

    def request(self, url, method, **kwargs):
        """
        判断是get还是post请求
        :param url:
        :param method:
        :param kwargs:
        :return:
        """
        self.request_log(url, method, **kwargs)
        if method == "GET":
            return self.session.get(self.api_root_url + url, **kwargs)
        if method == "POST":
            return self.session.post(self.api_root_url + url, **kwargs)
        if method == "PUT":
            return self.session.put(self.api_root_url + url, **kwargs)
        if method == "DELETE":
            return self.session.delete(self.api_root_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        """
        判断请求是否有data，json或params，有则记录日志
        :param url:
        :param method:
        :param kwargs:
        :return:
        """

        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求地址>>>>{}".format(self.api_root_url + url))
        logger.info("接口请求方法>>>>{}".format(method))

        if data is not None:
            logger.info("接口请求的data参数>>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求入参>>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求params参数>>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
        if headers is not None:
            logger.info("接口请求headers>>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))
