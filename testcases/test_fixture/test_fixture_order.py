# pytest的fixture的执行顺序

import pytest
from icecream import ic


@pytest.fixture(scope='session')
def t_session():
    ic("session级fixture")


@pytest.fixture(scope="module")
def t_module():
    ic("module级fixture")


@pytest.fixture(scope="class")
def t_class():
    ic("class级fixture")


@pytest.fixture(scope="function")
def t_function():
    ic("function级fixture")


class TestOrder:
    def test_order(self, t_module, t_function, t_class, t_session):
        """
        传参顺序不影响执行顺序，依然按照session->module->class->function顺序执行
        :param t_module:
        :param t_function:
        :param t_class:
        :param t_session:
        :return:
        """
        assert 1 == 1