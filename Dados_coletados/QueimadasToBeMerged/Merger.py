#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:33:40 2020

@author: jaevillen
"""


import pandas as pd
from haversine import haversine as hv

def readFiles():
    biomes = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"]
    for b in biomes:
        for ano in range (2016, 2020):
            for mes in range (1, 13):
                print("               Files:"+b+str(ano)+str(mes))
                if (mes < 10):
                    aqmFileName = b+'_'+str(ano)+'_0'+str(mes)+'_aqm.csv'
                    focosFileName = 'Focos'+b+'_'+str(ano)+'_0'+str(mes)+'.csv'
                    outName = 'Merged/Queimadas'+b+'_'+str(ano)+'_0'+str(mes)+'.csv'
                else:
                    aqmFileName = b+'_'+str(ano)+'_'+str(mes)+'_aqm.csv'
                    focosFileName = 'Focos'+b+'_'+str(ano)+'_'+str(mes)+'.csv'
                    outName = 'Merged/Queimadas'+b+'_'+str(ano)+'_'+str(mes)+'.csv'
                try:
                    aqmFile = pd.read_csv(aqmFileName, index_col=0)
                    focosFile = pd.read_csv(focosFileName)
                except:
                    continue;
                                
                df = pd.DataFrame(getCoordinates(aqmFile, focosFile))
                df.to_csv(outName, index=False)
                    
                                                                
def getCoordinates(aqmFile, focosFile):  
    listOfDicts  = []
    for indexA, rowA in aqmFile.iterrows():
        coordAqm = (rowA["latitude"], rowA["longitude"])
        fireRadius = rowA["area(m²)"] / 2
        rowsToDrop = []
        if(focosFile.empty):
            print("Empty in "+str(indexA))
        for indexB, rowF in focosFile.iterrows():
            coordfocos = (rowF["latitude"],rowF["longitude"])
            if (belongs(coordAqm, fireRadius, coordfocos)):
                data = (rowF["datahora"])[0:11]
                d = {"data" :data, "latitude": rowA["latitude"], "longitude": rowA["longitude"], 
                     "area": rowA["area(m²)"], "diasemchuva": rowF["diasemchuva"], 
                     "precipitacao": rowF["precipitacao"], "riscofogo": rowF["riscofogo"]}
                
                listOfDicts.append(d)
                rowsToDrop.append(indexB)
                       
        focosFile.drop(rowsToDrop, inplace=True)
                
    return listOfDicts;
               
         
def belongs(fire, fireRadius, focus):
    fireFocusDistance = hv(fire, focus) # return the distance in kilometers
    fireFocusDistance = fireFocusDistance*1000
    if(fireFocusDistance < fireRadius):
        return True;
        
        

                 
readFiles()
                    