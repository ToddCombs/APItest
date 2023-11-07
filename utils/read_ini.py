# 读取settings.ini配置文件，需要configparser库
import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")

def read_ini():
    '''
    读取ini文件内容
    :return:
    '''
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    return config

get_ini = read_ini()

# print(read_ini()['host']['api_sit_url'])   # 优先通过数组层级拿到host