# pytest框架调用data.yaml
import pytest
from icecream import ic

from utils.read_data import get_data
from utils.yaml_util import func_yaml


@pytest.mark.parametrize("data", get_data["person"])    # person需要用数组方式调用
def test_person(data):
    '''
    :return:
    '''
    # data = get_data["person"]
    ic(func_yaml(data))
