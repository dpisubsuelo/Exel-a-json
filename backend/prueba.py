from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import excel_to_db
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/uploadfile/')
async def create_upload_file(file_upload: UploadFile):
    data = await file_upload.read()
    UPLOAD_DIR = "./files"
    save_to = UPLOAD_DIR + "/" + file_upload.filename
    with open(save_to, 'wb') as f:
        f.write(data)

    # Verificar la existencia del archivo
    if os.path.exists(save_to):
        print("El archivo se grabó correctamente.")
        # Leer y verificar el contenido del archivo
        with open(save_to, 'rb') as f:
            contenido = f.read()
            if contenido == data:
                print("El contenido del archivo es correcto.")
                #Insertarlo en la base de datos
                excel_to_db.subirOt(file_upload.filename)
            else:
                print("El contenido del archivo no coincide con los datos escritos.")
    else:
        print("Error: El archivo no se pudo grabar.")
    
    return {"filenames": file_upload.filename}