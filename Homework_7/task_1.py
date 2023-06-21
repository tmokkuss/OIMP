import pandas as pd
import datetime as dt

data = pd.read_csv('source_data.csv')
data['date'] = pd.to_datetime(data['date'])
data_january = data[data['date'].dt.month == 1]
data['day'] = data['date'].dt.day
data['hour'] = data['date'].dt.hour
print(data.head())

print("Количество заказов с 'order_price' != 0:", data.query('order_price != 0').shape[0])

print("Процент заказов с нулевой ценой от общего числа заказов в январе:",
      data.query('order_price == 0').shape[0] / data_january.shape[0] * 100)

print("Найти, в какие дни у нас есть заказы с ценой == 0", data.query('order_price == 0')['day'].unique())

print("Топ 100-пользователей по частоте заказов:\n",
      data.groupby('uid')['order_id'].nunique().sort_values(ascending=False).head(100))

print("Топ 100-пользователей по сумме заказов:\n",
      data.groupby('uid')['order_price'].sum().sort_values(ascending=False).head(100))

print("Топ-10 пользователей по приборам:\n", data.groupby('uid')['cutlery'].sum().sort_values(ascending=False).head(10))

print("Топ-20 пользователей по чаевым:\n", data.groupby('uid')['tips'].sum().sort_values(ascending=False).head(20))

print("Топ 20 дней, когда чаевых было больше всего:\n",
      data.groupby('day')['tips'].sum().sort_values(ascending=False).head(20))

print("Какое количество столовых приборов пользуется популярностью?:\n", data['cutlery'].value_counts())

print("Количество пользователей всего:", data['uid'].nunique())

print("Топ-10 пользователей, которые потратили наибольшее количество денег в сервисе:\n",
      data.groupby('uid')['order_price'].sum().sort_values(ascending=False).head(10))

print("Топ 5 дней, в которые было больше всего заказов?\n",
      data.loc[data['day'] != dt.date(2022, 1, 1)].groupby('day')['order_id'].nunique().sort_values(ascending=False).head(5))

