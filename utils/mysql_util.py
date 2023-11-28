# 连接数据库

import pymysql

from utils.log_util import logger
from utils.read import base_data

data = base_data.read_ini()['mysql']

DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWORD'],
    "db": data['MYSQL_DB']
}


class MysqlDb:

    def __init__(self):
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)  # **代表参数，autocommit代表变更后主动提交update
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        '''
        用完记得关闭连接和游标释放资源
        :return:
        '''
        self.cur.close()
        self.conn.close()

    def select_db_one(self, sql):
        logger.info(f'执行sql:{sql}')
        # 执行查询
        self.cur.execute(sql)
        # 返回一条数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果:{result}')
        return result

    def select_db_all(self, sql):
        logger.info(f'执行sql:{sql}')
        self.cur.execute(sql)
        # 返回所有数据
        result = self.cur.fetchall()
        logger.info(f'sql执行结果:{result}')
        return result


    def execute_db(self, sql):
        '''
        执行update时可能报错需要try
        :param sql:
        :return:
        '''
        try:
            logger.info(f'执行sql:{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))

db = MysqlDb()

if __name__ == "__main__":
    db = MysqlDb()
    result = db.select_db_one("SELECT `code` FROM users_verifycode WHERE mobile = '17311111111' ORDER BY `id` DESC LIMIT 1;")
    print(result['code'])