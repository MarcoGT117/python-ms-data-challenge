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

#print(output)

#Funciones con argumentos

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
#Si se ejecuta sin un argumento arrojara un error

#Argumentos variables, permite pasar cualquier numero de argumentos, se pone un "*"
def variable_length(*args):
    print(args) #Imprime todos los valores pasados como argumentos

def sequence_time(*args):
   total_minutes = sum(args)
   if total_minutes < 60:
       return f"Total time to launch is {total_minutes} minutes"
   else:
       return f"Total time to launch is {total_minutes/60} hours"

#Funciones variables de palabras clave
def variable_keys_length(**kwargs):
    print(kwargs)

variable_keys_length(tanks=1, day="Wednesday", pilots=3) #Regresa los valores e forma de diccionario, por lo que se pueden realizar todas las mismas operaciones de los diccionarios

#Nueva funcion
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
