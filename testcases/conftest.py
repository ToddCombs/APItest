import pytest

from api.user_api import login
from utils.read import base_data

def get_data():
    '''
    简化获取数据函数
    :return:
    '''
    return base_data.read_data()


@pytest.fixture
def login_fixture():
    '''
    简化登录接口
    :return:
    '''
    data = get_data()['login_fixture']
    mobile = data['mobile']
    password = data['password']
    result = login(mobile, password)
    return result.body['token'], mobile



