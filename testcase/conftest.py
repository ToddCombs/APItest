# conftest.py名称为框架固定不可修改，作用为控制多个文件调用一次
# conftest.py文件方法无需导入，函数作用于当前文件夹及下级文件夹
# Terminal命令行执行pytest testcase/test_fixture -s   -s是执行时打印case中的内容
import pytest
from icecream import ic
from utils.log_util import logger

@pytest.fixture(scope="session", autouse=False)  # 这里需要定义autouse=True否则需要在每个testcase文件中加入，会很麻烦
def test_session():
    ic("我是session级的fixture")

@pytest.fixture(scope="function", autouse=False)  # autouse作用在每个引用方法上，不用方法调用也可以
def test_func1():
    ic("我是function1级的fixture")

@pytest.fixture(scope="function")
def test_func2():
    ic("我是function2级的fixture")

@pytest.fixture(scope="function", autouse=True)
def func():
    logger.info("开始执行测试用例。。。")
    yield
    logger.info("测试用例执行完毕！")