# Imprimir los numeros que se encuentran en cierto rango de a y b

import os

# input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",a,"hasta el",b )
print("Luego a cada uno sumarle 2")
print("La respuesta es:")

# iterador_rango

for suma in range(a,b):
    print(suma +2)
# fin_iterador_en_rango

print("Fin de bucle")
