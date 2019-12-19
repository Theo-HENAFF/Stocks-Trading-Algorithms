from dataframeBuild import dfCreation
from strategy import ma_strat, ema_strat
from backTesting import rendement_strategy

from pandas.plotting import lag_plot
from statistics import mean 
import matplotlib.pyplot as plt

# =============================================================================
# Creation du dataframe avec  récolte des donnees via l'API
# interval : Allowed values are (5m | 15m | 1d | 1wk | 1mo)
# rangee : Allowed values are (1d | 5d | 3mo | 6mo | 1y | 5y | max)
# =============================================================================

df = dfCreation("^FCHI",rangee = "1y",interval = "1d")

# =============================================================================
# Other columns plot
# =============================================================================
# ax = plt.gca()
# df.plot(y='close',x='date',color='red',ax=ax)
# df.plot(y='open',x='date',color='blue',ax=ax)
# df.plot(y='low',x='date',color='green',ax=ax)
# df.plot(y='high',x='date',color='cyan',ax=ax)
# plt.title("Cours du CAC40 sur les dernières 24h")


# =============================================================================
# MA plot
# =============================================================================
# ax = plt.gca()
# ma6.plot(y='ma6',color='blue',ax=ax)
# ma15.plot(y='ma15',color='cyan',ax=ax)
# df.plot(y='close',x='date',color='red',ax=ax)
# plt.title("Cours du CAC40 sur les dernières 24h avec courbes MA6(bleu) et MA12(cyan)")


# =============================================================================
# EMA plot
# =============================================================================
# ax = plt.gca()
# ma6.plot(y='ema6',color='blue',ax=ax)
# ma15.plot(y='ema15',color='cyan',ax=ax)
# df.plot(y='close',x='date',color='red',ax=ax)
# plt.title("Cours du CAC40 sur les dernières 24h avec courbes EMA5(bleu) et EMA10(cyan)")


# plt.show()


# =============================================================================
# MA Strat
# =============================================================================
crossing_ma, ma6, ma15 = ma_strat(df,6,15)
# for order in crossing_ma:
#     if crossing_ma[order] == 'b':
#         print('MA-->need to sell at : ', df.iloc[[order]].date.to_string(index=False))
#     else :
#         print('MA-->need to buy at : ', df.iloc[[order]].date.to_string(index=False))


# =============================================================================
# EMA Strat
# =============================================================================
crossing_ema, ema6, ema15 = ema_strat(df,5,10)
# for order in crossing_ema:
#     if crossing_ema[order] == 'b':
#         print('EMA-->need to sell at : ', df.iloc[[order]].date.to_string(index=False))
#     else :
#         print('EMA-->need to buy at : ', df.iloc[[order]].date.to_string(index=False))



# =============================================================================
# Afficher le rendement arithmétique de la stratégie
# =============================================================================
print(rendement_strategy(df,ema_strat,5,15))

# =============================================================================
# Afficher le rendement arithmétique du portefolio
# =============================================================================
# liste_action=["BRK-B","NKE","LVMHF","AAPL","GE","TSLA","GS","^FCHI","PFE"]
# liste_rendement = []
# for action in liste_action:
#     mes1, rendement, mes2 = rendement_strategy(dfCreation(action,rangee = "1mo",interval = "1d"),ema_strat,5,15)
#     liste_rendement.append(rendement)
# print("Rendement moyen du portefolio : ", round(mean(liste_rendement),5), "%")


print(type(df.close.values))
lag_plot(df.close)
plt.show()






















