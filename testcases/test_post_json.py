import requests
from icecream import ic

json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.post(url=url, json=json_data)
ic(r.status_code)
ic(r.json())