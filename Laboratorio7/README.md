# Eliminación de Producciones Epsilon en Gramáticas

Este proyecto tiene como objetivo procesar gramáticas libres de contexto y eliminar producciones epsilon (`ε`). El código verifica si una gramática es válida según un conjunto de expresiones regulares, construye el conjunto de subconjuntos posibles de variables anulables y modifica la gramática para eliminar las producciones epsilon.

## Estructura del Proyecto

- **`evaluate_expression`**: Verifica si una expresión de gramática cumple con el formato especificado por una expresión regular.
- **`build_power_set`**: Construye el conjunto de potencias (todos los subconjuntos posibles) de un conjunto dado.
- **`remove_epsilon_productions`**: Elimina las producciones epsilon (`ε`) de una gramática y actualiza las reglas de producción de acuerdo a las variables anulables.
- **`read_file`**: Lee el contenido de un archivo de texto y lo devuelve como una lista de líneas.

## Requisitos Previos

- **Python 3.x**: Asegúrate de tener Python instalado en tu sistema.
- **Pip (Opcional)**: Para gestionar dependencias adicionales si las hubiese, aunque el código no requiere paquetes externos fuera de los módulos estándar de Python.

## Instalación

1. Asegurarse de encontrarse en la ruta de la carpeta de Laboratorio7

```bash
cd Laboratorio7
```


## Uso

1. Crea un archivo de texto dentro de la carpeta /resources llamado input1.txt (y opcionalmente input2.txt) que contenga las producciones de la gramática. Cada línea debe tener el formato:

A->B|C
B->ε
C->A|B|ε

2. Ejecuta el script principal

python main.py

El programa validará si todas las producciones en el archivo cumplen con la expresión regular, eliminará las producciones ε de la gramática, y mostrará la nueva gramática en consola.

## Ejemplo de Input

S->AB|ε
A->a|ε
B->b

## Ejemplo de Output

{'S': ['AB', 'A', 'B'],
 'A': ['a'],
 'B': ['b']}


## Estructura del Proyecto

```
📦 Laboratorio7
├── 📂 PDFs
│   └── 📜 Instrucciones.pdf
│   └── 📜 ejercicio1.pdf
├── 📂 resources
│   ├── 📜 input1.txt
│   └── 📜 input2.txt
├── 📂 src
│   └── 📜 main.py
├── 📂 video
│   └── 📜 video.mp4
└── 📜 README.md
```

## Contacto

Si tienes alguna duda o comentario sobre este repositorio, no dudes en ponerte en contacto conmigo a través de mis canales oficiales.

Discord: **gabrielpaz___**
Correo electrónico: **paz221087@uvg.edu.gt**  

[![Linkedin](https://img.shields.io/badge/-username-blue?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN)](https://www.linkedin.com/in/gabriel-paz-gapg/)
[![Gmail Badge](https://img.shields.io/badge/-seuemail@email.com-006bed?style=flat-square&logo=Gmail&logoColor=white&link=mailto:SEU-EMAIL)](mailto:SEU-EMAIL)
[![GitHub](https://img.shields.io/github/followers/iuricode?label=follow&style=social)](LINK-DO-SEU-GITHUB)

## Licencia

Este repositorio está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

