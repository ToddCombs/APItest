import yaml
from icecream import ic

f = open("../config/data.yaml", encoding="utf-8")
data = yaml.safe_load(f)

ic(data['human'])
ic(data['human_dict'])
ic(data['human_name'])
ic(data['human_ability'])
ic(data['human_ability_list'])