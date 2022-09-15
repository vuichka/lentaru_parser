from datetime import date, datetime
from bs4 import BeautifulSoup 
import requests as r
import re


URL = 'https://lenta.ru/parts/news/'
PAGES = 5 # number of pages to parse


res = []

for i in range(PAGES):
    page = r.get(URL + str(i))  
    soup = BeautifulSoup(page.content, features="html.parser")
    news = soup.find_all('a', class_=['parts_news', 'card-full-news'])
    for k in news:
        dt = re.findall(r'\d{2}-\d{2}-\d{4}|\d{4}/\d{2}/\d{2}', k.get('href'))
        if '-' in dt[0]:
            dt = datetime.strptime(dt[0] + 'T' + k.div.time.text, r'%d-%m-%YT%H:%M').strftime("%Y-%m-%dT%H:%M:%S")
        else:
            dt = datetime.strptime(dt[0] + 'T' + k.div.time.text, r'%Y/%m/%dT%H:%M').strftime("%Y-%m-%dT%H:%M:%S")
        res.append({ 'title': k.h3.text, 'time': dt })

for i in res:
    print(i)