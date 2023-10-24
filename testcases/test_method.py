import pytest
import requests
from icecream import ic


class TestMobile:

    def setup_method(self):
        ic("准备测试数据")

    def teardown_method(self):
        ic("清理测试数据")

    def test_assertNumber(self):
        expect = 1
        actual = 1
        assert expect == actual

    def test_mobile(self):
        ic("测试手机号归属地get请求mobile")
        r = requests.get("http://api.binstd.com/shouji/query",
                         params={"shouji": "13371115555", "appkey": "9508bd66e49ce0e1"})

        ic(r.status_code)
        ic(r.json())
        assert r.status_code == 200

        res = r.json()
        assert res['status'] == '103'
        assert res['msg'] == 'APPKEY无请求此数据权限'
        assert res['result'] is not None


if __name__ == '__main__':
    pytest.main()
