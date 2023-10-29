# conftest.py名称为框架固定不可修改，作用为控制多个文件调用一次
# conftest.py文件方法无需导入，函数作用于当前文件夹及下级文件夹
# Terminal命令行执行pytest testcase/test_fixture -s   -s是执行时打印case中的内容
import pytest
from icecream import ic


@pytest.fixture(scope="session", autouse=False)  # 这里需要定义autouse=True否则需要在每个testcase文件中加入，会很麻烦
def test_session():
    ic("我是session级的fixture")


@pytest.fixture(scope="function", autouse=False)
def test_func1():
    ic("我是function1级的fixture")


@pytest.fixture(scope="function", autouse=False)
def test_func2():
    ic("我是function2级的fixture")


@pytest.fixture(scope="function", autouse=False)
def get_params():
    """
    pytest内的return的用法
    :return:
    """
    params = {"shouji": "13371115555", "appkey": "9508bd66e49ce0e1"}
    return params


@pytest.fixture(scope="function", autouse=False)
def func():
    '''
    前置后置步骤可以写在一个函数里，用yield分割
    return返回所有结果，程序中止不再运行
    yield则返回一个可迭代的生成器对象，用for循环或next()方法遍历生成器提取结果
    :return:
    '''
    ic("我是前置步骤")
    yield
    ic("我是后置步骤")
