from bs4 import BeautifulSoup
import requests


def get_total_pages():
    i = 1
    while True:
        url_site = f'https://quotes.toscrape.com/page/{i}/'
        response = requests.get(url_site)
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.find('li', class_='next') is not None:
            i += 1
        else:
            break
    return i


if __name__ == '__main__':
    print(get_total_pages())
