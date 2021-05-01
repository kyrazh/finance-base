import requests
from bs4 import BeautifulSoup

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&rlz=1C1GCEA_enRU918RU918&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE&aqs=chrome.0.69i59j69i57j69i61l3.2632j0j7&sourceid=chrome&ie=UTF-8'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}


page = requests.get(DOLLAR_RUB, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
convert = soup.findAll("span", {'class': 'DFlfde', "class": "SwHCTb"})

curs = float(convert[0].text.replace(",", "."))

print(curs)