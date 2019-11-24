# Validar la marca de mi celular

import os

marca=os.sys.argv[1]
marca_invalida=True

while( marca_invalida):
    marca=input("Ingrese la marca de celular:")
    marca_invalida=(marca!="sansumg" and marca!="verikoll" and marca!="nokia" and marca!="sony")
# fin_while

print("fin del bucle")
print("La respuesta es:", marca_invalida)
