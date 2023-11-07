import configparser
import os

import yaml

# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml"))


data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")


class FileRead:

    # 实例化参数，否则无法调用
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path


    def read_data(self):
        f = open(self.data_path, encoding="utf-8")
        data = yaml.safe_load(f)
        return data


    # 读取settings.ini配置文件，需要configparser库
    def read_ini(self):
        '''
        读取ini文件内容
        :return:
        '''
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf-8')
        return config

base_data = FileRead()  # 接收FileRead类


# get_ini = read_ini()

# print(read_ini()['host']['api_sit_url'])   # 优先通过数组层级拿到host
