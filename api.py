import requests
import matplotlib.pyplot as plt
import numpy as np

r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol=OANDA:EUR_USD&resolution=D&from=1572651390&to=1575243390&token=bqj97bvrh5r89luqta70')
#1573077600
print(r.json())

r2 = r.json()

#print(r2['c'][0])

f= open("apidata.txt","w")
for i in r2:
     f.write(str(i) + '\n')
     for n in r2[i]:
         f.write(str(n) + '\n')

length = len(r2['c'])
print(length)

candles = []
for i in range(length):
    candles.append([])
    candles[i].append(r2['c'][i])
    candles[i].append(r2['h'][i])
    candles[i].append(r2['l'][i])
    candles[i].append(r2['o'][i])
print(candles)

days = []
for i in range(length):
    days.append(i+1)
print(days)

closes = []
for i in range(length):
    closes.append(r2['c'][i])
print(closes)

plt.plot(days, closes, 'ro')
plt.ylabel('Close price')
plt.xlabel('Day')
plt.show()



f.close()



'''for i in range(length):
     for n in r2:
         f.write(str(n) + '\n')
         f.write(str(r2[n][i]) + '\n')
f.close()'''

f=open("apidata.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)
f.close()
