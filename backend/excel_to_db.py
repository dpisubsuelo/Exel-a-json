import pandas as pd
from pymongo import MongoClient
import os

root = "./files/" 
def generarJSON(filename):
    read_from = root + filename
    data = pd.read_excel(read_from)
    df = pd.DataFrame(data, columns=["Fecha", "Descripción", "Monto"])
    diccionary = df.to_dict(orient='records')
    return diccionary

def subirOt(filename):
    conn = MongoClient('mongodb+srv://dpisubuselo:dpimongo@clusterdpi.fyfnnlv.mongodb.net/?retryWrites=true&w=majority&appName=Clusterdpi')
    db = conn['Prueba-excel']
    name_colection = 'excel'
    colection = db[name_colection]
    diccionary = generarJSON(filename)
    if diccionary:
        res = colection.insert_many(diccionary)
        print("Se insertaron correctamente los registros", diccionary)
    # read_from = root + filename
    # os.remove(read_from)

if __name__ == "__main__":
    subirOt("Control_de_Gastos.xlsx")