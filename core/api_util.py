from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()  # 继承自父类RestClient

    def get_mobile_belong(self, **kwargs):
        '''
        获取多个url并组装成请求
        :param params:
        :param kwargs:
        :return:返回请求
        '''
        return self.get('/shouji/query', **kwargs)

    def post_data(self, **kwargs):
        '''
        发送post请求
        :param kwargs:
        :return:
        '''
        return self.post('/posts', **kwargs)

    def get_code(self, **kwargs):
        '''
        项目实战调用
        :return:
        '''
        return self.post('/code/', **kwargs)


api_util = Api()  # 初始化类
