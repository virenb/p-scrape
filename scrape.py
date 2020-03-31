import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://books.toscrape.com/index.html')

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all(class_='product_pod')

with open('books.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Book', 'Price']
  csv_writer.writerow(headers)

  for book in books:
    h3 = book.find('h3')
    title = h3.find('a').get('title')
    price = book.find(class_='price_color').get_text().replace('Â', '')
    csv_writer.writerow([title, price])


