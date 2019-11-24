# Decodificar la contrasena de mi celular
# a=mi nombre
# b=mi dni
# c=mi numero de celular

import os

# input
a=os.sys.argv[1]
b=os.sys.argv[2]
c=os.sys.argv[3]

contrasena="abc"

# Iterador
for letra in contrasena:
    if letra == "a":
        print("Alex")
    if letra == "b":
        print("71580572")
    if letra == "c":
        print("974354085")
#fin de iterador

print("Fin del bucle")
