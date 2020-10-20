# run with pipenv run python3 filename
import requests
from bs4 import BeautifulSoup


r = requests.get("https://news.google.com/news/rss")

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

news_list = soup.findAll("item")


for news in news_list:
    print(news.title.text, '\n',
        news.link.text)