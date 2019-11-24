# Imprimir los numeros que se encuentran en cierto rango de l y k

import os

# input
l=int(os.sys.argv[1])
k=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",l,"hasta el",k)
print("Luego multiplicar a cada uno por 3")
print("La respuesta es:")

# iterador_rango
resultado=[]

for multiplicar in range(l,k):
    multiplicar_por_tres=(multiplicar * 3)
    resultado.append(multiplicar_por_tres)

print("El resultado primero es:",resultado)

# fin_iterador_en_rango

print("Fin de bucle")
