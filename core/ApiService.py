from core.rest_client_new import RestClient
from utils.assertUtil import AssertUtil


class ApiService:

    def __init__(self):
        self.session = RestClient()

    def handle_case(self, test_data):
        """
        获取url,method,headers,case_info,validate
        :param test_data:
        :return:
        """
        url = test_data['request_info']['url']
        method = test_data['request_info']['method']
        headers = test_data['request_info']['headers']
        case_info = test_data['case_info']
        validate = case_info.pop('validate', None)
        res = self.session.do_request(url=url, method=method, headers=headers, **case_info)
        # 断言判断逻辑
        AssertUtil().validate_response(res, validate)

        return res
