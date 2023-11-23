# 连接数据库

import pymysql

from utils.log_util import logger
from utils.read import base_data

data = base_data.read_ini()['mysql']

DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "username": data['MYSQL_USER'],
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

    def select_db(self, sql):
        logger.info(f'执行sql:{sql}')
        # 执行查询
        self.cur.execute(sql)
        # 拿所有获取的数据
        return self.cur.fetchall()

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


if __name__ == "__main__":
    db = MysqlDb()
    db.select_db()