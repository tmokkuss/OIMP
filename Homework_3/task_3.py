import requests
from collections import Counter


def get_auth(data):
    values = data['entries']
    auth_list = []
    for i in values:
        auth_list.append(i['Auth'])
    return auth_list


def count_auth(auth_list):
    auth_list = auth_list
    count_auth_types = Counter(auth_list)
    return count_auth_types


def get_ratio_auth(count_auth_types, data):
    count_auth_types = count_auth_types
    count = data['count']
    auth_ratio = []
    for key, value in count_auth_types.items():
        if key == '':
            ratio = value / count
            auth_ratio.append(f'Without Auth: {"{:.4f}".format(ratio)}')
        else:
            ratio = value / count
            auth_ratio.append(f'{key}: {"{:.4f}".format(ratio)}')
    return auth_ratio


def get_github_apis(data):
    values = data['entries']
    count = 0
    for value in values:
        if value['Link'].startswith('https://github.com/'):
            count += 1
    return count


def get_categories_and_auth(data):
    values = data['entries']
    categories_list = []
    for value in values:
        categories_list.append(value['Category'])
    categories = Counter(categories_list)
    return dict(categories)


if __name__ == "__main__":
    URL = "https://api.publicapis.org/entries"
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        auth_list = get_auth(data=data)
        count_auth_types = count_auth(auth_list=auth_list)
        print("________________")
        print('Процентное соотношение разных видов Auth аутентификации к общему числу публичных API: ')
        ratio_auth = get_ratio_auth(count_auth_types=count_auth_types, data=data)
        print(ratio_auth)
        print("________________")
        print("Количество публичных API развернутых на github: ")
        github_apis = get_github_apis(data=data)
        print(github_apis)
        print("________________")
        print("Количество публичных API в определенных категориях: ")
        categories = get_categories_and_auth(data=data)
        print(categories)
    else:
        print(f'Что-то пошло не так, код ошибки: {response.status_code}')