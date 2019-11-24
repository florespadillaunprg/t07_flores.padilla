# Validar el precio de un televisor

import os

precio_del_televisor=float(os.sys.argv[1])
precio_invalido=(precio_del_televisor<400.2 or precio_del_televisor>550.21)


while( precio_invalido==True):
    precio_del_televisor=float(input("Ingrese precio del televisor:"))
    precio_invalido=(precio_del_televisor<400.2 or precio_del_televisor>550.21)
# fin_while

print("fin del bucle")
print("La respuesta es:", precio_del_televisor, "dolares")
