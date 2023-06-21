import requests
import numpy as np
from bs4 import BeautifulSoup


def load_countries(n):
    url = 'https://randomuser.me/api/'
    params = {'results': n}
    response = requests.get(url, params=params)
    data = response.json()['results']
    countires = [user['location']['country'] for user in data]
    return countires


def generate_product_id(n):
    return np.random.randint(low=1, high=25, size=n)


def generate_region_sales(n):
    return np.random.randint(low=100, high=500, size=n)


def generate_regions(n, country_names):
    regions = []
    unique_countries = list(set(country_names))
    for _ in range(n):
        if len(unique_countries) > 0:
            country = unique_countries.pop()
            regions.append(f"Region {country}")
        else:
            regions.append(f"Region {np.random.randint(1, 5)}")
    return regions


def extract_currency_codes():
    url = "https://www.exchangerate-api.com/docs/supported-currencies"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    currency_table = soup.find('table', class_='table-striped')
    if currency_table is None:
        return {}
    rows = currency_table.find_all('tr')[1:]
    country_currency_code = {}
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            code = cells[0].text.strip()
            country = cells[2].text.strip()
            country_currency_code[country] = code
    return country_currency_code


def get_exchange_rate(currency_code):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"
    response = requests.get(url)
    data = response.json()
    rates = data.get("rates")
    rub_value = rates.get("RUB")
    return rub_value


def convert_to_rub(data, currency_codes):
    converted_data = []
    for row in data:
        country = row[2]
        currency_code = currency_codes.get(country, "EUR")
        exchange_rate = get_exchange_rate(currency_code)
        sales = float(row[1])
        converted_sales = sales * exchange_rate
        converted_row = np.append(row, [currency_code, converted_sales])
        converted_data.append(converted_row)
    return converted_data


if __name__ == '__main__':
    n = 50
    country_names = load_countries(n)
    data = np.column_stack((generate_product_id(n), generate_region_sales(n), country_names))

    np.savetxt('data.txt', data, delimiter=',', fmt='%s')
    data = np.loadtxt('data.txt', delimiter=',', dtype=str)

    currency_codes = extract_currency_codes()
    converted_data = convert_to_rub(data, currency_codes)

    np.savetxt('converted_data.txt', converted_data, delimiter=',', fmt='%s')
