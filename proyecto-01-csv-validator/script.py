import csv

# Abrimos el archivo CSV en modo lectura
with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    
    # Saltamos la primera fila (el encabezado: nombre,edad,email)
    next(lector)
    
    # Contamos las filas de datos
    contador = 0
    for fila in lector:
        contador += 1
    
    # Mostramos el resultado
    print("Total de registros:", contador)