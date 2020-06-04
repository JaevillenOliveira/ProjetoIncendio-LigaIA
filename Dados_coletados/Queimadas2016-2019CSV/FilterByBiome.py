#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:42:00 2020

@author: jaevillen
"""

# =============================================================================
# This script gets the fires by year by month and splits it by biome, so the 
# result are files separated by year, month and biome
# ============================================================================= 

import pandas as pd

def func0():
    biomes = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"]
    for ano in range (2016, 2020):
        for mes in range (1,13):
            for b in biomes:
                if (mes < 10):
                    InFileName = str(ano)+'_0'+str(mes)+'_aqm.csv'
                    outFileName = b+'_'+str(ano)+'_0'+str(mes)+'_aqm.csv'
                else:
                     InFileName = str(ano)+'_'+str(mes)+'_aqm.csv'
                     outFileName = b+'_'+str(ano)+'_'+str(mes)+'_aqm.csv'
                
                inputFile = pd.read_csv(InFileName)
                
                outputFile = inputFile[(inputFile.bioma == b)]
                outputFile.to_csv(outFileName)
                
func0()
