# Decodificar la estructura del peru
# c=centro poblado
# d=distrito
# p=provincia
# r=departamento
# n=nacion

import os

# input
c=os.sys.argv[1]
d=os.sys.argv[2]
p=os.sys.argv[3]
r=os.sys.argv[4]
n=os.sys.argv[5]

estructura_del_peru="cdprn"

# Iterador
for letra in estructura_del_peru:
    if letra == "c":
        print("Nuevo San Lorenzo")
    if letra == "d":
        print("Jose Leonardo Ortiz")
    if letra == "p":
        print("Chiclayo")
    if letra == "r":
        print("Lambayeque")
    if letra == "n":
        print("Todo esta parte pertenece a la nacion del Peru")
#fin de iterador

print("Fin del bucle")
