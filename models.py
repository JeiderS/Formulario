from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://jeidersilgado:#Jei123456@cluster0.oytvlfz.mongodb.net/"

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["Formulario"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
