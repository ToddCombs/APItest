import allure
import pytest

from core.ApiService import ApiService
from utils.yamlutil import YamlUtil


@allure.feature("用户")
class TestUser:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("user_center.yaml", "user_login_new"))
    def test_user_new(self, data):
        response = ApiService().handle_case(data)
        assert response['token'] is  not None