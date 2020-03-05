# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:18:05 2020

@author: Adlla Katarine
"""

import os as aqv
import pandas as pd

############################################ CONVERTER ARQUIVOS .TXT EM .CSV ############################################
listArchives = aqv.listdir('path')

for archive in listArchives:
    
    with open(archive, 'r') as archiveTXT:
        linhas = archiveTXT.readlines() #cada linha é um elemento da lista linhas
        
    for i in range(0, len(linhas)):
        linhas[i] = linhas[i].replace(';', ',')
    
    with open(archive, 'w') as arquivo:
        arquivo.writelines(linhas)
    
    archive = "NATAL - RN (OMM 82598).txt"
    archiveAux = pd.read_csv(archive, header = None, error_bad_lines=False)
    name = archive.replace('.txt', '')
    archiveAux.to_csv(name +'.csv')
    
    for file in listArchives:
        aqv.remove(file)
####################################################################################################################################

