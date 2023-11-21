import allure

from api.user_api import send_code
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("注册登录")
    @allure.title("注册手机号用例")
    def test_register(self):
        json_data = base_data.read_data()['test_register']
        result = send_code(json_data)
        assert result.success is True