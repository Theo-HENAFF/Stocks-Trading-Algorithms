import requests

def charts_request (stockName, interval="5m", rangee="1d"):
    #interval : Allowed values are (5m | 15m | 1d | 1wk | 1mo)
    #int_temps : Allowed values are (1d | 5d | 3mo | 6mo | 1y | 5y | max)
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

    querystring = {"region":"US","lang":"en","symbol":stockName,"interval":interval,"range":rangee}

    headers = {

        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()



# res = coin_request('TSLA','1d')
# timestamp = res["chart"]["result"][0]["timestamp"]
# openPrice = res["chart"]["result"][0]["indicators"]["quote"][0]["open"][0]
# print(timestamp,openPrice)