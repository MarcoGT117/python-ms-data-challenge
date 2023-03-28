#Para recuperar todos los valores de un diccionario se usa el metodo keys()
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

#print(rainfall.keys())

#Para iterar los valores de las keys

for key in rainfall.keys():
    print(f"Precipitation in {key} = {rainfall[key]}cm")

#Para determinar si un valor existe se puede usar la palabra clavbe "in":
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1 #Ya que existe el valor, se actualizara a 3.1
else:
    rainfall['december'] = 1

#Se pueden recuperar solo los valores sin las keys con values()
total_rainfall = 0

for rain_value in rainfall.values():
    total_rainfall = rain_value + total_rainfall

print(f"There was a total rainfall of {total_rainfall} during the measured months")