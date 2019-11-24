# Imprimir los numeros que se encuentran en cierto rango de s y t

import os

# input
s=int(os.sys.argv[1])
t=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",s,"hasta el",t)
print("Luego sumar a cada uno 10")
print("Luego sumar a cada uno 100")
print("Luego sumar a cada uno 1000")
print("La respuesta es:")

# iterador_rango
resultado1=[]
resultado2=[]
resultado3=[]

for suma in range(s,t):
    suma_mas_diez=(suma + 10)
    resultado1.append(suma_mas_diez)
    suma_mas_cien=(suma + 100)
    resultado2.append(suma_mas_cien)
    suma_mas_mil=(suma + 1000)
    resultado3.append(suma_mas_mil)

print("El resultado primero es:",resultado1)
print("El resultado segundo es:",resultado2)
print("El resultado tercero es:",resultado3)

# fin_iterador_en_rango

print("Fin de bucle")
