# Decodificar el nombre completo del presidente del peru y el anio que terminara su mandato
# n=nombre
# p= apellidp paterno
# m=apellido materno
# a=anio

import os

# input
n=os.sys.argv[1]
p=os.sys.argv[2]
m=os.sys.argv[3]
a=os.sys.argv[4]

datos_del_presidente="npma"

# Iterador
for letra in datos_del_presidente:
    if letra == "n":
        print("Martin")
    if letra == "p":
        print("Vizcarra")
    if letra == "m":
        print("Cornejo")
    if letra == "a":
        print("2021")
#fin de iterador

print("Fin del bucle")
