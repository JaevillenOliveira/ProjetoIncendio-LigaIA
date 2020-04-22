#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:42:00 2020

@author: jaevillen
"""

import pandas as pd

def func0():
    biomes = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"]
    for ano in range (2016, 2020):
        print(ano)
        for mes in range (1,13):
            for b in biomes:
                if (mes < 10):
                    InFileName = str(ano)+'_0'+str(mes)+'_aqm.csv'
                    outFileName = b+'_'+str(ano)+'_0'+str(mes)+'_aqm.csv'
                else:
                     InFileName = str(ano)+'_'+str(mes)+'_aqm.csv'
                     outFileName = b+'_'+str(ano)+'_'+str(mes)+'_aqm.csv'
                
                inputFile = pd.read_csv(InFileName, index_col=0)
             
                outputFile = inputFile[(inputFile.bioma == b)]
                outputFile.to_csv(outFileName)
                
func0()