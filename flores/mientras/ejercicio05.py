# Validar el precio de una computadora

import os

precio_de_computadora=float(os.sys.argv[1])
precio_valido=(precio_de_computadora<500.65 or precio_de_computadora>1000.65)

while( precio_valido==True):
    precio_de_computadora=float(input("Ingrese precio:"))
    precio_valido=(precio_de_computadora<500.65 or precio_de_computadora>1000.65)
# fin_while

print("fin del bucle")
print("La respuesta es:", precio_de_computadora,"dolares")
