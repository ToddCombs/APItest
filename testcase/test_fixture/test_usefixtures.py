import pytest
from icecream import ic

@pytest.mark.usefixtures("use_fixture1", "use_fixture2")  # 无参数，无法接传参
def test_usefixtures():
    ic('usefixture')