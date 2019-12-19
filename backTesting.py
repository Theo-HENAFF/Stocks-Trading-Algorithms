# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:38:25 2019

@author: HENAFF
"""

#import zipline
from statistics import mean 

# =============================================================================
# Calcul du rendement d'une stratégie 'a la main'
# =============================================================================
def rendement_strategy(df, strategy, span1, span2):
    crossing, series1, series2 = strategy(df, span1, span2)
    rendement = []
    for i,order in enumerate(crossing):
        if crossing[order] == 's' and i==0: #on ne vend pas si on a pas achete avant
            pass
        elif crossing[order] == 'b':
            achat = df.close.iloc[[order]].item()
        else:
            vente = df.close.iloc[[order]].item()
            rendement.append((achat-vente)/achat)
    
    return 'Le rendement arithmétique moyen est de : ',round(mean(rendement)*100,5),'%'
    
    
    
    
    
    
    
    
