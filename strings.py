#En python las cadenas son inmutables, por lo que no se pueden modificar, por ejemplo al concatenar dos strings

fact = "There is no atmosphere in the moon"

fact + " In the moon there is no sound" #Esta operacion no alterara el string fact, si se quisiera mantener esta "modificacion" seria necesario almacenarla
print(fact) #Solo imprimira "There is no atmosphere in the moon"

fact2 = fact + ", In the moon there is no sound"
print(fact2) #Imprimira "There is no atmosphere, In the moon In the moon there is no sound"

#Para los strings se pueden usar comillas simples, dobles o triples. Combinelas segun la situacion lo requiera intentando mantener siempre la consistencia

string = """We only see about 60% of the Moon's surface, this is known as the "near side"."""

print(string)

#Metodos de los strings
string2 = "Temperatures and facts about the moon"
string2.title() #Cambia el primer caracter de cada palabra del string a mayusculas. Resultado 'Temperatures And Facts About The Moon'

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures.split() #Si el argumento esta vacio entonces separara en una lista los subelementos separados por espacios, si se le pasa un argumento, separara basado en el argumento

#El operador in regresa un booleano dependiendo de si encuentra el operando de la izquierda en el contenido del operando de la derecha (true si lo encuentra o false si no), es case sensitive

print("moon" in "This text will describe facts and challenges with space travel") #false

print("moon" in "This text will describe facts about the Moon") #false

print("Moon" in "This text will describe facts about the Moon") #true

#find() ayuda a buscar el indice de la posicion en que se encuentra el argumento siendo el primer caracter [0], si no lo encuentra regresa -1

temperatures2 = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(temperatures2.find("Moon")) #-1
print(temperatures2.find("Mars")) #64

#Al igual que con .title() se pueden usar los metodos .lower() y .upper() para pasar todos los caracteres del string a minusculas o mayusculas, respectivamente

print("The Moon And The Earth".lower()) #the moon and the earth

print("The Moon And The Earth".upper()) #THE MOON AND THE EARTH

#Los metodos startswith() y endswith() devuelven un booleano dependiendo de si el string al que se le aplica empieza o termina con el argumento que se le pasa al metodo

print("-60".startswith('-')) #true

if "30 C".endswith("C"): ##This temperature is in Celsius
    print("This temperature is in Celsius")

#El metodo .replace(a, b) reemplzara al argumento "a" con el contenido del argumento "b"
string3 = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(string3.replace("Celsius", "C")) #Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.

#El metodo .join() une metodos iterables (Como una lista) en un solo string
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print(" ".join(moon_facts)) #Se usa un espacio para unir los distintos elementos de la lista
#Salida -> 'The Moon is drifting away from the Earth.On average, the Moon is moving about 4cm every year'


#Se puede imprimir una variable en medio de un string usando el marcador %s
mass_percentage = 1/6
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage) #"On the Moon, you would weigh about 1/6 of your weight on Earth"

#Si se necesiatan mas de un valor se rodean los distintos valores en parentesis en orden, pe:
print("Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s." % ("Moon", "Earth", "Moon", "Earth"))

#Otra manera de obtener un resulato similar es con el metodo .format(), en este en vez de usar %s se usa {}

print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage)) #"On the Moon, you would weigh about 1/6 of your weight on Earth"

#Para sustituir por varios valores se pone entre las llaves el indice de los distintos argumentos de format()

print("Both sides of the {0} get the same amount of sunlight, but only one side is seen from {1} because the {0} rotates around its own axis when it orbits {1}.".format("Moon", "Earth")) 
                    #Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

#Para mejorar la legibilidad se pueden usar nombres de variables entre los {} y en los argumentos especificar los valores de estos
print("You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth".format(moon="Moon", mass=mass_percentage))
    #You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth


#A partir de python 3.6 se pueden usar f-strings, las cuales permiten incrustar variables o codigo en el string, lo que resulta aun mas legible, como ejemplo
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth") #"On the Moon, you would weigh about 1/6 of your weight on Earth"

subject = "interesting facts about the moon"
print(f"{subject.title()}") #Interesting Facts About The Moon