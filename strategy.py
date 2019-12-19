# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:36:08 2019

@author: HENAFF
"""
import numpy as np
from collections import OrderedDict
# =============================================================================
# Moving average strategy
# =============================================================================
def ma_close(df,span):
    ma = df.close.rolling(span).mean()
    colName = 'ma{}'.format(span)
    ma.columns = [colName]
    return ma


def ma_strat(df,span1,span2):
    ma1 = ma_close(df,span1)
    ma2 = ma_close(df,span2)
    
    diff = ma1 < ma2
    diff_forward = diff.shift(1)

    buy = np.where(diff - diff_forward == -1)[0]
    sell = np.where(diff - diff_forward == 1)[0]
    
    crossing = {}
    for order in buy.tolist():
        crossing[order] = 'b'
    for order in sell.tolist():
        crossing[order] = 's'
    return OrderedDict(sorted(crossing.items())), ma1, ma2


# =============================================================================
# Exponential moving average strategy
# =============================================================================
def ema_close(df,span):
    ema = df.close.ewm(span=span,adjust=False).mean()
    colName = 'ema{}'.format(span)
    ema.columns = [colName]
    return ema

def ema_strat(df,span1,span2):
    ema1 = ema_close(df,span1)
    ema2 = ema_close(df,span2)
    
    diff = ema1 < ema2
    diff_forward = diff.shift(1)

    buy = np.where(diff - diff_forward == -1)[0]
    sell = np.where(diff - diff_forward == 1)[0]

    crossing = {}
    for order in buy.tolist():
        crossing[order] = 'b'
    for order in sell.tolist():
        crossing[order] = 's'
    return OrderedDict(sorted(crossing.items())), ema1, ema2





