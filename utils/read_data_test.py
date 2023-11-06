import yaml
from icecream import ic

f = open("../config/data.yaml", encoding="utf-8")
data = yaml.safe_load(f)
ic(data['test']['name'])
ic(data['test']['request']['url'])
ic(data['test']['request']['method'])
ic(data['test']['request']['headers'])
ic(data['test']['request']['json'])

ic(data['mobile_belong'])
ic(data['mobile_belong_post'])
ic(data['mobile_belong_get'])

# ic(data['human'])
# ic(data['human_dict'])
# ic(data['human_name'])
# ic(data['human_ability'])
# ic(data['human_ability_list'])

