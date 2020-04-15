# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:43:34 2020

@author: Daniel Costa
"""

import os as aqv
import pandas as pd

cd = pd.read_csv('.')


listArchives = aqv.listdir('.')
listArchives.remove("sem título0.py")
listArchives.remove("coord_bio.csv")


for archive in listArchives:
############################################ ADICIONANDO O BIOMA ############################################

    df = pd.read_csv(archive)
    for i in range(len(cd)):
        for ia in range(len(df)):
            if df.loc[ia, 'Latitude'] == cd.loc[i, 'lat'] and df.loc[ia, 'Longitude'] == cd.loc[i, 'lon']:
                df['Bioma'] = cd.loc[i,'Bioma']
                df.to_csv(archive, index = False)
                