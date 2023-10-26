import pytest
import requests
from icecream import ic
# 默认scope是function,或class,或module,session(作用于所有py文件)区别是作用域不同
# autouse=True则运行fixture
@pytest.fixture(scope="class", autouse=True)
def func():
    ic("前置步骤")

class TestClassFixture:

    # def teardown_function():
    #     ic("清理测试数据")


    def test_assertNumber(self):
        assert 1 == 1


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