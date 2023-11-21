import pytest
import requests
from icecream import ic
# 默认scope是function
# @pytest.fixture(scope="function", autouse=True)
# def func():
#     ic("前置步骤")

#
# def teardown_function():
#     ic("清理测试数据")


def test_assertNumber():  # 这里直接调用conftest.py中的test_func1
    assert 1 == 1


def test_mobile(get_params):
    shouji = get_params["shouji"]
    appkey = get_params["appkey"]
    ic("测试手机号归属地get请求mobile")
    r = requests.get("http://api.binstd.com/shouji/query",
                     params={"shouji": shouji, "appkey": appkey})

    ic(r.status_code)
    ic(r.json())
    assert r.status_code == 200

    res = r.json()
    assert res['status'] == '103'
    assert res['msg'] == 'APPKEY无请求此数据权限'
    assert res['result'] is not None


if __name__ == '__main__':
    pytest.main()