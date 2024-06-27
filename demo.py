import requests
from bs4 import BeautifulSoup

url = "https://subslikescript.com/movie/Titanic-120338"
response = requests.get(url, verify=False)
content = response.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')
title = soup.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
    file.close()
