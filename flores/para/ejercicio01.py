# Decifrar el mensaje bloqueado

import os

# input
a=os.sys.argv[1]
l=os.sys.argv[2]
e=os.sys.argv[3]
x=os.sys.argv[4]

msg="alex"

# Iterador
for letra in msg:
    if letra == "a":
        print("Buenos dias")
    if letra == "l":
        print("¿ como estas ?")
    if letra == "e":
        print("¡salimos a cenar esta tarde!")
    if letra == "x":
        print("Te espero a las 5:00 pm")
#fin de iterador

print("Fin del bucle")
