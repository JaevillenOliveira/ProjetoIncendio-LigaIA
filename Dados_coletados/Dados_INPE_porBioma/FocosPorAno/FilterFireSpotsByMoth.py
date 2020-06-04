# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# =============================================================================
# This script gets the fire spots of each biome by year and splits it by month 
# ============================================================================= 

import pandas as pd

def func0():   
    biomes = ["Amazonia", "Caatinga", "Cerrado", "MataAtlantica", "Pampa", "Pantanal"]
    for b in biomes:
        print('b')
        for beginningYear in range (2016, 2019):
            # Name pattern Focos'Biome'_'beginningYear'-'endingYear'.csv
            InFileName = 'Focos'+b+'_'+str(beginningYear)+'-'+str(beginningYear+1)+'.csv' 
            inputFile = pd.read_csv(InFileName, usecols=['datahora', 'diasemchuva', 'precipitacao', 'riscofogo', 'latitude', 'longitude'])
            
            outFileName = 'FocosPorMes/Focos'+b+'_'+str(beginningYear)+'_'+str(12)+'.csv' 
            func1(inputFile, beginningYear, 12, outFileName)
            for month in range (1, 12):
                if(month < 10):
                    outFileName = 'FocosPorMes/Focos'+b+'_'+str(beginningYear+1)+'_'+'0'+str(month)+'.csv' 
                else:
                    outFileName = 'FocosPorMes/Focos'+b+'_'+str(beginningYear+1)+'_'+str(month)+'.csv' 
                func1(inputFile, beginningYear+1, month, outFileName)
                
        
def func1(inputFile, year, month, outFileName):
    if(month < 10):
        out = inputFile[(inputFile.datahora.str.startswith(str(year)+'/'+'0'+str(month)))]
    else:
        out = inputFile[(inputFile.datahora.str.startswith(str(year)+'/'+str(month)))]
    
    out.to_csv(outFileName, index=False)
            
func0()        
        
        
        
        
        
        
