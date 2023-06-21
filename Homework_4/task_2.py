import requests
from bs4 import BeautifulSoup


def scrape_catalog(url, params=None):
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    product_elements = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for product_element in product_elements:
        name = product_element.find('h4', class_='card-title').text.strip()
        price = product_element.find('h5').text.strip()
        products.append({'name': name, 'price': price})

    next_page = soup.find('a', class_='next page-link')
    if next_page:
        next_page_url = next_page['href']
        params = {'page': int(next_page_url.split('=')[-1])} if params else {'page': 2}
        products += scrape_catalog(url, params=params)

    return products


if __name__ == '__main__':
    url = 'https://scrapingclub.com/exercise/list_basic/'
    catalog = scrape_catalog(url)

    for product in catalog:
        print(f"Наименование товара: {product['name']}, Цена: {product['price']}")
