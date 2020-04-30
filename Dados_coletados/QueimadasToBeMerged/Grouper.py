#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:43:57 2020

@author: jaevillen
"""
import pandas as pd
import numpy as np


def readFiles():
    biomes = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"]
    for b in biomes:
        for ano in range (2016, 2020):
            for mes in range (1, 13):
                print("               Files:"+b+str(ano)+str(mes))
                if (mes < 10):
                    focosFileName = 'Focos'+b+'_'+str(ano)+'_0'+str(mes)+'.csv'
                    outName = 'FocosAgrupados'+b+'_'+str(ano)+'_0'+str(mes)+'.csv'
                else:
                    focosFileName = 'Focos'+b+'_'+str(ano)+'_'+str(mes)+'.csv'
                    outName = 'FocosAgrupados'+b+'_'+str(ano)+'_'+str(mes)+'.csv'
                try:
                    focosFile = pd.read_csv(focosFileName)
                except:
                    continue;
                                               
                df = pd.DataFrame(goThroughFiles(focosFile))
                df.to_csv(outName, index=False)
                
def goThroughFiles(focosFile):
    print(focosFile.index) 
    listOfDicts = []
    for indexA, rowA in focosFile.iterrows():
        rowCounter = 0
        nonEmptydsc = 0
        nonEmptyrf = 0
        nonEmptypr = 0
        
        dataA = (rowA["datahora"])[0:11]
        latA = rowA["latitude"]
        lonA = rowA["longitude"]
        
        diasemchuva = rowA["diasemchuva"]
        precipitacao = rowA["precipitacao"]
        riscofogo = rowA["riscofogo"]
        
        for indexB, rowB in focosFile.iterrows():
            dataB = (rowB["datahora"])[0:11]
            latB = rowB["latitude"]
            lonB = rowB["longitude"]
            if ((latA == latB) & (lonA == lonB) & (dataA == dataB)):
                if(~np.isnan(rowB["diasemchuva"])):
                   if (np.isnan(diasemchuva)):
                       diasemchuva = rowB["diasemchuva"]
                   else:
                       diasemchuva += rowB["diasemchuva"]
                       nonEmptydsc += 1

                if(~np.isnan(rowB["riscofogo"])):
                   if (np.isnan(riscofogo)):
                       riscofogo = rowB["riscofogo"]
                   else:
                       riscofogo += rowB["riscofogo"]
                       nonEmptyrf += 1         
                       
                if(~np.isnan(rowB["precipitacao"])):
                   if (np.isnan(precipitacao)):
                       precipitacao = rowB["precipitacao"]
                   else:
                       precipitacao += rowB["precipitacao"]
                       nonEmptypr += 1                         

                
                focosFile.drop(focosFile.index[rowCounter])
            rowCounter += 1
        
        if(nonEmptydsc > 0):
            diasemchuva = diasemchuva/nonEmptydsc
        if(nonEmptyrf > 0):
            riscofogo = riscofogo/nonEmptyrf
        if(nonEmptypr > 0):
            precipitacao = precipitacao/nonEmptypr
        
        d = {"data": dataA, "latitude": latA, "longitude": lonA, "diasemchuva": diasemchuva, 
             "precipitacao": precipitacao, "riscofogo": riscofogo}
        
        listOfDicts.append(d)
        
    return listOfDicts;

            
readFiles()                
                
                
                
                
                
                
                
                
                
                
                
                
                