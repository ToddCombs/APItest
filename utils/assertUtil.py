import jsonpath


class AssertUtil:

    def contains(self, check_value, except_value):
        assert except_value in check_value, f'{except_value} in {check_value}'

    def extract_by_jsonpath(self, extract_value: dict, extract_expression: str):
        """
        根据jsonpath获取值，判断返回是否存在，并取值
        :param extract_value: res.json()
        :param extract_expression: $.token
        :return:
        """
        extract_value = jsonpath.jsonpath(extract_value, extract_expression)
        if not extract_value:
            return
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value


    def validate_response(self, response, validate_check):
        """
        校验传入结果
        :param response:
        :param validate_check:
        :return:
        """
        for check in validate_check:
            for check_type, check_value in check.items():
                # 实际结果
                actual_value = self.extract_by_jsonpath(response, check_value[0])
                # 预期结果
                except_value = check_value[1]
                if check_type in ['contains', 'con']:
                    self.contains(actual_value, except_value)


