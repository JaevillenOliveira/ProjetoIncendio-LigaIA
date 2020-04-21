# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:09:08 2020

@author: Daniel Costa
"""

import os as aqv


listArchives = aqv.listdir('.')
listArchives.remove("LerCoordenadas.py")
listArchives.remove("1- Lugares sem informação para a data.txt")
listArchives.remove("Direção do Vento.txt")

a = 0 
for archive in listArchives:
    
############################################ SALVANDO AS COORDENADAS DE CADA ARQUIVO ############################################
    with open(archive, 'r') as archives:
        linhas = archives.readlines() #cada linha é um elemento da lista linhas
        linha0 = linhas[0] 
        linha1 = linhas[1] 
        
        
        linha0 = linha0.split(' ')
        linha1 = linha1.split(' ')
        
        linha0 = linha0[4]
        linha1 = linha1[3] 
        
        #linha0 = linha0 + ','
        
        #linha1 = linha1 + ','

        linha0 = linha0.rstrip('\n')
        linhat = linha0 +','+ linha1
        
        with open('coordenadas2.csv', 'a') as arq: #salvando em um arquivo só com coordenadas
           if a == 0:
              arq.write('lat,lon\n')
              a = 1

           arq.write(linhat)
##########################################################################################################################
