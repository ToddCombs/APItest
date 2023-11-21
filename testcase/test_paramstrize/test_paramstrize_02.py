import pytest
from icecream import ic


# 多参数多次循环数组入参
@pytest.mark.parametrize("name, sex", [["todd", "male"], ["combs", "female"], ["bourne", "male"]])
def test_paramstrize_02(name, sex):
    ic(f"{name}的性别是{sex}")


# 多参数多次循环元组入参
@pytest.mark.parametrize("name, sex", [("todd", "male"), ("combs", "female"), ("bourne", "male")])
def test_paramstrize_03(name, sex):
    ic(f"{name}的性别是{sex}")