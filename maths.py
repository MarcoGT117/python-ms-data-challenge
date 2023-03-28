#Se admiten las 4 operaciones basicas + - * /
#La operacion "division de multiplo inferior" redondea hacia abajo una divison, se usa "//", pe
seconds = 1042
minutes = seconds/60 #17.3666667
minutes_rounded = seconds//60 # 17

#El operador modulo regresa el resto de una division, es "%"
#pe, si desearamos obtener el numero de segundos restantes de la operacion anterior
leftover_seconds = 1042 % 60 #Es el restante de dividir 1042/60, en este caso, 22
clock = f"{seconds} seconds is equal to {minutes_rounded}:{leftover_seconds}"
print(clock)

#Strings a numeros
#int() puede recibir como argumeto un string el cual sera convertido en un entero, float() hara lo mismo pero para decimales
string_int = int('253') #253
string_float = float('253.3') #253.3

print(float('253')) #253.0

#los valores absolutos son aquellos que no son negativos sin su signo, se pueden crear usando abs()
print(abs(39 - 16)) #23
print(abs(16 - 39)) #23

#round() redondea el valor
print(round(13.6)) #14

#la libreria math tambien permite hacer estas y otras operaciones, por ejemplo roof() redondea el numero hacia arriba y floor() hacia abajo

from math import ceil, floor

print(floor(12.5)) #12
print(ceil(12.5)) #13

#
