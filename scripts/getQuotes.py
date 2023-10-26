import yfinance as yf
import pandas as pd
import getticker
import configmanager
import os

class GetData:
    def __init__(self):
        config_manager = configmanager.Configs()
        self.all_configs = config_manager.read_configs()
        self._output_path = self.all_configs['application']['outputpath']

def runprocess():
    getdata = GetData()
    tickerlist = getticker.TickerList()
    dfticker = tickerlist.readdata()
    print(dfticker) 

    # for index, row in dfticker.iterrows():
    for row in dfticker.iterrows():
        tickerdata = yf.Ticker(row['Symbol'])
        df = pd.DataFrame(tickerdata.dividends)
        if not df.empty:
            path = getdata._output_path + row['Symbol'] + '.csv'
            print(path)
            df.to_csv(path)

        print(tickerdata.dividends)
        # tickerdf = tickerdata.history(period='1d', start='2013-10-24', end='2023-10-24')

print(os.getcwd())
runprocess()

# tickersymbol = '5PAISA.NS'
# tickerdata = yf.Ticker(tickersymbol)
# tickerdf = tickerdata.history(period='1d', start='2023-1-1', end='2023-10-16')
# print(tickerdf)

# ticker2 = tickerdata.actions
# print(ticker2)
# ticker2 = tickerdata.dividends
# print(ticker2)
# ticker2 = tickerdata.splits
# print(ticker2)
# # ticker2 = tickerdata.earnings
# # print(ticker2)
# ticker2 = tickerdata.get_earnings_forecast
# print(ticker2)


# df = pd.DataFrame(tickerdf)
# path = './Output/' + tickersymbol + '.csv'

# -------------Dont open this------------
# Closing save line temporarily for testing
# df.to_csv(path)