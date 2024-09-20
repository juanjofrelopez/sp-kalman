import requests
import json
import numpy as np
import csv

def url_formatter(ticker):
  interval = "5d"
  tempReq = requester(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?formatted=true&lang=en-US&region=US&includeAdjustedClose=false&interval=5d&useYfid=true&corsDomain=finance.yahoo.com")
  init_date = tempReq['chart']['result'][0]['meta']['firstTradeDate']
  end_date = tempReq['chart']['result'][0]['meta']['currentTradingPeriod']['regular']['end']
  url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?formatted=true&lang=en-US&region=US&includeAdjustedClose=true&interval={interval}&period1={init_date}&period2={end_date}&events=capitalGain%7Cdiv%7Csplit&useYfid=true&corsDomain=finance.yahoo.com"
  return url

def requester(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
  res = requests.get(url, headers=headers)
  data = json.loads(res.text)
  return data

def save_csv(out,ticker):
  filename = f'data/{ticker}_quote_data.csv'
  with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['open', 'close', 'high', 'low', 'volume'])
    length = len(out[0])
    for i in range( len(out[0])):
        csv_writer.writerow(out[j][i] for j in range(5))
        
def data_parser(data,ticker):
  props = ['open', 'close', 'high', 'low', 'volume']
  out = []
  for prop in props:
    temp = data['chart']['result'][0]['indicators']['quote'][0][prop]
    out.append(temp)
  save_csv(out,ticker)
  out = np.array([data['chart']['result'][0]['indicators']['quote'][0][prop] for prop in props])
  return out

def get_data(ticker):
  url = url_formatter(ticker)
  data = requester(url)
  parsed = data_parser(data,ticker)
  np.save(f"npy_files/{ticker}_quote_data",parsed)
