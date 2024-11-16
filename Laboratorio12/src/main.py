# UNIVERSIDAD DEL VALLE DE GUATEMALA
# Teoria de la Computación
# Gabriel Alberto Paz Gonzalez 221087
# Fecha 15-11-2024

from pprint import pprint

print(" -------------------- INICIO --------------------------")

# EJERCICIO 1: Escribir un programa en Python (o Haskell para puntos extra) que ordene una lista de diccionarios
print("-------------- EJERCICIO 1 ----------------")
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}         
]
res = sorted(D, key=lambda x: x['make'])
pprint(res)

# EJERCICIO 2:  Escribir un programa en Python (o Haskell para puntos extra) que calcule la potencia n-esima de cada elemento en una lista de enteros, usando funciones lambda
print("\n ----------------- EJERCICIO 2 ------------------")
potencia = 4
num = [1,2,3,4,5,6,7,8,9,10]

res = list(map(lambda x: x**potencia, num))

print(res)

# EJERCICIO 3:  Escribir un programa en Python (o Haskell para puntos extra) que calcule la matriz transpuesta XT, usando funciones lambda.
print("\n ------------------- EJERCICIO 3 ----------------------")
X = [
    [1,2,3,1],
    [4,5,6,0],
    [7,8,9,-1]
]

res = list(map(lambda x: list(x), zip(*X)))

for i in res:
    print(i)

# EJERCICIO 4:  Escribir un programa en Python (o Haskell para puntos extra) que elimine elementos indicados de una lista, usando las funciones lambda. Aquí los elementos a borrar también deben indicarse como una lista, y la salida debe ser la lista elementos remanentes.
print("\n ------------------- EJERCICIO 4 ----------------------------")
colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', ' negro']
elementos = ['rojo, verde', 'azul', 'gris', 'negro']

res = lambda colores, elementos: list(filter(lambda x: x not in elementos, colores))
print(res(colores, elementos))

print(" ---------------------- FINAL ----------------------")