#Se puede pedir al usuario que ponga los datos drante la ejecucion del programa de la siguiente manera

print("Welcome to the greeting program")
name = input("Please enter yout name: " )
print("Hello " + name)

#input guarda los datos como string, si se requiere hacer operaciones matematicas hay que convertir ese string en algun data de tipo de numero, por ejemplo, con int()

print("Adding program")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print(int(first_number) + int(second_number))