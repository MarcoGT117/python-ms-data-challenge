#Se pueden usar argumentos para que el programa tome datos desde la consola al ejecutar dicho programa, pe:
# python3 backup.py 2023-01-01      |En este ejemplo el programa backup recibe como arguimento el string "2023-01-01", para hacer esto se necesita importar sys, pe

import sys

print(sys.argv)
print(sys.argv[0]) # esta posicion es el nombre del programa
print(sys.argv[1]) # este seria el primer argumento