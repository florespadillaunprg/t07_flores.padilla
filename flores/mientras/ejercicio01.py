# mostrar mensaje "Hola, ¿como estas?" bien o mal.

import os

respuesta=os.sys.argv[1]
respuesta_invalida=True

while( respuesta_invalida):
    respuesta=input("Ingrese respuesta:")
    respuesta_invalida=(respuesta!="bien" and respuesta!="mal")
# fin_while

print("fin del bucle")
print("La respuesta es:", respuesta)
