# 向表内写入数据
import mysql.connector

connection = mysql.connector.connect(

)

cursor = connection.cursor()

table_name = "etci_order_main"
columns = ['order_code', 'first_channel_code', 'second_channel_code', 'user_id', 'third_user_id', 'phone',
           'order_status',
           'order_amount', 'actual_pay_amount', 'amount_refunded', 'refund_status', 'product_type', 'product_code',
           'source', 'delete_flag', 'remark']

for i in range(1, 10001):
    values = f"('order00aaaa{i}', 'CJ_YT_AHYT', 'gx_ywx_tyb', '7','23555438', '13718415257','1000', '29.90','29.90', " \
             f"'0.00','3000','2','107203477297799','3{i}','0','test')"
    insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES {values};"
    cursor.execute(insert_sql)

connection.commit()
connection.close()
