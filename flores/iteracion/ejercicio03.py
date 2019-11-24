# Sumar los "p" primeros numeros al cuadrado cada uno

import os

p=int(os.sys.argv[1])

i=1
suma=0

while(i<=p ):
    suma += i**2
    i += 1
#fin_while

print("La suma de los", p,"primeros numeros al cuadrado es:", suma)

