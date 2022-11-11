from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/s?k=laptop&crid=2XAXZO02VK979&sprefix=laptop%2Caps%2C275&ref=nb_sb_noss_2"
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
laptops = soup.find(
    'div', class_= 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
print(laptops)
laptop_brand = laptops.find(
    'span', class_ = 'a-size-mini a-spacing-none a-color-base s-line-clamp-2')
laptop_price = laptops.find('span', class_='a-price-whole')
price_before = laptops.find('span', class_='a-offscreen')
delivery_time = laptops.find('span', class_='a-color-base a-text-bold')
total_rating = laptops.find('span', class_='a-size-base s-underline-text')


print(f'''
Laptop: {laptop_brand.text}
Price: {laptop_price.text}
Price-Before: {price_before.text}
Delivery: {delivery_time}
Total Rating: {total_rating}
''')
