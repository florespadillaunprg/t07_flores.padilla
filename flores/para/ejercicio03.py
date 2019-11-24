# Decodificar la fecha de mi naciemto
# d=dia
# m=mes
# a=anio

import os

# input
dia=os.sys.argv[1]
mes=os.sys.argv[2]
anio=os.sys.argv[3]

fecha_de_naciemto="dma"

# Iterador
for letra in fecha_de_naciemto:
    if letra == "d":
        print("29")
    if letra == "m":
        print("julio")
    if letra == "a":
        print("2000")
# fin_iterador

print("Fin de bucle")
