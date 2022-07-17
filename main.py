import requests
from bs4 import BeautifulSoup

url = 'https://www.banki.ru/products/currency/cash/kaliningrad/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, features='html.parser')

table = soup.findAll('span', {'class': 'font-bold'})

print()
print(soup.title.text)
print()

print(f'USD: {table[0].text}')
print(f'EURO: {table[1].text}')
# print(soup.title)
#
#
# msgs = soup.select('a')
# print(msgs)