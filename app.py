# © Stock Suggester- Made by Yuval Simon. For bogan.cool

import yfinance as yf
from pandas_datareader import data as pdr

import datetime
from dateutil.relativedelta import relativedelta

import math
import sys

import requests
from bs4 import BeautifulSoup

options = input("(i) Do you want me to scrape HQ stocks from yahoo finance's website? (yes/no): ")

start_date_input = int(input("(1) Enter time (number) in months to start with: "))
ma_input = int(input("(2) Enter moving average (number): "))

if options == 'yes':

    def actives():
        url = 'https://finance.yahoo.com/most-active/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find_all("div", {"id": "Lead-5-ScreenerResults-Proxy"})

        td1 = table[0].find_all("td", {"aria-label": "Symbol"})

        a = td1[0].find_all("a", {"class": "Fw(600) C($linkColor)"})
        for a in td1:
            try:
                # Finding stock and prices
                yf.pdr_override()

                stock = a.text
                now = datetime.datetime.now()

                startdate = datetime.datetime.today() + relativedelta(months=-start_date_input)

                df = pdr.get_data_yahoo(stock, startdate, now)

                ma = ma_input

                smaString = "Sma_" + str(ma)

                df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

                df = df.iloc[ma:]

                # Checking stock prices average
                prices = [math.trunc(df["Close"][i]) for i in df.index]
                total = sum(prices)

                amount = len([Int for Int in prices if isinstance(Int, int)])

                average = total / amount

                # print(f'The average is: {math.trunc(average)}')


                # Checking if you should buy the stock.
                today_stock = pdr.get_data_yahoo(stock, now, now)

                numb = [math.trunc(today_stock["High"][i]) for i in today_stock.index]

                sum_numb = sum(numb)
                # print(f"Current {stock}'s price per share is: {sum_numb}")

                if sum_numb < average:
                    print(f'{stock}I suggest you to buy this stock!')
                    abcdeh = f'-{stock}- I suggest you to buy \n'
                    with open('stocks.txt', 'a+') as f:
                        f.write(abcdeh)
                        f.close()

                elif sum_numb > average:
                    print('')

            except ZeroDivisionError:
                print('Stock not found!')
                pass

    def trendings():
        url = 'https://finance.yahoo.com/trending-tickers'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find_all("div", {"id": "Lead-4-YFinListTable-Proxy"})

        td1 = table[0].find_all("td", {"class": "data-col0 Ta(start) Pstart(6px) Pend(15px)"})

        a = td1[0].find_all("a", {"class": "Fw(b)"})
        for a in td1:
            try:
                # Finding stock and prices
                yf.pdr_override()

                stock = a.text
                now = datetime.datetime.now()

                startdate = datetime.datetime.today() + relativedelta(months=-start_date_input)

                df = pdr.get_data_yahoo(stock, startdate, now)

                ma = ma_input

                smaString = "Sma_" + str(ma)

                df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

                df = df.iloc[ma:]

                # Checking stock prices average
                prices = [math.trunc(df["Close"][i]) for i in df.index]
                total = sum(prices)

                amount = len([Int for Int in prices if isinstance(Int, int)])

                average = total / amount

                # print(f'The average is: {math.trunc(average)}')

                # Checking if you should buy the stock.
                today_stock = pdr.get_data_yahoo(stock, now, now)

                numb = [math.trunc(today_stock["High"][i]) for i in today_stock.index]

                sum_numb = sum(numb)
                # print(f"Current {stock}'s price per share is: {sum_numb}")

                if sum_numb < average:
                    print(f'{stock}I suggest you to buy this stock!')
                    abcdeh = f'-{stock}- I suggest you to buy \n'
                    with open('stocks.txt', 'a+') as f:
                        f.write(abcdeh)
                        f.close()

                elif sum_numb > average:
                    print('')

            except ZeroDivisionError:
                print('Stock not found!')
                pass

    def gainers():
        url = 'https://finance.yahoo.com/gainers'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find_all("div", {"id": "mrt-node-Lead-5-ScreenerResults"})

        td1 = table[0].find_all("td", {"aria-label": "Symbol"})
        a = td1[0].find_all("a", {"class": "Fw(600) C($linkColor)"})
        for a in td1:
            try:
                # Finding stock and prices
                yf.pdr_override()

                stock = a.text
                now = datetime.datetime.now()

                startdate = datetime.datetime.today() + relativedelta(months=-start_date_input)

                df = pdr.get_data_yahoo(stock, startdate, now)

                ma = ma_input

                smaString = "Sma_" + str(ma)

                df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

                df = df.iloc[ma:]

                # Checking stock prices average
                prices = [math.trunc(df["Close"][i]) for i in df.index]
                total = sum(prices)

                amount = len([Int for Int in prices if isinstance(Int, int)])

                average = total / amount

                # print(f'The average is: {math.trunc(average)}')

                # Checking if you should buy the stock.
                today_stock = pdr.get_data_yahoo(stock, now, now)

                numb = [math.trunc(today_stock["High"][i]) for i in today_stock.index]

                sum_numb = sum(numb)
                # print(f"Current {stock}'s price per share is: {sum_numb}")

                if sum_numb < average:
                    print(f'{stock}I suggest you to buy this stock!')
                    abcdeh = f'-{stock}- I suggest you to buy \n'
                    with open('stocks.txt', 'a+') as f:
                        f.write(abcdeh)
                        f.close()

                elif sum_numb > average:
                    print('')

            except ZeroDivisionError:
                print('Stock not found!')
                pass

    actives()
    gainers()
    trendings()

    lines_seen = set()  # holds lines already seen
    outfile = open('stocks_no_dups.txt', "w")
    for line in open('stocks.txt', "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

elif options == 'no':
    Stock = input('(3) Please enter stock symbol: ')
    # Finding stock and prices
    yf.pdr_override()

    stock = Stock
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

        # print(f'The average is: {math.trunc(average)}')

    except ZeroDivisionError:
        print('Stock not found!')
        sys.exit()

    # Checking if you should buy the stock.
    today_stock = pdr.get_data_yahoo(stock, now, now)

    numb = [math.trunc(today_stock["High"][i]) for i in today_stock.index]

    sum_numb = sum(numb)
    # print(f"Current {stock}'s price per share is: {sum_numb}")

    if sum_numb < average:
        print(f'-{stock}- I suggest you to buy this stock!')

    elif sum_numb > average:
        print('')
