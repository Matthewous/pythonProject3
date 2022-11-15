import requests
import bs4
from fake_headers import Headers
from pprint import pprint

HUBS = ['Программирование *', 'python']

header = Headers(os="mac", headers=True).generate()

base_url = "https://habr.com"

url= base_url + "/ru/all/"

response = requests.get(url, headers=header)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if hub in HUBS:
            title = article.find('h2').find('span').text
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            pprint(f'Название: {title}, ссылка: {link}')