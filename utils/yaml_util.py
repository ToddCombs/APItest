# 在yaml文件使用自定义函数，主要用faker库生成随机数据

import random
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
                # 强转类型，否则字符串和int型相加会报错
                data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end+1:len(str(value))]
    return data


def random_name():
    '''
    随机名字
    :return:
    '''
    return fk.name()

def random_number():
    '''
    随机年龄
    :return:
    '''
    return random.randint(1, 100)

def random_sex():
    '''
    随机性别
    :return:
    '''
    return random.choice(['男', '女'])

if __name__ == '__main__':
    # 这里需要对参数化字符串进行处理
    data = {'name': '北京-${random_name()}-测开', 'age': '${random_number()}', 'sex': '${random_sex()}'}
    ic(func_yaml(data))
