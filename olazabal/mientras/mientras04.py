# Mostrar el nombre del anio actual

import os

anio=os.sys.argv[1]
anio_valido=True

while( anio_valido):
    anio=input("Ingrese nombre del anio:")
    anio_valido=(anio=="anio de la lucha contra la corrupcion e impunidad")
# fin_while

print("fin del bucle")
print("La respuesta es:", anio)
