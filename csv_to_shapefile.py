# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:52:09 2020

@author: Daniel Costa
"""

import geopandas
from shapely.geometry import Point
import pandas as pd


df = pd.read_csv('coordenadas2.csv')


# combine lat and lon column to a shapely Point() object
df['geometry'] = df.apply(lambda x: Point((float(x.lat), float(x.lon))), axis=1)

df = geopandas.GeoDataFrame(df, geometry='geometry')

df.to_file('MyGeometries.shp', driver='ESRI Shapefile')