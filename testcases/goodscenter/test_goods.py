import allure

from api.goods_api import get_banner


@allure.feature("用户中心模块")
class TestGoods:

    @allure.story("首页展示内容")
    @allure.title("banner测试title")
    def test_banner(self, banner_num):
        '''
        测试banner数据
        :param banner_num:这里用框架@pytest.fixture()引入banner_num方法，不用变量去存储
        :return:
        '''
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num
