# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:18:05 2020

@author: Adlla Katarine
"""

import os as aqv
import pandas as pd

listArchives = aqv.listdir('.')
listArchives.remove("conversao_csv.py")

for archive in listArchives:
    
############################################ CONVERTER ARQUIVOS .TXT EM .CSV ############################################
    with open(archive, 'r') as archiveTXT:
        linhas = archiveTXT.readlines() #cada linha é um elemento da lista linhas
        linha0 = linhas[0]
        linha1 = linhas[1]
        linhas.remove(linha0)
        linhas.remove(linha1)
        
    for i in range(0, len(linhas)):
        linhas[i] = linhas[i].replace(';', ',')
    
    with open(archive, 'w') as arquivo:
        arquivo.writelines(linhas)
    
    archiveAux = pd.read_csv(archive, header = None, error_bad_lines=True)
    name = archive.replace('.txt', '') + '.csv'
    archiveAux.to_csv(name)
##########################################################################################################################
    
    
############################################ REMOVER LINHA .CSV ############################################
    with open(name, "r") as arq:
        linhas = arq.readlines()
        newLinha0 = linhas[0]
        linhas.remove(newLinha0)
        
    with open(name, 'w') as arquivo:
        arquivo.writelines(linhas)
##########################################################################################################################


############################################ CONVERTER ARQUIVOS .TXT EM .CSV ############################################
    df = pd.read_csv(name)
    df = df.drop(columns=['0'])
    df = df.rename(columns={'Unnamed: 14': 'Latitude'})
    df['Latitude'] = linha0.strip('Latitude (graus) : ')
    df['Longitude'] = linha1.strip('Longitude (graus) : ')
    df.to_csv(name, index = False)
    
for file in listArchives:
    aqv.remove(file)
####################################################################################################################################

