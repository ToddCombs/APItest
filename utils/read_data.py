import yaml
import os
import requests
from icecream import ic

# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml"))


path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")


def read_data():
    f = open(path, encoding="utf-8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
params = {
    "type": "moive",
    "tag": "热门",
    "page_limit": 10,
    "page_start": 0
}
# req保存了cookie或者session
# res_douban = requests.get("https://movie.douban.com/j/search_subjects", params=params, headers=headers)
#
#
# ic(res_douban.status_code)
# ic(res_douban.text)