import requests


def get_value_and_currency(input_data):
    data = input_data.split()
    value, currency = data[0], data[1]
    return value, currency


def request(convert_currency):
    currency = convert_currency
    URL = f'https://open.er-api.com/v6/latest/{currency}'
    response = requests.get(URL)
    return response.json()


def find_price(data, local_currency, convert_currency):
    data = data
    local_currency = local_currency
    convert_currency = convert_currency
    rates = data['rates']
    price = rates[f'{local_currency}']
    return price


def convert(value, price, local_currency, convert_currency):
    value = float(value)
    price = price
    local_currency = local_currency
    convert_currency = convert_currency
    result = value / price
    return f'Ваши {value} {local_currency} это {"{:.2f}".format(result)} {convert_currency}'


if __name__ == "__main__":
    input_data = input("Введите число и валюту в виде 100 RUB, 1000 USD и т.д. : ")
    convert_currency = input("Введите в какую валюту хотите преоброзовать: ")
    value = get_value_and_currency(input_data=input_data)[0]
    local_currency = get_value_and_currency(input_data=input_data)[1]
    data_json = request(convert_currency=convert_currency)
    price = find_price(
        data=data_json,
        local_currency=local_currency,
        convert_currency=convert_currency)
    result = convert(
        value=value,
        price=price,
        local_currency=local_currency,
        convert_currency=convert_currency
    )
    print(result)