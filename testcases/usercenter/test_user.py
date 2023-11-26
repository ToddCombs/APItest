import allure
import pytest

from api.user_api import send_code, register, login
from testcases.conftest import get_data
from testcases.usercenter.conftest import get_code, delete_user, delete_code
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("注册登录")
    @allure.title("注册手机号用例")
    def test_register(self):
        '''
        注册验证
        :return:
        '''
        json_data = base_data.read_data()['test_register']
        # 删除验证码
        delete_code(json_data['mobile'])
        # 发送验证码
        result = send_code(json_data)
        assert result.success is True
        # 获取短信验证码
        mobile = result.body['mobile']
        code = get_code(mobile)
        # 注册
        register_result = register(code, mobile)
        assert register_result.success is True
        # 删除用户
        delete_user(mobile)


    @pytest.mark.parametrize('username,password', get_data()['user_login'])
    @allure.story("用户登录")
    @allure.title("手机号登录用例")
    def test_login(self, username, password):
        '''
        登录验证
        :return:
        '''
        print(username, password)
        result = login(username, password)
        assert result.success is True
        assert result.body['token'] is not None
        assert len(result.body['token']) != 0

