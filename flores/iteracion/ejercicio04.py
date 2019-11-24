# Sumar los "b" primeros numeros multiplicados por su mismo numero (i*i)

import os

b=int(os.sys.argv[1])

i=1
suma=0

while(i<=b ):
    suma += i*i
    i += 1
#fin_while


print("La suma de los", b," primeros numeros multiplicados por su mismo numero (i*i) es:", suma)
