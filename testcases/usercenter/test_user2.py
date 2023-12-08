import allure
import pytest

from api.user_api import send_code, register, login, add_shopping_cart
from testcases.conftest import get_data
from testcases.usercenter.conftest import get_code, delete_user, delete_code, get_shop_cart_num
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:

    @allure.story("注册登录")
    @allure.title("注册手机号用例")
    def test_shopping_cart2(self, login_fixture):
        '''
        加购物车用例
        :return:
        '''
        # result = login(username, password)
        # token = result.body['token']
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()['shopping_cart']
        result = add_shopping_cart(param, token)
        # 查询购物车数量
        num = get_shop_cart_num(username, param['goods'])
        assert result.success is True
        # assert result.body['num'] == num