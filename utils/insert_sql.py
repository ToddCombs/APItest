# 向表内写入数据
import mysql.connector

connection = mysql.connector.connect(
    host="mysql-qa-all.mysql.tcloud.etcp.cn",
    user="yeehaw_insurance_dev",
    password="mNtDH3Cmso7h96nE",
    database="yeehaw_insurance"
)

cursor = connection.cursor()

table_name = "etci_order_main"
columns = ['order_code', 'first_channel_code', 'second_channel_code', 'user_id', 'third_user_id', 'phone',
           'order_status',
           'order_amount', 'actual_pay_amount', 'amount_refunded', 'refund_status', 'product_type', 'product_code',
           'source', 'delete_flag', 'remark']

for i in range(1, 10001):
    values = f"('order0000{i}', 'CJ_YT_AHYT{i}', 'gx_ywx_tyb{i}', '7{i}','23555438{i}', '13718415257{i}','1000{i}', '29.90{i}','29.90{i}', '0.00{i}','3000{i}','2{i}','107203477297799{i}','3{i}','0{i}','test{i}')"
    insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES {values};"
    cursor.execute(insert_sql)

connection.commit()
connection.close()
