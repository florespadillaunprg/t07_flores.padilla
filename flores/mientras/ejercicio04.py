# Validar el nombre de mi hermano mayor

import os

nombre=os.sys.argv[1]
nombre_invalido=True

while( nombre_invalido):
    nombre=input("Ingrese nombre:")
    nombre_invalido=(nombre!="Juan" and nombre!="Jose"
                     and nombre!="Lucas" and nombre!="Pedro"
                     and nombre!="Leonardo" and nombre!="Roberto"
                     and nombre!="Rodrigo" and nombre!="Alex"
                     and nombre!="Ricardo" and nombre!="Esteban")
# fin_while

print("fin del bucle")
print("La respuesta es:", nombre)
