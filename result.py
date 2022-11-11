from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/premier-league-table'

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
result = soup.find('table', {'class':'standing-table__table callfn'})

print(result)
