# Mostrar el nombre valido del arquero de la seleccion peruana

import os

nombre=os.sys.argv[1]
nombre_valido=True

while( nombre_valido):
    nombre=input("Ingrese el nombre:")
    nombre_valido=(nombre=="Pedro")
# fin_while

print("fin del bucle")
print("La respuesta es:", nombre)
