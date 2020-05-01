import requests
import json
import pandas as pd
import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt

def plot_data(exchange, currency1, currency2, timeframe, mav1, mav2, vYesOrNo):
    url = 'https://finnhub.io/api/v1/forex/candle?symbol='+exchange+':'+currency1+'_'+currency2+'&resolution='+timeframe+'&from=1572651390&to=1588194174&token=bqj97bvrh5r89luqta70'
    r = requests.get(url)
    data = json.loads(r.content)
    #print(data)

    reformatted_data = dict()
    reformatted_data['Date'] = []
    reformatted_data['Open'] = data['o']
    reformatted_data['High'] = data['h']
    reformatted_data['Low'] = data['l']
    reformatted_data['Close'] = data['c']
    reformatted_data['Volume'] = data['v']

    length = len(data['c'])
    for i in range(length):
        reformatted_data['Date'].append(datetime.datetime.fromtimestamp(data['t'][i]))

    #print(reformatted_data)
     
    pdata = pd.DataFrame.from_dict(reformatted_data)

    #print(pdata)

    pdata.set_index(keys = 'Date', inplace = True)
    mpf.plot(pdata, type='candle', mav = (mav1, mav2), title = currency1+'-'+currency2, volume = vYesOrNo)
    

plot_data('OANDA', 'GBP', 'USD', 'D', 7, 30, True)
