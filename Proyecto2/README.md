
# Proyecto 2 - Análisis Sintáctico y Árbol de Parseo

Este proyecto implementa un **análisis sintáctico** basado en gramáticas libres de contexto, utilizando el **algoritmo CYK** para verificar si una frase es aceptada por la gramática, y genera un **árbol de parseo** que se visualiza y se guarda como una imagen.

## Características del Proyecto

- Análisis Sintáctico con CYK: Implementa el algoritmo CYK para verificar si una frase es aceptada por una gramática en Forma Normal de Chomsky (CNF).
- Visualización del Árbol de Parseo: Genera un árbol de parseo de la frase aceptada y lo visualiza como una imagen, además de guardarlo en un archivo PNG.
- Modularidad: El código está dividido en módulos para facilitar la lectura y mantenimiento (manejo de archivos, algoritmo CYK, visualización, etc.).
- Entrada y Salida: El programa lee una gramática desde un archivo en la carpeta input, analiza la frase ingresada por el usuario, y guarda los resultados en la carpeta output.
- Conversión a CNF: Incluye funciones para convertir cualquier gramática a CNF, lo cual es un requisito previo para utilizar el algoritmo CYK
- Manejo de Dependencias: Usa un archivo requirements.txt para instalar fácilmente todas las dependencias necesarias.

## Requisitos Previos

Este proyecto utiliza Python 3.11 y varias librerías para la generación del árbol de parseo. Asegúrate de tener las siguientes dependencias instaladas:

- **networkx**: Para crear y manejar grafos.
- **matplotlib**: Para visualizar el árbol de parseo.
- **pydot**: Para la disposición gráfica del árbol.
- **graphviz**: Necesario para generar el layout del grafo.

Puedes instalar las dependencias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```


## Instalación

1. Clona este repositorio:
    ```bash
    git clone <https://github.com/vgcarlol/Proy1-Teoria-Compu>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd <Proyecto2>
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Prepara un archivo de texto en la carpeta `input/` llamado `gramatica.txt`.El archivo debe seguir el formato estándar de producción de gramáticas en CNF (Forma Normal de Chomsky).
    ```
    S->NP VP
    VP->VP PP
    VP->V NP
    VP->cooks|drinks|eats|cuts
    PP->P NP
    NP->DET N
    NP->he|she
    V->cooks|drinks|eats|cuts
    P->in|with
    N->cat|dog
    N->beer|cake|juice|meat|soup
    N->fork|knife|oven|spoon
    DET->a|the
    ```
3. Ejecuta el programa principal (main.py):

    ```
    python src/main.py
    ```

4. Ingresa la frase:
    ```
    Ingrese la frase que desea verificar:: #Ingresar frase
    ```
5. Los resultados se generarán en la carpeta `output/` y se mostrarán en consola.

## Estructura del Proyecto

```
📦 Laboratorio7
├── 📂 input
│   └── ![TXT](https://img.icons8.com/color/48/000000/txt.png) gramatica1.txt
├── 📂 output
│   └── ![TXT](https://img.icons8.com/color/48/000000/txt.png) resultado.txt
├── 📂 src
│   ├── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) config.py
│   ├── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) cyk_algorithm.py
│   ├── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) file_handler.py
│   ├── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) grammar_utils.py
│   ├── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) main.py
│   └── ![Python](https://img.icons8.com/color/48/000000/python--v1.png) tree_visualizer.py
├── ![PDF](https://img.icons8.com/color/48/000000/pdf.png) Instrucciones.pdf
├── ![TXT](https://img.icons8.com/color/48/000000/txt.png) README.md
└── ![TXT](https://img.icons8.com/color/48/000000/txt.png) requirements.txt

```


### config.py:

**Descripción:** Este archivo contiene configuraciones clave del proyecto, como la ruta por defecto para el archivo de entrada. Sirve para centralizar las configuraciones y facilitar posibles cambios en el futuro.
**Funcionalidad:** Define la ruta del archivo de entrada de la gramática.

### cyk_algorithm.py:

**Descripción:** Implementa el algoritmo CYK (Cocke-Younger-Kasami), que es un algoritmo de análisis sintáctico utilizado para verificar si una cadena pertenece a un lenguaje descrito por una gramática en CNF.
**Funcionalidad:** Toma la gramática convertida a CNF y una cadena como entrada, y determina si la cadena es aceptada o no.

### file_handler.py:

**Descripción:** Manejador de archivos para leer y escribir datos en el proyecto. Lee la gramática desde un archivo de texto y escribe los resultados en archivos de salida.
**Funcionalidad:** Lee el archivo de gramática desde la carpeta input y escribe los resultados del análisis en la carpeta output.

### grammar_utils.py:

**Descripción:** Contiene varias utilidades para trabajar con gramáticas, incluyendo funciones para convertir una gramática a Forma Normal de Chomsky (CNF).
**Funcionalidad:** Simplifica la gramática eliminando producciones epsilon, producciones unitarias, símbolos no derivables, y producciones inalcanzables.

### main.py:

**Descripción:** Es el punto de entrada principal del programa. Controla el flujo del programa, desde la lectura de la gramática, el análisis de la frase con el algoritmo CYK, hasta la visualización y almacenamiento del árbol de parseo.
**Funcionalidad:** Ejecuta el programa completo, pide al usuario que ingrese una frase, verifica la gramática con el algoritmo CYK, y genera el árbol de parseo si la frase es aceptada.

### tree_visualizer.py:

**Descripción:** Genera y visualiza el árbol de parseo utilizando la librería networkx para crear los nodos y aristas que representan la estructura del árbol.
**Funcionalidad:** Toma la tabla generada por el algoritmo CYK y construye un árbol de parseo, que luego se visualiza y guarda como una imagen en la carpeta output.

### README.md:

**Descripción:** Proporciona una descripción detallada del proyecto, incluyendo instrucciones de instalación, requisitos, cómo usar el programa y una explicación de la estructura del proyecto.
**Funcionalidad:** Documento de referencia para cualquier persona que quiera entender cómo instalar y ejecutar el proyecto.

### requirements.txt:

**Descripción:** Lista todas las dependencias necesarias para ejecutar el proyecto, como networkx, matplotlib, pydot, y otras librerías de Python.
**Funcionalidad:** Facilita la instalación de dependencias utilizando el comando pip install -r requirements.txt.

## Contacto

Si tienes alguna duda o comentario sobre este repositorio, no dudes en ponerte en contacto conmigo a través de mis canales oficiales.

Discord: **gabrielpaz___**
Correo electrónico: **paz221087@uvg.edu.gt**  

[![Linkedin](https://img.shields.io/badge/-gabrielpaz-blue?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN)](https://www.linkedin.com/in/gabriel-paz-gapg/)
[![Gmail Badge](https://img.shields.io/badge/-paz221087@uvg.edu.gt-006bed?style=flat-square&logo=Gmail&logoColor=white&link=mailto:SEU-EMAIL)](mailto:paz221087@uvg.edu.gt)
[![GitHub](https://img.shields.io/github/followers/iuricode?label=follow&style=social)](LINK-DO-SEU-GITHUB)

## Licencia

Este proyecto está bajo la licencia MIT.
