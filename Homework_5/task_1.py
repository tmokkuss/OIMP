import requests
from bs4 import BeautifulSoup


def scrape_emoji_categories():
    url = 'https://emojipedia.org/search/'
    list_of_categories = ["nature", "music", "science"]
    emoji_counts = {}

    for category in list_of_categories:
        params = {'q': category}
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find('ol', class_='search-results')
        items = elements.find_all('a')
        emoji_list = []
        count = 0
        for item in items:
            emoji_list.append((item.text)[:2])
            count += 1
        emoji_counts[category] = count
        print(f"Категория {category} имеет {count} эмоджи.")
        print(f"Список эмоджи категории {category} : ", emoji_list)

    return emoji_counts


if __name__ == '__main__':
    scrape_emoji_categories()
