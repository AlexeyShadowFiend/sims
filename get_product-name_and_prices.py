import requests
from bs4 import BeautifulSoup
import lxml

url = "https://rozetka.com.ua/ua/avtomobilnie-invertori/c4639256/"
filepath = "product.txt"
agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
product_names = []
product_price = []
counter = 0

respons = requests.get(url, headers=agent)
soup = BeautifulSoup(respons.text, "lxml")

# Get all products
all_product = soup.find('ul', class_='catalog-grid ng-star-inserted')

# Get list of products
list_product = all_product.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')

# For each element in array of product list
for elem in list_product:
    # Get name of current product
    title_of_product = elem.find('span', class_='goods-tile__title',)
    price_of_product = elem.find('span', class_='goods-tile__price-value',)

    # Add name to array
    product_names.append(title_of_product.text)

    # Add price to array with replacing &nbsp; (utf-8: u"\u00A0") to white space
    product_price.append((price_of_product.text).replace(u"\u00A0", " "))

for i in range(len(product_names)):
    # print("Product:"+product_names[counter]+" - ["+product_price[counter]+"]")
    with open(filepath, 'a', encoding='UTF8') as f:
        f.write(f'{"Product:"+product_names[counter]+"- ["+product_price[counter]+"]"}\n')
    counter += 1
