# Imprimir los numeros que se encuentran en cierto rango de f y p

import os

# input
f=int(os.sys.argv[1])
p=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",f,"hasta el",p)
print("Lego restarle a cada uno 2")
print("La respuesta es:")

# iterador_rango
resultado=[]

for resta in range(f,p):
    resta_menos_dos=(resta - 2)
    resultado.append(resta_menos_dos)

print("El resultado primero es:",resultado)

# fin_iterador_en_rango

print("Fin de bucle")
