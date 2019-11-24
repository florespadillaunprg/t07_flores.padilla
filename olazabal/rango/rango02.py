# Imprimir los numeros que se encuentran en cierto rango de m e n

import os

# input
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",m,"hasta el",n)
print("Luego sumarle a cada uno mas 5")
print("La respuesta es:")

# iterador_rango
resultado=[]

for suma in range(m,n):
    suma_mas_cinco=(suma + 5)
    resultado.append(suma_mas_cinco)

print("El resultado primero es:",resultado)

# fin_iterador_en_rango
print("Fin del bucle")
