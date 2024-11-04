import os
import shutil
from collections import Counter

def contar_y_eliminar_imagenes(path_carpeta):
    # Tipos de archivos de imagen
    extensiones_imagen = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    
    # Contador de imágenes por carpeta
    contador_imagenes = {}
    
    # Recorrer todas las subcarpetas
    for root, _, files in os.walk(path_carpeta):
        # Contar solo los archivos que sean imágenes
        cantidad_imagenes = sum(1 for file in files if os.path.splitext(file)[1].lower() in extensiones_imagen)
        if cantidad_imagenes > 0:
            contador_imagenes[root] = cantidad_imagenes
    
    # Obtener las 20 carpetas con más imágenes
    top_20_carpetas = set([carpeta for carpeta, _ in Counter(contador_imagenes).most_common(20)])
    
    # Eliminar las carpetas que no están en el top 20
    for carpeta in contador_imagenes:
        if carpeta not in top_20_carpetas:
            shutil.rmtree(carpeta)
            print(f"Carpeta eliminada: {carpeta}")
    
    # Imprimir las 20 carpetas con más imágenes
    for carpeta in top_20_carpetas:
        print(f"{carpeta}: {contador_imagenes[carpeta]} imágenes")

# Ejemplo de uso
path = "/Users/bryan.campos/Documents/Bryan/IA/IA_Proyeto_3/archive/train"  # Reemplaza por la ruta de tu carpeta
contar_y_eliminar_imagenes(path)
