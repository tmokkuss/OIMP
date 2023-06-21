import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    page = 1
    quotes = []

    while True:
        url = f'https://quotes.toscrape.com/page/{page}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quote_elements = soup.find_all('div', class_='quote')
        for quote_element in quote_elements:
            text = quote_element.find('span', class_='text').text.strip()
            author = quote_element.find('small', class_='author').text.strip()
            quotes.append(f'{text} - (c) {author}')

        next_button = soup.find('li', class_='next')
        if not next_button:
            break

        page += 1

    return quotes, page


def print_quotes(quotes):
    for index, quote in enumerate(quotes):
        print(f'{index+1}. {quote}')


if __name__ == '__main__':
    quotes, num_pages = scrape_quotes()
    print_quotes(quotes)
    print(f'На сайте {num_pages} страниц и {len(quotes)} цитат')
