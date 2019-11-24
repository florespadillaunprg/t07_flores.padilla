# Imprimir los numeros que se encuentran en cierto rango de q y p

import os

# input
q=int(os.sys.argv[1])
p=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",q,"hasta el",p)
print("Luego restar a cada uno 20")
print("Luego restar a cada uno 40")
print("Luego restar a cada uno 60")
print("La respuesta es:")

# iterador_rango
resultado1=[]
resultado2=[]
resultado3=[]

for resta in range(q,p):
    resta_menos_veinte=(resta - 20)
    resultado1.append(resta_menos_veinte)
    resta_menos_cuarenta=(resta - 40)
    resultado2.append(resta_menos_cuarenta)
    resta_menos_sesenta=(resta - 60)
    resultado3.append(resta_menos_sesenta)

print("El resultado primero es:",resultado1)
print("El resultado segundo es:",resultado2)
print("El resultado tercero es:",resultado3)

# fin_iterador_en_rango

print("Fin de bucle")
