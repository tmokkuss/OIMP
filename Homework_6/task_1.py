import random
import requests
import csv
import pandas as pd


def write_data(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_ids(data_length):
    ids = [str(random.randint(0, 99999)) for _ in range(data_length)]
    return ids


def generate_salary(data_length):
    salaries = [str(random.randint(100000, 999999)) for _ in range(data_length)]
    return salaries


def generate_month(data_length):
    months = [str(random.randint(1, 12)) for _ in range(data_length)]
    return months


def generate_users(data_length):
    url = "https://randomuser.me/api/"
    params = {'results': data_length}
    response = requests.get(url, params=params)
    data = response.json()
    users = [f"{user['name']['title']}. {user['name']['first']} {user['name']['last']}" for user in data['results']]
    return users


def generate_data(data_length):
    titles = ['id', 'salary', 'month', 'name']
    ids = generate_ids(data_length)
    salaries = generate_salary(data_length)
    months = generate_month(data_length)
    users = generate_users(data_length)
    data = list(zip(ids, salaries, months, users))
    return [titles] + data


if __name__ == '__main__':
    data_length = 15
    data = generate_data(data_length)
    write_data('data.csv', data)

    df = pd.read_csv('data.csv')

    print('Средняя зарплата:', df['salary'].mean())