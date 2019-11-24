# decodificar cada una de las notas
# a=nota01
# b=nota02
# c=nota03
# d=nota05

import os

# input
a=os.sys.argv[1]
b=os.sys.argv[2]
c=os.sys.argv[3]
d=os.sys.argv[4]

notas="abcd"

# Iterador
for letra in notas:
    if letra == "a":
        print("15")
    if letra == "b":
        print("12")
    if letra == "c":
        print("11")
    if letra == "d":
        print("16")
#fin de iterador

print("Fin del bucle")
