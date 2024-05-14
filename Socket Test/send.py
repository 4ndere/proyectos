import os
import time
import glob
import shutil
import subprocess
import requests

while True:
    # Ejecuta el script de respaldo
    subprocess.run(['C:/script.bat'], shell=True)

    # Define la ruta al directorio de respaldos
    backup_dir = 'C:/Backups/'

    # Busca el archivo de respaldo más reciente
    list_of_files = glob.glob(backup_dir + '*.sql')  # Obtiene una lista de todos los archivos .sql
    latest_file = max(list_of_files, key=os.path.getctime)  # Encuentra el archivo más reciente

    # Define el destino en el servidor
    remote_filepath = '/var/www/html/Backus/' + os.path.basename(latest_file)

    # Copia el archivo al servidor
    shutil.copy(latest_file, remote_filepath)

    # Verifica que el archivo se haya copiado correctamente
    response = requests.get('http://localhost:8080/Backus/' + os.path.basename(latest_file))

    if response.status_code == 200:
        print('El archivo de respaldo se copió correctamente al servidor.')
    else:
        print('Hubo un error al copiar el archivo de respaldo al servidor.')

    # Espera un minuto antes de ejecutar la próxima iteración
    time.sleep(60)
