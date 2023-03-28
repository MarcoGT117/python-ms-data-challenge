#en python los if se ejecutan en base a la sangria del codigo
"""
a = 24
b = 44
if a <= 0:
    print(a) #La condcion del if es falsa, por lo que print(a) no se ejecutara
print(b) #Esta instruccion esta fuera de la sangria del if, por lo que se ejecutara independientemente de la condicion del if
"""

#Para un if-else la estructura es la siguiente 

a = 93
b = 27

"""
if a >= b:
    print(a)
else:
    print(b) #Recuerda respetar la sangria para que se ejecuten las instrucciones deseadas
"""

#Para statements else-if se usa la abreviacion "elif"
"""
if a >= b:
    print("a is greater or equal to b")
elif a == b:
    print("a is equal to b")
"""

#Se pueden combinar con una instruccion final del tipo else

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b") 

#Se pueden anidar if, elif y else para crear estructuras logicas mas complejas

c = 16
d = 25
e = 27

if c > d:
    if d > e:
        print("c is greather than d and d is greater than e")
    else:
        print("c is grather than d and lesser than e")
elif c == d:
    print("c is equal to d")
else:
    print("c is lesser than d")