import yfinance as yf
from pandas_datareader import data as pdr

import datetime
from dateutil.relativedelta import relativedelta

import math

# Finding stock and prices
yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")

now = datetime.datetime.now()

startdate = datetime.datetime.today() + relativedelta(months=-12)

df = pdr.get_data_yahoo(stock, startdate, now)

ma = 50

smaString = "Sma_" + str(ma)

df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

df = df.iloc[ma:]

# Checking stock prices average
prices = [math.trunc(df["Close"][i]) for i in df.index]

total = sum(prices)

amount = len([Int for Int in prices if isinstance(Int, int)])

average = total / amount

print(f'The average is: {math.trunc(average)}')


# Checking if you should buy the stock.
today = pdr.get_data_yahoo(stock, now, now)

numb = [math.trunc(today["High"][i]) for i in today.index]

sum_numb = sum(numb)

if sum_numb < average:
    print('I suggest you to buy this stock!')

elif sum_numb > average:
    print('I suggest you to NOT buy this stock.')
