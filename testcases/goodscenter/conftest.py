import pytest

from utils.mysql_util import db


@pytest.fixture()
def banner_num():
    sql = "SELECT COUNT(id) AS banner_number FROM goods_banner;"
    result = db.select_db_one(sql)
    return result['banner_number']