from pymongo import MongoClient
import pandas as pd

# Lee el archivo Excel
df = pd.read_excel('./Control_de_Gastos.xlsx')

# Muestra las primeras filas del DataFrame
print(df.head())

# Convierte el DataFrame a JSON
json_data = df.to_json(orient='records')

# Guarda el JSON en un archivo
# with open('./archivo.json', 'w') as json_file:
#     json_file.write(json_data)

# print("Conversión completa. El archivo JSON ha sido guardado.")
conn = MongoClient('mongodb+srv://dpisubuselo:dpimongo@clusterdpi.fyfnnlv.mongodb.net/?retryWrites=true&w=majority&appName=Clusterdpi')
db = conn['pruebaBg']
name_colection = 'Excel'
colection = db[name_colection]

colection.insert_many(df.to_dict('records'))

print("Conversión completa. Los datos han sido guardados en la base de datos.")