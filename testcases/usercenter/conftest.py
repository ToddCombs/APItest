from utils.log_util import logger
from utils.mysql_util import db


def get_code(mobile):
    '''
    获取短信验证码
    :param mobile:
    :return:
    '''
    sql = "SELECT `code` FROM users_verifycode WHERE mobile = '%s' ORDER BY `id` DESC LIMIT 1" % mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['code']

def delete_user(mobile):
    '''
    删除用户
    :param mobile:
    :return:
    '''
    sql = "DELETE FROM users_userprofile WHERE mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')


def delete_code(mobile):
    '''
    删除短信code
    :param mobile:
    :return:
    '''
    sql = "DELETE FROM users_verifycode WHERE mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')


def user_id(mobile):
    '''
    查询user_id
    :param mobile:
    :return:
    '''
    sql = "SELECT id FROM users_userprofile WHERE mobile = '%s';" % mobile
    result = db.select_db_one(sql)
    return result['id']


def get_shop_cart_num(username, good_id):
    '''
    查询UID
    :param username:
    :param good_id:
    :return:
    '''
    id = user_id(username)
    sql = "SELECT nums FROM trade_shoppingcart WHERE user_id = %d AND goods_id = %d" % (id, good_id)
    result = db.select_db_one(sql)
    return result['nums']

