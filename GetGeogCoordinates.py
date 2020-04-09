import csv

pathToInputFile = '/home/jaevillen/IEEE/ForestFiresProject/FocosQueimadas2016-2019Shape/'
pathToOutputFile = '/home/jaevillen/IEEE/ForestFiresProject/FocosQueimadas2016-2019CSV/'

biome_layer = QgsVectorLayer("/home/jaevillen/IEEE/ForestFiresProject/Biomas/lm_bioma_250.shp", "biomas", "ogr")

def getBiomeGeom():
    for b in biome_layer.getFeatures():
        if(b['bioma'] == "Amazônia"):
            geomAmazonia = b.geometry()
        elif(b['bioma'] == "Caatinga"):
            geomCaatinga = b.geometry()
        elif(b['bioma'] == "Cerrado"): 
            geomCerrado = b.geometry()
        elif(b['bioma'] == "Mata Atlântica"):
            geomMataAtlantica = b.geometry()   
        elif(b['bioma'] == "Pampa"):
            geomPampa = b.geometry()  
        elif(b['bioma'] == "Pantanal"):
            geomPantanal = b.geometry()   

    caller(geomAmazonia,geomCaatinga,geomCerrado,geomMataAtlantica,geomPampa,geomPantanal)

def writeInFile(fire_spots_layer,geomAmazonia,geomCaatinga,geomCerrado,geomMataAtlantica,geomPampa,geomPantanal,pathToOutputFile): 
    with open(pathToOutputFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "LatitudeX", "LongitudeY", "Area", "Bioma"])
        for f in fire_spots_layer.getFeatures():
            geom = f.geometry()
            lat = geom.centroid().get().x()
            lon = geom.centroid().get().y()
            if(geomAmazonia.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Amazonia"])
            elif(geomCaatinga.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Caatinga"])
            elif(geomCerrado.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Cerrado"])
            elif(geomMataAtlantica.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Mata Atlantica"])
            elif(geomPampa.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Pampa"])
            elif(geomPantanal.contains(geom)):
                writer.writerow([f.id(), lat, lon, geom.area(), "Pantanal"])      

def caller(geomAmazonia,geomCaatinga,geomCerrado,geomMataAtlantica,geomPampa,geomPantanal):
    for ano in range (2018,2015, -1):
        print(ano)
        for mes in range (1,13):
            if (ano == 2019 & mes > 9):
                continue;
            else:
                if(mes < 10):
                    inputFileName = str(ano)+'_0'+str(mes)+'_aqm.shp'
                    outputFileName = str(ano)+'_0'+str(mes)+'_aqm.csv'
                else:
                    inputFileName = str(ano)+'_'+str(mes)+'_aqm.shp'
                    outputFileName = str(ano)+'_'+str(mes)+'_aqm.csv'
                print(pathToInputFile+inputFileName)
                fire_spots_layer = QgsVectorLayer(pathToInputFile+inputFileName, "focos", "ogr")
                writeInFile(fire_spots_layer,geomAmazonia,geomCaatinga,geomCerrado,geomMataAtlantica,geomPampa,geomPantanal,pathToOutputFile+outputFileName)
            
getBiomeGeom()