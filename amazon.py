from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/s?k=laptop&crid=2XAXZO02VK979&sprefix=laptop%2Caps%2C275&ref=nb_sb_noss_2"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
results = soup.find_all('div', {'data-component-type': 's-search-result'})

i = 0
item = results[i]

def scrape():
    atag = item.h2.a
    name = atag.text
    link = 'https://www.amazon.in'+atag.get('href')
    price_parent = item.find('span','a-price')
    price = price_parent.find('span', 'a-offscreen').text
    price_before_parent = item.find('span', class_='a-price a-text-price')
    price_before = price_before_parent.find('span', class_='a-offscreen').text
    rating = item.i.text
    delivery_parent = item.find('div', class_ = "a-row s-align-children-center")
    delivery = delivery_parent.find('span',class_ = 'a-color-base puis-medium-weight-text').text

    result = (name, price, price_before, rating, delivery)
    print(result)

for item in results:
    scrape()
    i = i + 1




