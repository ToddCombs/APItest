import requests


class TestUser:
    '''
    pytest框架中类不能定义__init__函数，运行会报错
    '''
    token_1 = ''
    username_1 = ''

    def test_login(self):
        '''
        登录获取并返回token
        :return:token
        '''
        url = "http://pgateway-admin.intra.sit.etcp.net/platform/login?userName=admin&password=123456"
        res = requests.get(url)
        token = res.json().get('data')['token']
        username = res.json().get('data')['userName']
        return token, username
        # TestUser.token_1 = token  # 类中引用参数，函数可以不return
        # TestUser.username_1 = username

    def test_get_userinfo(self):
        '''
        获取用户信息
        :return:
        '''
        token, username = self.test_login()
        headers = {
            "token": token
        }
        assert headers['token'] == token
        assert username == 'admin'

# if __name__ == '__main__':
#     pytest.main()
