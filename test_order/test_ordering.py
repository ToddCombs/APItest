import pytest
from icecream import ic

@pytest.mark.run(order=1)
def test_login():
    ic('login...')


def test_pay():
    ic('pay...')

@pytest.mark.run(order=2)
def test_search():
    ic('search...')

@pytest.mark.run(order=3)
def test_order():
    ic('order...')