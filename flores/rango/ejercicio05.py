# Imprimir los numeros que se encuentran en cierto rango de h y j

import os

# input
h=int(os.sys.argv[1])
j=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",h,"hasta el",j)
print("Luego dividir a cada uno 18")
print("Luego dividir a cada uno 9")
print("Luego dividir a cada uno 27")
print("La respuesta es:")

# iterador_rango
resultado1=[]
resultado2=[]
resultado3=[]

for division in range(h,j):
    dividir_entre_dieciocho=(division / 18)
    resultado1.append(dividir_entre_dieciocho)
    dividir_entre_nueve=(division / 9)
    resultado2.append(dividir_entre_nueve)
    dividir_entre_veintisiete=(division / 27)
    resultado3.append(dividir_entre_veintisiete)

print("El resultado primero es:",resultado1)
print("El resultado segundo es:",resultado2)
print("El resultado tercero es:",resultado3)

# fin_iterador_en_rango

print("Fin de bucle")
