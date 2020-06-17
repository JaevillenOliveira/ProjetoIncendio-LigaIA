# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:46:32 2020

@author: Adlla Katarine e Daniel Alves
"""
import os as aqv
import pandas as pd

def main():
    addArea(converterKM())

def converterKM():
    lista = []
    with open('area.txt', 'r', encoding='utf-8') as arquivoTXT:
            listaAreas = arquivoTXT.readlines()
            
    for i in range(0, len(listaAreas)):
        listaAreas[i] = listaAreas[i].replace("km²", "").strip()
        nomeKM = listaAreas[i].split(' - ')
        km2 = float(nomeKM[1])
        dicCidades = {'cidade' : nomeKM[0], 'm²' : (km2*1000000)}
        lista.append(dicCidades)
    return lista

def addArea(lista):
    listaArquivos = aqv.listdir('.')
    
    for arquivo in listaArquivos: 
        nomeCidadeArq = arquivo.split(' - ')
        for nomeCidade in lista:
            if(nomeCidadeArq[0] == nomeCidade['cidade']):
                df = pd.read_csv(arquivo)
                df['area(m²)'] = nomeCidade['m²']
                df.to_csv(arquivo, index = False)

main()
