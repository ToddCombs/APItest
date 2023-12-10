import os

import pytest

from api.user_api import login
from utils.read import base_data

def get_data():
    """
    简化获取数据函数
    :return:
    """
    return base_data.read_data()


@pytest.fixture
def login_fixture():
    """
    简化登录接口
    :return:
    """
    if 'token' not in os.environ:
        data = get_data()['login_fixture']
        mobile = data['mobile']
        password = data['password']
        result = login(mobile, password)
        os.environ['token'] = result.body['token']
        os.environ['mobile'] = str(mobile)
        return result.body['token'], mobile
    else:
        return os.environ['token'], os.environ['mobile']


@pytest.fixture(scope="session")
def login_token():
    """
    简化登录接口
    :return:
    """
    data = get_data()['login_fixture']
    mobile = data['mobile']
    password = data['password']
    result = login(mobile, password)
    headers = {
        "Authorization": "JWT " + result.body["token"]
    }
    return headers, mobile