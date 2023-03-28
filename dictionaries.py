#Los diccionarios de Python son variables es una coleccion de key-values contenidas en una sola varaible (Como los objetos)

planet ={
    'name' : 'Earth',
    'moons' : 1
}

#Hay dos maneras de obtener los datos de un diccionario

print(planet.get('name'))

print(planet['name']) #Ambos regresan el mismo resultado, pero este es el mas comun
#Cuando la key especificada no existe el metodo get regresa 'None' mientras que el eso de corchetes regresa 'KeyError'

#Al igual existen dos metodos para actualizar los datos de un diccionario, 
#Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

#Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79
#Ambas son validas, la diferencia es que update permite actualizar varias keys a la vez mientras que con corchetes se tiene que hacer una actulizacion a la vez

#Para añadir keys con un value use
planet['orbital period'] = 4333

#Para quitar una llave y su valor use el metodo pop, este metodo ademas de eliminar la key devuelve el valor quie esta contenia
removed_item = planet.pop('orbital period')
print(removed_item)
print(planet) #Aqui la key ya ha sido eliminada

#Se pueden crear o añadir diccionarios que contengan mas diccionarios
planet['diameter_(km)'] = {
    'polar' : 133709,
    'equatorial' : 142984
}

#Para recuperar los datos de diccionarios anidados
print(planet['diameter_(km)']['polar'])
#Con un poco de formato
print(f"Planet name: {planet['name']} | Equatorial diameter: {planet['diameter_(km)']['equatorial']}")


