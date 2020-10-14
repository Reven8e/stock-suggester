import yfinance as yf
from pandas_datareader import data as pdr

import datetime
from dateutil.relativedelta import relativedelta

import math

import sys


# Finding stock and prices
yf.pdr_override()

stock = input("(1) Enter a stock ticker symbol: ")
start_date_input = int(input("(2) Enter time (number) in months to start with: "))
ma_input = int(input("(3) Enter moving average (number): "))

now = datetime.datetime.now()

startdate = datetime.datetime.today() + relativedelta(months=-start_date_input)

df = pdr.get_data_yahoo(stock, startdate, now)

ma = ma_input

smaString = "Sma_" + str(ma)

df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

df = df.iloc[ma:]

# Checking stock prices average
try:
    prices = [math.trunc(df["Close"][i]) for i in df.index]
    total = sum(prices)

    amount = len([Int for Int in prices if isinstance(Int, int)])

    average = total / amount

    print(f'The average is: {math.trunc(average)}')

except ZeroDivisionError:
    print('Stock not found!')
    sys.exit(0)


# Checking if you should buy the stock.
today_stock = pdr.get_data_yahoo(stock, now, now)

numb = [math.trunc(today_stock["High"][i]) for i in today_stock.index]

sum_numb = sum(numb)
print(f"Current {stock}'s price per share is: {sum_numb}")

if sum_numb < average:
    print('I suggest you to buy this stock!\n')

elif sum_numb > average:
    print('I suggest you to NOT buy this stock.')
