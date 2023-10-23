import requests
from icecream import ic
# import pytest
# res_github = requests.get("https://api.github.com/events")
# 创建一个会话机制
# req = requests.Session()

# headers 里加入键值'Cookie':'token=xxxxxxx'  用以绕开登录
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
params = {
    "type": "moive",
    "tag": "热门",
    "page_limit": 10,
    "page_start": 0
}
# req保存了cookie或者session
res_douban = requests.get("https://movie.douban.com/j/search_subjects", params=params, headers=headers)
# ic(res_douban.status_code)
# ic(res_douban.text)

def test_mobile():
    r = requests.get("http://api.binstd.com/shouji/query", params={"shouji": "13371115555", "appkey": "9508bd66e49ce0e1"})

    ic(r.status_code)
    ic(r.json())
    assert r.status_code == 200

    res = r.json()
    assert res['status'] == '103'
    assert res['msg'] == 'APPKEY无请求此数据权限'
    assert res['result'] is not None

