import requests

def get_categories():
    url_categories=('https://api.escuelajs.co/api/v1/categories')
    r=requests.get(url_categories)
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories=r.json()
    for category in categories:
        print(category['name'])
