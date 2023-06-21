import requests
import datetime as datetime


def request_main(URL):
    response = requests.get(URL)
    print(response.status_code)
    return response.json()


def request(data):
    data = data
    for values in data:
        platform_name = values[1]
        URL = f'https://kontests.net/api/v1/{platform_name}'
        response = requests.get(URL)
        listts = response.json()
        for value in listts:
            try:
                time_first = value['start_time']
                time_data = datetime.datetime.fromisoformat(time_first[:-1])
                if datetime.timedelta(days=15) >= time_data - datetime.datetime.now() >= datetime.timedelta(days=0):
                    time_first = value['start_time']
                    print(value['name'], "  DATE: ", time_data.strftime("%d-%m-%y"), )
            except ValueError:
                time_first = value['start_time']
                time_data = datetime.datetime.strptime(time_first[2:10], "%y-%m-%d")
                if datetime.timedelta(days=15) >= time_data - datetime.datetime.now() >= datetime.timedelta(days=0):
                    time_first = value['start_time']
                    print(value['name'], "  DATE: ", time_data.strftime("%d-%m-%y"))


if __name__ == '__main__':
    URL = 'https://kontests.net/api/v1/sites'
    data = request_main(URL=URL)
    print(request(data=data))