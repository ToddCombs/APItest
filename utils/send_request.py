import json

import time
import datetime


import requests
from utils.log_util import logger
from icecream import ic

def sort_by_key(params):
    """
    a-z排序入参字典
    :param params:
    :return:
    """
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    return sorted_params


def param_string(params):
    """
    除sign外的参数拼接符串
    :return:
    """
    param_string = "&".join([f"{key}={value}" for key, value in sort_by_key(params) if value])
    return param_string


def send_request(url, method, **kwargs):
    """
    发送测试请求
    :param url:/
    :param method:
    :param kwargs:
    :return:
    """


if __name__ == '__main__':

    hosts = "/"
    auth = ""
    url = hosts + auth
    method = "post"
    params = {
        "sign": "",
        "channelNo": "",
        "data": "data",
        "timestamp": int(round(time.time() * 1000))
    }


    ic(dict(sort_by_key(params)))
    ic(param_string(params))