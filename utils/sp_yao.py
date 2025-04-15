import requests
from icecream import ic
from bs4 import BeautifulSoup

search_words = "药"

search_url = "https://www.nmpa.gov.cn/datasearch/"

headers = {
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
params = {
    "keyword": search_words
}

response = requests.get(search_url, headers=headers, params=params)

if response.status_code != 200:
    ic(f"请求失败：{response.status_code}")
    exit()

soup_url = BeautifulSoup(response.text, "html.parser")

res = soup_url.find_all('div', class_='result-item')

for res_detail in res:
    detail_url = res_detail.find('a')['href']

    if not detail_url.startswith('http'):
        detail_url = f'https://www.nmpa.gov.cn{detail_url}'
    ic(f"正在访问详情页：{detail_url}")

    detail_res = requests.get(detail_url, headers=headers)

    if detail_res.status_code == 200:
        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')

        tit = detail_soup.find('h1').text if detail_soup.find('h1') else "无标题"

        content = detail_soup.find('div', class_='content')
        if content:
            content_text = content.get_text(separator='\n').strip()
        else:
            content_text = "无内容"

        ic(f"标题：{title}")
        ic(f"内容：{content_text}")
        ic("-" * 50)
    else:
        ic(f"无法获取详情页数据，状态码：{detail_res.status_code}")
