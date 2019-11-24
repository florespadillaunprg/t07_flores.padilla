# Mostrar el peso en una persona en kg

import os

peso=float(os.sys.argv[1])
peso_invalido=(peso<50.4 or peso>80.96)


while(peso_invalido == True):
    peso=float(input("Ingrese peso:"))
    peso_invalido=(peso<50.4 or peso>80.96)
#fin_while

print("Fin del bucle")
print("La respuesta es :", peso)
