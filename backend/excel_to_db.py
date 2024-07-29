import pandas as pd
from pymongo import MongoClient
import os
from procesos import subirOt

root = "./files/" 
def generarJSON(filename):
    read_from = root + filename
    data = pd.read_excel(read_from)
    df = pd.DataFrame(data, columns=["Solicitante", "Descripción"])
    diccionary = df.to_dict(orient='records')
    return diccionary

def subirOt(filename):
    conn = MongoClient('mongodb+srv://paulo:Paulo2023@cluster0.prraayx.mongodb.net/ObrasDev?retryWrites=true&w=majority')
    db = conn['ObrasDev']
    name_colection = 'ots'
    colection = db[name_colection]
    diccionary = generarJSON(filename)
    if diccionary:
        res = colection.insert_many(diccionary)
    read_from = root + filename
    os.remove(read_from)

if __name__ == "__main__":
    subirOt()