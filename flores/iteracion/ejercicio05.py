# Sumar los "y" primeros numeros impares elevados al cubo y divididos entre 2

import os

y=int(os.sys.argv[1])

i=1
suma=0

while(i<=y ):
    suma += (i**3)/2
    i += 1
#fin_while


print("La suma de los", y," primeros elevados al cubo y divididos entre dos es:", suma)
