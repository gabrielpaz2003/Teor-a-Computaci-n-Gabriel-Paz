
# Laboratorio No. 12 - Teoría de la Computación

## Universidad del Valle de Guatemala
### Ingeniería en Ciencias de la Computación y Tecnologías de la Información
**Estudiante:** Gabriel Alberto Paz Gonzalez  
**Carné:** 221087  
**Fecha:** 15-11-2024  

---

## Descripción

Este repositorio contiene la solución al **Laboratorio No. 12** del curso de Teoría de la Computación. El objetivo fue resolver cuatro ejercicios utilizando **Python** y **funciones lambda**, demostrando habilidades en programación funcional y manipulación de estructuras de datos.

---

## Ejercicios

### 1. Ordenar una lista de diccionarios
**Descripción:**  
Se ordena una lista de diccionarios según una clave indicada.  
**Función clave:** `sorted` con `lambda`.  
**Ejemplo de entrada:**
```python
[
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
```
**Ejemplo de salida:**
```python
[
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
```

---

### 2. Potencia n-ésima de elementos en una lista
**Descripción:**  
Se eleva cada elemento de una lista a una potencia `n`.  
**Función clave:** `map` con `lambda`.  
**Ejemplo de entrada:**
```python
num = [1, 2, 3, 4, 5]
potencia = 3
```
**Ejemplo de salida:**
```python
[1, 8, 27, 64, 125]
```

---

### 3. Calcular la matriz transpuesta
**Descripción:**  
Se calcula la transpuesta de una matriz representada como una lista de listas.  
**Función clave:** `zip` con `map`.  
**Ejemplo de entrada:**
```python
X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
**Ejemplo de salida:**
```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

---

### 4. Eliminar elementos de una lista
**Descripción:**  
Se eliminan elementos de una lista según otra lista de elementos a borrar.  
**Función clave:** `filter` con `lambda`.  
**Ejemplo de entrada:**
```python
colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris']
elementos = ['rojo', 'gris']
```
**Ejemplo de salida:**
```python
['verde', 'azul', 'amarillo']
```

---

## Instrucciones de uso

1. Clonar este repositorio en tu máquina local.
2. Ejecutar cada script correspondiente a los ejercicios en un entorno de Python 3.
3. Asegurarse de tener instalada la versión más reciente de Python.

---

## Video de demostración

Puedes encontrar el video con la demostración de los ejercicios [aquí](https://youtu.be/z8-hENGZSy8).

---

## Créditos

Este laboratorio fue desarrollado por Gabriel Alberto Paz Gonzalez como parte del curso de Teoría de la Computación.
