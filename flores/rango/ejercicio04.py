# Imprimir los numeros que se encuentran en cierto rango de w y z

import os

# input
w=int(os.sys.argv[1])
z=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",w,"hasta el",z)
print("Luego multiplicar a cada uno 5")
print("Luego multiplicar a cada uno 15")
print("Luego multiplicar a cada uno 25")
print("La respuesta es:")

# iterador_rango
resultado1=[]
resultado2=[]
resultado3=[]

for multipicacion in range(w,z):
    multiplicar_por_cinco=(multipicacion * 5)
    resultado1.append(multiplicar_por_cinco)
    multiplicar_por_quince=(multipicacion * 15)
    resultado2.append(multiplicar_por_quince)
    multiplicar_por_veinticinco=(multipicacion * 25)
    resultado3.append(multiplicar_por_veinticinco)

print("El resultado primero es:",resultado1)
print("El resultado segundo es:",resultado2)
print("El resultado tercero es:",resultado3)

# fin_iterador_en_rango

print("Fin de bucle")
