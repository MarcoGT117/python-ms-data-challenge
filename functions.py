#Para crear funciones en python se debe usar def antes del nombre de la funcion

def rocket_parts_none():
    print('payload, propellant, strucrture')

#Ejecutando la funcion
rocket_parts_none()

#Asignar la funcion a una variable
output = rocket_parts_none() #Devolvera un None, para evitar esto se puede añadir un return a la funcion

def rocket_parts():
    return 'payload, propellant, strucrture'

output = rocket_parts()

print(output)