# USING LIST COMPREHENSIONS

valores = [91,41,9,2,95,338,189,9]


division = [num/39 for num in valores]

print(division)

print('\n')     # SALTO DE LINEA EN BLANCO

# VERSION COMPACTA

operador = []
for num in valores:
    division = num/39
    suma = division+19
    resta = suma - 8.7848
    multi = resta * 9.6
    operador.append(multi)
print(operador)

#Ej 3

miles = [100,57,93,44,80]

km = [value * 1.609 for value in miles]

#Ej 4

answers = [True, True, False, False, True]

opposite = []
for answer in answers:
    opposite.append(not answer)

print(opposite)

print([not answer for answer in answers])

#Ej 5

Mayor_de_edad =  [33,18,16,8,99,24,26]
can_enter = [age >= 18 for age in Mayor_de_edad] 

# Para copiar una lista
# Ej 5

copia = [dato for dato in Mayor_de_edad]


# Ej 6

Nombres = ["Carlos", "Chari", "Asustin", "Toño", "Arinta", "Valentina", "Marla"]
titulo = ["Ese mi lic " + nombre for nombre in Nombres]

# Ej 7

for name in Nombres:
    print(f"Saludos cordiales lic. {name}")

# Ej 8

words = ["Manzano", "Tago", "Vintro", "Amigi", "Weyi altepeŧ", "Aŧ","papanicolau"]
count_letter_d = [word.count("d") for word in words]
count_letter_a = [word.count("A") for word in words]

# La funcion de arriba es demasido específica, diferencia entre mayusculas y minúsculas "A" != "a"

# LO MISMO PERO CON FUNCIONES

#Ej 9

nombroj = [550,90,368,2,84,0.36]
def halve(num):
      return num/4

division = [halve(operacion) for operacion in nombroj]

#Ej 10 Se pueden hacer mas operaciones en las funciones

def multiple_operacion(dato):
    multi = 4.59 * dato
    resta = 24 - multi
    return resta + 2
operador = [multiple_operacion(num) for num in nombroj]

# Después de 'in' se agrega el nombre de la lista que se usará

#Ej 11

authors = ["Virgina Wolf", "John Steinbeck"]
def add_comma(between):
    parts = between.split("i")  # EN ESTA LÍNEA DE CODIGO SE INDICA EN QUE CARACTER SE VA A REALIZAR EL CORTE DE LA PALABRA
    return parts[1]+"?¿"+parts[0]   #EN ESTA LÍNEA SE COLOCA EL ORDEN EN EL QUE SE VAN A COLOCAR Y EL CARACTER QUE LOS SEPARARÁ
authors_update = [add_comma(between) for between in authors]



#Ej 12 REUSANDO LISTA PASADA 'words'


def doble_letra(palabra):
    count = palabra.count("a")
    return count == 3

doble_a = [doble_letra(palabra) for palabra in words]


#Ej 13

punktoj = [62, 90, 70, 60, 40]

def aprobado(final):
    extra = final + 39
    return extra > 90

calificaciones = [aprobado(final)for final in punktoj]

#Ej 14   REUSANDO LISTAS ANTERIORES

impresionanti = [dato for dato in valores if dato > 90]


#Ej 15 NO SALIÓ 

websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [retpagxo for retpagxo in websites if websites.count(".fr") >= 1] 

# Ej 16

ideal = [rango for rango in valores if rango >= 55 and rango <= 200]






