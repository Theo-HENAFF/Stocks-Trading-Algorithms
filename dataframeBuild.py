import pandas as pd
from apiRequest import charts_request
from datetime import datetime


def dfCreation(Stocks_Name,interval="5m",rangee="1d"):
    res = charts_request(Stocks_Name,interval,rangee)
    dictIndex = res["chart"]["result"][0]["timestamp"]

    listeIndex = []
    for index in dictIndex:
         listeIndex.append(datetime.fromtimestamp(index))
    
    lowDict = res["chart"]["result"][0]["indicators"]["quote"][0]["low"]
    
    highDict = res["chart"]["result"][0]["indicators"]["quote"][0]["high"]

    closeDict = res["chart"]["result"][0]["indicators"]["quote"][0]["close"]

    openDict = res["chart"]["result"][0]["indicators"]["quote"][0]["open"]


    df = pd.DataFrame({'open': openDict, 'close': closeDict, 'high': highDict, 'low': lowDict, 'date': listeIndex}, index = listeIndex)
    return df

#print(dfCreation('TSLA','1d'))


