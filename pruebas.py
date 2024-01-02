import requests
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt

# Escribimos la fecha en formato string
ticker = input("Input the ticker symbol: ")
from_date = input("Input the start date in 'yyyy/mm/dd' format: ")
to_date = input("Input the end date in 'yyyy/mm/dd' format: ")

# Cambiamos los datos antes introducidos a tipo fecha
from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

# Ahora transformamos los datos tipo fecha a "epoch" legible para la máquina
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

# URL
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

# Encabezados para enmascararnos
headers = {
    "user-agent": "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
}

content = requests.get(url, headers=headers).content

with open("data.csv", "wb") as file:
    file.write(content)

# dataframe
df = pd.read_csv("data.csv")

# Resumen
summary = df.describe()
print(summary)

# Gráfico
plt.plot(df.Date, df.Close, label="Close")
plt.plot(df.Date, df.Open, label="Open")
plt.plot(df.Date, df.High, label="High")
plt.plot(df.Date, df.Low, label="Low")
plt.xticks([], rotation=45, fontsize=7)
plt.legend()

plt.show()