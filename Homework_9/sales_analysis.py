import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.txt', header=None, names=['Product ID', 'Sales', 'Region'])

print(f"Общая сумма продаж: {data['Sales'].sum()}")

print(f"Количество уникальных регионов продаж: {data['Region'].nunique()}")

print(f"Средняя сумма продаж на продукт: {data['Sales'].mean()}")

print(f"Продукт с наибольшей суммой продаж: {data.loc[data['Sales'].idxmax(), 'Product ID']}")

sales_by_region = data.groupby('Region')['Sales'].sum()
sales_by_region.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title('Сумма продаж по регионам')
plt.ylabel('')
plt.show()

# Топ 5 продуктов по продажам и построение круговой диаграммы
top_5_products = data.groupby('Product ID')['Sales'].sum().nlargest(5)
other_sales = data['Sales'].sum() - top_5_products.sum()
top_5_products['Other'] = other_sales
top_5_products.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title('Топ 5 продуктов по продажам')
plt.ylabel('')
plt.show()