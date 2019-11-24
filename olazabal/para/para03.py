# Decodificar mi codigo de la universidad
# a=numeros
# b=letra

import os

# input
a=os.sys.argv[1]
b=os.sys.argv[2]

codigo="ab"

# Iterador
for letra in codigo:
    if letra == "a":
        print("192025")
    if letra == "b":
        print("h")
#fin de iterador

print("Fin del bucle")
