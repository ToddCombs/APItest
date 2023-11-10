import pytest

from api.api import test_json
from utils.log_util import logger
from utils.read import base_data  # 引入FileRead类实例


def test_post():
    logger.info("开始执行test_post方法")
    json_data = base_data.read_data()["json_data"]  # 不通过parametrize调用字典
    result = test_json(json_data)
    assert result['id'] == 101
    logger.info("用例执行完毕")

if __name__ == '__main__':
    pytest.main()
