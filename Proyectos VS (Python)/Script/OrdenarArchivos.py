"""Molde para ordenar archivos una vez que se tenga una RUTA, colocar donde corresponda para que sea parametro en las funciones"""
import os
import shutil

"""defino los distintos formatos que se pueden encontrar en el arhivo"""
EXTENSIONES = {
    "Imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
}

def organizar_carpeta(ruta):
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            movido = False

            for carpeta, extensiones in EXTENSIONES.items():
                if extension in extensiones:
                    destino = os.path.join(ruta, carpeta)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(ruta_archivo, destino)
                    movido = True
                    break

            if not movido:
                destino = os.path.join(ruta, "Otros")
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_archivo, destino)

if __name__ == "__main__":
    organizar_carpeta("C:/Users/TU_USUARIO/Downloads")
