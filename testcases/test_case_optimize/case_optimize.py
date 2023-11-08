import pytest
import requests
from icecream import ic

from api.api import mobile_query
from utils.read import base_data  # 引入FileRead类实例

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    param = base_data.read_data()["mobile_belong"]  # 不通过parametrize调用字典
    result = mobile_query(param)
    assert result['status'] == '103'
    assert result['msg'] == 'APPKEY无请求此数据权限'
    assert result['result'] is not None


@pytest.mark.parametrize("mobile, appkey", base_data.read_data()["mobile_belong_post"])
def test_mobile_post(mobile, appkey):
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
def test_mobile_get(mobile, appkey):
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
