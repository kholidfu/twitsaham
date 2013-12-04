import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import re
import time
import urllib2

# download data
def dl():
    url = 'http://finance.yahoo.com/q/hp?s=%5EJKSE+Historical+Prices'
    html = urllib2.urlopen(url).read()
    pattern = re.compile(r"http://ichart.*=\.csv\"")
    m = re.search(pattern, html).group()

    with open('table.csv', 'wb') as f:
        f.write(urllib2.urlopen(m).read())

    df = pd.read_csv('table.csv', index_col='Date', parse_dates=True)
    df = df.sort_index(ascending=True)
    df = df.tail(80)
    # analysis
    macd = pd.rolling_mean(df['Adj Close'], 12)
    # bollinger bands
    # https://github.com/arvindevo/MachineLearningForTrading/blob/master/bollingerbands.py
    movavg = pd.rolling_mean(df['Adj Close'], 20, min_periods=20)
    movstddev = pd.rolling_std(df['Adj Close'], 20, min_periods=20)
    upperband = movavg + 2*movstddev
    lowerband = movavg - 2*movstddev

    # plot settings
    matplotlib.rcParams.update({'font.size': 8})
    s = datetime.now()

    # begin plot
    df['Adj Close'].plot(label='Close')
    macd.plot(label='macd', linestyle='--', color='r')
    upperband.plot(color='green')
    lowerband.plot(color='green')

    plt.title('Analisis Teknikal MACD dan Bollinger Bands IHSG')
    plt.legend(['Adjusted Close', 'MACD', 'Upper Bollinger', 'Lower Bollinger'])
    plt.xlim(s - timedelta(days=130), s + timedelta(days=7))
    plt.ylabel('Adjusted Close')
    plt.xlabel('Tanggal')

    # save the image for twitter update with image
    plt.savefig('ihsg.png')

    # show graph
    # plt.show()

dl()
