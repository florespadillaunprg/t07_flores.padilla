# Decifrar los datos personales del ingeniero electronico
# a= nombre completo
# b= edad
# c=sexo
# d=fecha de nacimiento
# e=ciudad actual

import os

# input
a=os.sys.argv[1]
b=os.sys.argv[2]
c=os.sys.argv[3]
d=os.sys.argv[4]
e=os.sys.argv[5]

datos_personales="abcde"

# Iterador
for letra in datos_personales:
    if letra == "a":
        print("Juan Zurita Ramos")
    if letra == "b":
        print("35 anos")
    if letra == "c":
        print("masculino")
    if letra == "d":
        print("23/07/1985")
    if letra == "e":
        print("Trujillo")
#fin de iterador

print("Fin del bucle")
