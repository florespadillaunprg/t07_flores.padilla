# Validar la hora en la que almuerzo

import os

hora_de_almuerzo=float(os.sys.argv[1])
hora_invalida=(hora_de_almuerzo<1.00 or hora_de_almuerzo>2.30)

while( hora_invalida==True):
    hora_de_almuerzo=float(input("Ingrese hora:"))
    hora_invalida=(hora_de_almuerzo<1.00 or hora_de_almuerzo>2.30)
# fin_while

print("fin del bucle")
print("La respuesta es:", hora_de_almuerzo,"pm")
