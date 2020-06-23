# -*- coding: utf-8 -*-
"""
@author: Adlla Aragão e Daniel Costa
"""
import os as aqv
import json
import pandas as pd
from math import sqrt, pi
from functools import partial
import pyproj
from shapely.geometry import Point
from shapely.ops import transform

arquivosEstacao = aqv.listdir('.\\Dados_coletados\\Dados Meteorológicos')
with open('PathsToFiles.json') as datafile:
    # esse json contém os caminhos pra cada dataset, podendo achar o foco
    # e o aqm com a chave ano e mês
    arquivosFocoQmd = json.load(datafile)

def main():
    for estacao in arquivosEstacao:
        for ano in range(2016, 2020):
            for mes in range(1, 13):

                strmes = mesToStr(mes)
                pathAqm = getPath(str(ano), strmes, 'aqm')
                pathFoco = getPath(str(ano), strmes, 'foco')
                df_Aqm = pd.read_csv(pathAqm)
                df_Foco = pd.read_csv(pathFoco)

                df_Estacao = pd.read_csv(estacao)
                for i in range(0, len(df_Estacao)):
                    dataEstacao = df_Estacao.loc[i].Data.split('/')

                    # verificação das datas
                    if(dataEstacao[1] == mes and dataEstacao[2] == ano):
                        aqmFoco(df_Aqm, df_Estacao, i)
                        aqmFoco(df_Foco, df_Estacao, i)
                        

def aqmFoco(df_aqmFoco, df_Estacao, i):
    for j in range(0, len(df_aqmFoco)):
        if(df_aqmFoco.loc[j].bioma == df_Estacao.loc[i].Bioma):
            if(contem(df_Estacao.loc[i].Latitude, df_Estacao.loc[i].Longitude, df_aqmFoco.loc[j].latitude, df_aqmFoco.loc[j].longitude, df_Estacao.loc[i]['area(m²)'])):
                if(j == 0):
                    df_aqmFoco['direcaoVento'] = None
                    df_aqmFoco['velocidadeVentoMedia'] = None
                    df_aqmFoco['velocidadeVentoMaximaMedia'] = None
                    df_aqmFoco['insolacaoTotal'] = None
                    df_aqmFoco['nebulosidadeMedia'] = None
                    df_aqmFoco['numDiasPrecipitacao'] = None
                    df_aqmFoco['precipitacaoTotal'] = None
                    df_aqmFoco['tempMaximaMedia'] = None
                    df_aqmFoco['tempMinimaMedia'] = None
                    df_aqmFoco['umidadeRelativaMedia'] = None
                else:
                    df_aqmFoco.loc[j, 'direcaoVento'] = df_Estacao.loc[i].DirecaoVento
                    df_aqmFoco.loc[j, 'velocidadeVentoMedia'] = df_Estacao.loc[i].VelocidadeVentoMedia
                    df_aqmFoco.loc[j, 'velocidadeVentoMaximaMedia'] = df_Estacao.loc[i].VelocidadeVentoMaximaMedia
                    df_aqmFoco.loc[j, 'insolacaoTotal'] = df_Estacao.loc[i].InsolacaoTotal
                    df_aqmFoco.loc[j, 'nebulosidadeMedia'] = df_Estacao.loc[i].NebulosidadeMedia
                    df_aqmFoco.loc[j, 'numDiasPrecipitacao'] = df_Estacao.loc[i].NumDiasPrecipitacao
                    df_aqmFoco.loc[j, 'precipitacaoTotal'] = df_Estacao.loc[i].PrecipitacaoTotal
                    df_aqmFoco.loc[j, 'tempMaximaMedia'] = df_Estacao.loc[i].TempMaximaMedia
                    df_aqmFoco.loc[j, 'tempMinimaMedia'] = df_Estacao.loc[i].TempMinimaMedia
                    df_aqmFoco.loc[j, 'umidadeRelativaMedia'] = df_Estacao.loc[i].UmidadeRelativaMedia
                        
def getPath(ano, mes, tipo):
    try:
        return arquivosFocoQmd[ano][mes][tipo]
    except:
        return None


def mesToStr(mes):
    if mes < 10:
        return '0' + str(mes)
    else:
        return str(mes)


# Utilizando a área total da cidade para calcular o raio da mesma
def calcular_raio(area):
    # Calculando o valor o raio utilizando a área total da cidade
    aux = area/pi
    raio = sqrt(aux)

    return raio


# Verifica se determinadas coordenadas estão contidas no círculo da cidade
def contem_area(lat_focoQmd, long_focoQmd, circle):
    # Cria ponto com as coordenadas do foco ou da queimada
    ponto = Point(lat_focoQmd, long_focoQmd)

    return circle.contains(ponto)


# Cria o círculo da cidade e faz a verificação, retornando 'True' ou 'False'
def contem(lat_estacao, long_estacao, lat_focoQmd, long_focoQmd, area):
    lat, lon = lat_estacao, long_estacao  # Coordenadas da estação
    # Utiliza a área da cidade para calcular o raio dela
    radius = calcular_raio(area)

    local_azimuthal_projection = "+proj=aeqd +R=6371000 +units=m +lat_0={} +lon_0={}".format(
        lat, lon
    )
    wgs84_to_aeqd = partial(
        pyproj.transform,
        pyproj.Proj("+proj=longlat +datum=WGS84 +no_defs"),
        pyproj.Proj(local_azimuthal_projection),
    )
    aeqd_to_wgs84 = partial(
        pyproj.transform,
        pyproj.Proj(local_azimuthal_projection),
        pyproj.Proj("+proj=longlat +datum=WGS84 +no_defs"),
    )

    center = Point(float(lon), float(lat))
    point_transformed = transform(wgs84_to_aeqd, center)
    buffer = point_transformed.buffer(radius)
    # Get the polygon with lat lon coordinates
    circle_poly = transform(aeqd_to_wgs84, buffer)  # Círculo contendo a cidade

    return contem_area(lat_focoQmd, long_focoQmd, circle_poly)
