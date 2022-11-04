from pymongo import MongoClient
import json 
import certifi

CertificadoAutenticidad = certifi.where()

####################################
# Cargar el archivo de configuracion

def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

####################################
# Funcion de conexion

def dbConnection():
    dataConfig = loadConfigFile()
    try:
        #Conexion atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = CertificadoAutenticidad)
        #Conexion local
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["backend_resultados"]
    except ConnectionError:
        print("Error de conexion con la db")
    return db