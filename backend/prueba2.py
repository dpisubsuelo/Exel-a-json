import pandas as pd
from pymongo import MongoClient
import os

UPLOAD_DIR = "./files"
read_from = UPLOAD_DIR + r"/desde_summa.xlsx"

data = pd.read_excel(read_from)
df = pd.DataFrame(data, columns=["Solicitante", "Descripción"])
diccionary = df.to_dict(orient='records')
print(diccionary)

UPLOAD_DIR = "./files"
save_to = UPLOAD_DIR + r"/desde_summa.json"

with open(save_to, 'w', encoding='utf-8') as archivo:
    json.dump(diccionary, archivo, ensure_ascii=False, indent=4)

# Insertar en la base de datos

conn = MongoClient('mongodb+srv://paulo:Paulo2023@cluster0.prraayx.mongodb.net/ObrasDev?retryWrites=true&w=majority')
db = conn['ObrasDev']
name_colection = 'ots'

colection = db[name_colection]

# if diccionary:
#     res = colection.insert_many(diccionary)

os.remove(read_from)