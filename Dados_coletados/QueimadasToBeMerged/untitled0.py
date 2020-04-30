#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:20:56 2020

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
                    focosFileName = 'Focos'+b+'_'+str(ano)+'_0'+str(mes)+'.csv'         
                else:
                   focosFileName = 'Focos'+b+'_'+str(ano)+'_'+str(mes)+'.csv'
                try:
                    focosFile = pd.read_csv(focosFileName)
                except:
                    continue;
                
                smallerDistance = 0 
                coordAqmB = None
                for indexA, rowA in focosFile.iterrows():
                      coordAqmA = (rowA["latitude"], rowA["longitude"])
                     # radiusA = rowA["area(m²)"] / 2
                      if(bool(coordAqmB)):
                          d = (hv(coordAqmA, coordAqmB))*1000 
                          if ((smallerDistance == 0) | (d < smallerDistance)):
                              smallerDistance = d
                
                      coordAqmB = coordAqmA
                print(smallerDistance)
              
                              

readFiles()                
                
                
                
                
                
                
                
                
                
                