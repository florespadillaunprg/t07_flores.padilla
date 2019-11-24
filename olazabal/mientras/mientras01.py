# Mostrae la edad de mi mama (50 o 60)

import os

edad=int(os.sys.argv[1])
edad_invalida=True

while( edad_invalida):
    edad=int(input("edad de mi mama (50/60):"))
    edad_invalida=(edad==50 and edad==60)
# fin_while

print("fin del bucle")
print("La respuesta es:", edad)

