# Decodificar mi fecha de bautizo y en que iglesia
# d=dia
# m=mes
# a=anio
# i=nombre de la iglesia

import os

# input
d=os.sys.argv[1]
m=os.sys.argv[2]
a=os.sys.argv[3]
i=os.sys.argv[4]

fecha_de_bautizo="dmai"

# Iterador
for letra in fecha_de_bautizo:
    if letra == "d":
        print("02")
    if letra == "m":
        print("enero")
    if letra == "a":
        print("2002")
    if letra == "i":
        print("Iglesia Santo Pedro-Apostol")
#fin de iterador

print("Fin del bucle")
