import pytest
from icecream import ic

# 单参数单次循环
@pytest.mark.parametrize("name", ["ToddCombs"])
def test_paramstrize(name):
    ic("这是" + name)

@pytest.mark.parametrize("key", ["list1", "list2", "list3"])
def test_paramstrize01(key):
    '''
    单参数多次循环：列表几个，执行几次test
    :param key:
    :return:
    '''
    assert key == "list3"
    ic("列表入参" + key)

