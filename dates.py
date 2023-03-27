#Uso de fechas en python

#importacion de modulos
from datetime import date

this_day = date.today()

print(this_day)

#Al usar el operador "+" con dos tipos de datos que no son strings se obtendra un error, se tiene que convertir el otro tipo de dato a string de la siguiente manera
print("Today's date is " + str(this_day))