import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('trade_data.csv', delimiter='\s+')

fig, ax = plt.subplots(figsize=(10, 6))

for country in data['Страна'].unique():
    country_data = data[data['Страна'] == country]
    ax.plot(country_data['Год'], country_data['Объём'], marker='o', label=country)

ax.set_xlabel('Год')
ax.set_ylabel('Объём торговли')
ax.legend()

years = data['Год'].unique()
plt.xticks(years)

plt.savefig('trade_volume.png')
plt.show()
