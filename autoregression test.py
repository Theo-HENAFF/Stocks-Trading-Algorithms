# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:29:30 2019

@author: HENAFF
"""
from dataframeBuild import dfCreation
from strategy import ma_strat, ema_strat


import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error

df = dfCreation("^FCHI",rangee = "1y",interval = "1d")
crossing_ema, ema6, ema15 = ema_strat(df,5,10)

# split dataset
X = ema15.values
train, test = X[1:len(X)-7], X[len(X)-7:]
# train autoregression
model = AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
for i in range(len(predictions)):
	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot results
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()