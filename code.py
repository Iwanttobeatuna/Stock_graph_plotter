import numpy as np
import investpy
import pandas as pd
from cs50 import get_string
import plotly.express as px

## Getting the symbol from user
symbol = get_string("Symbol is ")
print(symbol)

## Getting stocks' open price, close price, low price, close price, volume and currency with investpy
df = investpy.get_stock_recent_data(stock=symbol, country='United States', as_json=False, order='ascending')

## Changing Pandas' database to csv
df.to_csv('file.csv',index=True, encoding='utf-8')
csv_file = 'file.csv'
df = pd.read_csv(csv_file)
print(df)

## Plotting close price against time
fig = px.line(df, x = 'Date', y = 'Close', title='Apple Share Prices over a month')
fig.show()

## Plotting volume traded against time
fig1 = px.line(df, x = 'Date', y = 'Volume', title='Volume traded over the past month')
fig1.show()
