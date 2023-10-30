import pytest
from icecream import ic
@pytest.fixture(params=["data1", "data2"], ids=["case1", "case2"])  # ids为测试用例标识
def params_fixture(request):
    return request.param

def test_params(params_fixture):
    ic(params_fixture)  # 取到params入参并打印