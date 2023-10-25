import requests


def test_login():
    '''
    登录获取并返回token
    :return:token
    '''
    url = "http://pgateway-admin.intra.sit.etcp.net/platform/login?userName=admin&password=123456"
    res = requests.get(url)
    token = res.json().get('data')['token']
    username = res.json().get('data')['userName']
    return token, username


def test_get_userinfo():
    '''
    获取用户信息
    :return:
    '''
    token = test_login()
    headers = {
        "token": token
    }
    assert headers['token'] == token


# if __name__ == '__main__':
#     pytest.main()
