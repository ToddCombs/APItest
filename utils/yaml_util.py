# 在yaml文件使用自定义函数，主要用faker库生成随机数据

from faker import Faker
from icecream import ic

fk = Faker(locale="zh-CN")


def func_yaml(data):
    '''
    处理随机参数的yaml
    isinstance函数用来判断数据类型，是否为字典，为True进入判断
    :param data:
    :return:
    '''
    if isinstance(data, dict):
        # 逐个取字典内的键值
        for key, value in data.items():
            # 判断${}字符串是否在字典值内，True则重新赋值
            if '${' and '}' in str(value):
                # if 'random_name()' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start+2:end]  # 索引从${random_name}字符串的第二个开始取值
                data[key] = eval(func_name)
    return data


def random_name():
    '''
    随机名字函数
    :return:
    '''
    return fk.name()


if __name__ == '__main__':
    ic(random_name())
    data = {'name': '${random_name()}', 'age': 27, 'sex': '男'}
    ic(func_yaml(data))
