import requests


def get_type(response):
    data = response.json()
    type_list = []
    for i in data:
        type = i['type']
        type_list.append(type)
    return type_list


if __name__ == "__main__":
    URL = 'https://official-joke-api.appspot.com/jokes/ten'
    response = requests.get(URL)
    if response.status_code == 200:
        print(response.status_code)
        print("Запрос успешный")
        print(get_type(response=response))
    else:
        print(response.status_code)
        print('Что-то пошло не так')