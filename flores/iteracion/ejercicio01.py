# Sumar los "a" primeros numeros

import os

a=int(os.sys.argv[1])
i=0
suma=0

while(i<=a):
    suma += i
    i += 1
#fin_while

print("La suma de los", a," primeros numeros es:", suma)
