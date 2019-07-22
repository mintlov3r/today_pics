import requests


def first_test():
    url = 'https://www.toutiao.com/search_content'
    params = {
                'offset': offset,
                'format': 'json',
                'keyword': '电影',
                'autoload': 'true',
                'count': '20',
                'cur_tab': '3',
                'from': 'gallery'}

    for i in range(10):
        offset = i
        resp = requests.get(url, params=params)
        print(resp.text)
