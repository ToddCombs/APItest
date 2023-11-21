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


# 单参数参数值为字典
@pytest.mark.parametrize("student_name", [{"name": "todd", "sex": "male"}, {"name": "combs", "sex": "male"}, {"name": "jason", "sex": "female"}, {"name": "bourne", "sex": "female"}])
def test_paramstrize_04(student_name):
    ic(student_name["name"])
    ic(student_name["sex"])  # 需要保持字典key值个数大于调用的次数。如果多字典key值不一样，执行时会报错
