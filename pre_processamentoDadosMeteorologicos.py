# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:53:16 2020

@author: Adlla Katarine
"""

import os as aqv
import pandas as pd
from sklearn.impute import SimpleImputer # Tratando valores 'nan' da base de dados
import numpy as np 

listaArquivos = aqv.listdir('.')

for arquivo in listaArquivos:
    df = pd.read_csv(arquivo)
    
    #print(df.Estacao.isnull().sum(),  "  -  ",  df.shape)
    
    #print(df.Data.isnull().sum(),  "  -  ",  df.shape)
    
    print(df.Hora.isnull().sum(),  "  -  ",  df.shape)
    
    auxDirecaoVento = df.DirecaoVento.isnull().sum()
    if(auxDirecaoVento >= int(len(df)*0.7)):
        df = df.drop(columns=['DirecaoVento'])
        print(auxDirecaoVento,  "  -  ",  df.shape)
    
    
    auxVelocidadeVentoMedia = df.VelocidadeVentoMedia.isnull().sum()
    if(auxVelocidadeVentoMedia >= int(len(df)*0.7)):
        df = df.drop(columns=['VelocidadeVentoMedia'])
        print(auxVelocidadeVentoMedia,  "  -  ",  df.shape)
    
    
    auxVelocidadeVentoMaximaMedia = df.VelocidadeVentoMaximaMedia.isnull().sum()
    if(auxVelocidadeVentoMaximaMedia >= int(len(df)*0.7)):
        df = df.drop(columns=['VelocidadeVentoMaximaMedia'])
        print(auxVelocidadeVentoMaximaMedia,  "  -  ",  df.shape)
    
    auxInsolacaoTotal = df.InsolacaoTotal.isnull().sum()
    if(auxInsolacaoTotal >= int(len(df)*0.7)):
        df = df.drop(columns=['InsolacaoTotal'])
        print(auxInsolacaoTotal,  "  -  ",  df.shape)
    
    
    auxNebulosidadeMedia = df.NebulosidadeMedia.isnull().sum()
    if(auxNebulosidadeMedia >= int(len(df)*0.7)):
        df = df.drop(columns=['NebulosidadeMedia'])
        print(auxNebulosidadeMedia,  "  -  ",  df.shape)
    
    
    auxNumDiasPrecipitacao = df.NumDiasPrecipitacao.isnull().sum()
    if(auxNumDiasPrecipitacao >= int(len(df)*0.7)):
        df = df.drop(columns=['NumDiasPrecipitacao'])
        print(auxNumDiasPrecipitacao,  "  -  ",  df.shape)
    
    
    
    auxPrecipitacaoTotal = df.PrecipitacaoTotal.isnull().sum()
    if(auxPrecipitacaoTotal >= int(len(df)*0.7)):
        df.drop(columns=['PrecipitacaoTotal'])
        print(auxPrecipitacaoTotal,  "  -  ",  df.shape)
    
    
    auxTempMinimaMedia = df.TempMinimaMedia.isnull().sum()
    if(auxTempMinimaMedia >= int(len(df)*0.7)):
        df = df.drop(columns=['TempMinimaMedia'])
        print(auxTempMinimaMedia,  "  -  ",  df.shape)
    
    
    auxUmidadeRelativaMedia = df.UmidadeRelativaMedia.isnull().sum()
    if(auxUmidadeRelativaMedia >= int(len(df)*0.7)):
        df = df.drop(columns=['UmidadeRelativaMedia'])
        print(auxUmidadeRelativaMedia,  "  -  ",  df.shape)
    
    
    '''
    print('Linhas a serem excluídas.')
    for i in range(len(arquivo)):
        auxQuant = df.loc[0, :].isnull().sum()
        if(auxQuant == 14 or auxQuant == 15):
            print(auxQuant)
    '''      
    # Imputer recebe a classe que tratar dados nulos
    # Preenchendo valores nulos com os mais frequentes
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0)
    imputer = imputer.fit(df.iloc[:,3:]) 
    df.iloc[:,3:] = imputer.fit_transform(df.iloc[:,3:]) # Atribui as modificação de valores nulos, a mesma variavel