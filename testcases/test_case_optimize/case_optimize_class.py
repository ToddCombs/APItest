import allure
import pytest
import requests
from icecream import ic

from api.api import mobile_query
from utils.read import base_data  # 引入FileRead类实例

url = base_data.read_ini()['host']['api_sit_url']


@allure.epic("数据进制项目epic")
@allure.feature("手机号模块feature")
class TestMobile:
    @allure.story("查询手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.bing.com", name="缺陷地址issue（很少用）")
    @allure.description("当前手机号是：13371115555归属地是北京的description，经常用")
    @allure.step("手机号归属地的step，基本用不到")
    @allure.severity(severity_level="blocker")  # 用例的优先级
    def test_mobile(self):
        param = base_data.read_data()["mobile_belong"]  # 不通过parametrize调用字典
        result = mobile_query(param)
        assert result.success is True
        assert result.body['status'] == '103'
        assert result.body['msg'] == 'APPKEY无请求此数据权限'
        assert result.body['result'] is not None

    @allure.story("查询手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.bing.com", name="缺陷地址issue（很少用）")
    @allure.description("当前手机号是：13371115555归属地是北京的description，经常用")
    @allure.step("手机号归属地的step，基本用不到")
    @allure.severity(severity_level="blocker")  # 用例的优先级
    def test_mobile2(self):
        param = base_data.read_data()["mobile_belong"]  # 不通过parametrize调用字典
        result = mobile_query(param)
        assert result.success is True
        assert result.body['status'] == '103'
        assert result.body['msg'] == 'APPKEY无请求此数据权限'
        assert result.body['result'] is not None

    @allure.story("查询手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.bing.com", name="缺陷地址issue（很少用）")
    @allure.description("当前手机号是：13371115555归属地是北京的description，经常用")
    @allure.step("手机号归属地的step，基本用不到")
    @allure.severity(severity_level="blocker")  # 用例的优先级
    def test_mobile3(self):
        param = base_data.read_data()["mobile_belong"]  # 不通过parametrize调用字典
        result = mobile_query(param)
        assert result.success is True
        assert result.body['status'] == '203'
        assert result.body['msg'] == 'APPKEY无请求此数据权限'
        assert result.body['result'] is not None

    @pytest.mark.parametrize("mobile, appkey", base_data.read_data()["mobile_belong_post"])
    def test_mobile_post(self, mobile, appkey):
        ic("测试手机号归属地post请求mobile")
        r = requests.post(url + "/shouji/query",
                          params={"shouji": mobile, "appkey": appkey})

        ic(r.status_code)
        ic(r.json())
        res = r.json()
        assert res['status'] == '103'
        assert res['msg'] == 'APPKEY无请求此数据权限'
        assert res['result'] is not None

    @pytest.mark.parametrize("mobile, appkey", base_data.read_data()["mobile_belong_get"])
    def test_mobile_get(self, mobile, appkey):
        ic("测试手机号归属地get请求mobile")
        r = requests.get(url + "/shouji/query",
                         params={"shouji": mobile, "appkey": appkey})

        ic(r.status_code)
        ic(r.json())
        res = r.json()
        assert res['status'] == '103'
        assert res['msg'] == 'APPKEY无请求此数据权限'
        assert res['result'] is not None


if __name__ == '__main__':
    pytest.main()
