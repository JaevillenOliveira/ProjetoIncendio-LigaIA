#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 20:53:40 2020

@author: jaevillen
"""

import json
import pandas as pd
import numpy as np
from haversine import haversine as hv
from statistics import mean 

with open('result.json') as datafile:
    #esse json contém os caminhos pra cada dataset, podendo achar o foco
    #e o aqm com a chave ano e mês
    paths = json.load(datafile)

biomas = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"] 

def main(): 
    num = 0
    for ano in range (2017, 2020):
        for mes in range(1, 13):
            for bioma in biomas:
                
                strmes = mesToStr(mes)
                pathAqm = getPath(str(ano), strmes, 'aqm')
                pathFoco = getPath(str(ano), strmes, 'foco')
                if(pathAqm and pathFoco):
                    df1 = pd.read_csv(pathAqm)
                    df2 = pd.read_csv(pathFoco)
                    aqm = df1[(df1.bioma == bioma)]
                    foco = df2[(df2.bioma == bioma)]  
                    num += 1
                    populateDataset(aqm, foco, str(ano), strmes, bioma, num)


def getPath(ano, mes, tipo):
    try:
        return paths[ano][mes][tipo]
    except:
        return None

  
def mesToStr(mes):
    if mes < 10:
        return '0' + str(mes)
    else: 
        return str(mes)

def populateDataset(aqm, foco, ano, mes, bioma, num):
    COLUMN_NAMES=['latitude','longitude','bioma','area(m²)','diasemchuva','precipitacao','riscofogo']
    df = pd.DataFrame(columns=COLUMN_NAMES)    
    count = 0;
    lenght = len(aqm)
   
    focos = np.empty((0, 2), dtype=float)
    for index, focoRow in foco.iterrows():         
        focos = np.append(focos, np.array([[focoRow['latitude'], focoRow['longitude']]]), axis=0)

    for index, aqmRow in aqm.iterrows():
        pointAqm = (aqmRow['latitude'], aqmRow['longitude'])
        fireRadius = aqmRow["area(m²)"] / 2

        under_radius = searchCloseFocos(pointAqm, focos, fireRadius)
        mean = calculate_mean(foco, under_radius)
        
        df = df.append({'latitude' : aqmRow['latitude'] ,'longitude' : aqmRow['longitude'] ,'bioma' : aqmRow['bioma'] ,'area(m²)' : aqmRow['area(m²)'] ,'diasemchuva' : mean['diasemchuva'] ,'precipitacao' : mean['precipitacao'] , 'riscofogo' : mean['riscofogo']}, ignore_index=True)
        print('appending: ' + str(count) + ' from: ' + str(lenght) + ' rows | in dataset ' + str(num) + ' from: 288‬')
        count += 1
        
    outName = 'Fires/'+bioma + '_' + ano + '_' + mes + '.csv'
    df.to_csv(outName)
    

def searchCloseFocos(pointAqm, focos, fireRadius):

    result = np.empty(shape=[0, 1], dtype=float)
    for foco in focos:
        distance = hv(pointAqm, foco)
        result = np.append(result, np.array([[distance]]), axis=0)
           
    under_radius = []
    for i, r in enumerate(result, start=0):
        if(r < fireRadius):
            under_radius.append(i)
    return under_radius;


def calculate_mean(focos, under_radius):
    dias_sem_chuva = []
    precipitacao = []
    riscofogo = []

    for index in under_radius:
        foco = focos.iloc[index]
        dias_sem_chuva.append(foco['diasemchuva'])
        precipitacao.append(foco['precipitacao'])
        riscofogo.append(foco['riscofogo'])

    d = {'diasemchuva': np.nanmean(dias_sem_chuva), 'precipitacao' : np.nanmean(precipitacao), 'riscofogo' : np.nanmean(riscofogo)}
    return d;

main()    
