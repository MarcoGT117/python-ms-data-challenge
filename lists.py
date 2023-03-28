#Una lista es una coleccion de valores, ser crean encerrando los valores en corchetes y separando cada valor con comas
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#A los elementos de la lista se accede mediante su indice, siendo el primer elemento el indice 0, por ende, el ultimo sera la longitud - 1, la longitud de la lista se puede encontrar usando len(nombre_lista)

print(f"the first planet is {planets[0]}")
print(f"the third planet is {planets[2]}")
print(f"the last planet is {planets[len(planets)-1]}")

#Mediante esa notacion tambien se puede modificar el valor de uno de los elementos de la lista
#planets[3] = "Red Planet"
#print("Mars is also known as", planets[3]) 

#Se pueden agregar nuevos valores usando el metodo .append(valor_nuevo), esto lo añadira al final de la lista, las listas son dinamicas, creceran o decreceran dependiendo de sus elementops
print(len(planets)) # 8
planets.append("Nuevo valor")
print(len(planets)) # 9

#Usar .pop() eliminara el ultimo elemento de la lista, si se le da un argumento eliminara el valor del indice dado
planets.pop()
print(planets)
print(len(planets)) # 8

#Se pueden usar indices negativos, por ejemplo, -1 devolveria el ultimo elemento, -2 el penultimo, -3 el antepenultimo, etc.
print(f"the last planet is {planets[-1]}")

#para encontrar el indice de un valor se puede usar el metodo .index("termino_de_busqueda"), si el elemento no es encontrado, devuelve -1
jupiter_index = planets.index("Jupiter") # 4

#Numeros en las listas
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth
print(f"A bus in the earth weights {bus_weight}kg, in {planets[0]} the same bus would weight {bus_weight * gravity_on_planets[0]}kg")

#min() y max() devuelven el valor mas pequeño y mas grande de una lista, respectivamente
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

#Se pueden segmentar los valores de una lista para recuperar una serie de valores de esta, para eso use lista[a: b], siendo a el valor inicial de la lista y b el valor hasta el que quiere llegar

planets_before_earth = planets[0:2]
print(planets_before_earth) #'Mercury', 'Venus'
planets_after_earth = planets[3:8]
print(planets_after_earth) #'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
#Si no se pone un valor despues del doble punto entonces se ira hasta el ultimo elemento de la lista

#Se pueden unir dos listas usando "+"
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#el metodo .sort() ordena los elementos de la lista, si son elementos string lo hara en orden alfabetico, si son numeros, lo hara de mayor a menor
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter (in alphabetical order) are", regular_satellite_moons)
#Si se pone como argumetio reverse=True al metodo sort los ordenara inversamente
