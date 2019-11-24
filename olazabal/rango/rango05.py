# Imprimir los numeros que se encuentran en cierto rango de e y f

import os

# input
e=int(os.sys.argv[1])
f=int(os.sys.argv[2])

# ouput
print("Mostrar el intervalo que comienze desde el",e,"hasta el",f)
print("Luego dividir a cada una entre 10")
print("La respuesta es:")

# iterador_rango
resultado=[]

for dividir in range(e,f):
    dividir_entre_diez=(dividir / 10)
    resultado.append(dividir_entre_diez)

print("El resultado primero es:",resultado)

# fin_iterador_en_rango

print("Fin de bucle")
