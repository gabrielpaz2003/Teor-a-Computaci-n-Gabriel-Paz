import graphviz
import re

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class AnalizadorRegex:
    def __init__(self):
        self.precedencias = {
            '(': 1,
            '|': 2,
            '.': 3,
            '?': 4,
            '*': 4,
            '+': 4,
        }
        self.simbolos = {'|', '?', '+', '*', '(', ')'}


    def prioridad(self, simbolo):
        return self.precedencias.get(simbolo, 6)

    def preparar_regex(self, regex):
        resultado = []
        i = 0
        while i < len(regex):
            actual = regex[i]
            if actual == '+':
                resultado.append(resultado[-1])
                resultado.append('*')
            elif actual == '?':
                resultado.append('|')
                resultado.append('ε')
            else:
                resultado.append(actual)

            if actual == '\\':
                i += 1
                resultado.append(regex[i])
            elif actual not in self.simbolos and i + 1 < len(regex):
                siguiente = regex[i + 1]
                if siguiente not in self.simbolos and siguiente not in {'\\', '(', ')'}:
                    resultado.append('.')

            i += 1

        return ''.join(resultado)

    def convertir_a_postfijo(self, regex):
        salida = []
        pila = []
        detalles = []
        regex_procesado = self.preparar_regex(regex)

        i = 0
        while i < len(regex_procesado):
            simbolo = regex_procesado[i]
            if simbolo.isalnum() or simbolo == '\\':
                salida.append(simbolo)
                if simbolo == '\\' and i + 1 < len(regex_procesado):
                    i += 1
            elif simbolo == '(':
                pila.append(simbolo)
            elif simbolo == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                if pila:
                    pila.pop()  # pop the '('
            else:
                while pila and self.prioridad(pila[-1]) >= self.prioridad(simbolo):
                    salida.append(pila.pop())
                pila.append(simbolo)

            detalles.append(f"Elemento: {simbolo}, Pila: {list(pila)}, Salida: {list(salida)}")
            i += 1

        while pila:
            salida.append(pila.pop())
            detalles.append(f"Vaciar pila, Pila: {list(pila)}, Salida: {list(salida)}")

        return ''.join(salida), detalles

    def construir_arbol(self, postfix):
        pila = []
        for simbolo in postfix:
            if simbolo.isalnum() or simbolo == '\\':
                pila.append(Nodo(simbolo))
            elif simbolo in {'*', '?', '+'}:
                nodo = Nodo(simbolo, pila.pop())
                pila.append(nodo)
            elif simbolo in {'|', '.'}:
                derecha = pila.pop()
                izquierda = pila.pop()
                nodo = Nodo(simbolo, izquierda, derecha)
                pila.append(nodo)
        return pila.pop()

    def dibujar_arbol(self, nodo, dot=None):
        if dot is None:
            dot = graphviz.Digraph()
        dot.node(str(id(nodo)), nodo.valor)
        if nodo.izquierda:
            dot.edge(str(id(nodo)), str(id(nodo.izquierda)))
            self.dibujar_arbol(nodo.izquierda, dot)
        if nodo.derecha:
            dot.edge(str(id(nodo)), str(id(nodo.derecha)))
            self.dibujar_arbol(nodo.derecha, dot)
        return dot

def procesar_expresiones(archivo_entrada, archivo_salida):
    analizador = AnalizadorRegex()
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w', encoding='utf-8') as salida:
        for expresion in entrada:
            expresion_postfijo, transformaciones = analizador.convertir_a_postfijo(expresion.strip())
            arbol = analizador.construir_arbol(expresion_postfijo)
            dot = analizador.dibujar_arbol(arbol)
            
            # Limpiar caracteres no válidos para nombres de archivos
            nombre_archivo = re.sub(r'[<>:"/\\|?*ε]', '_', f'arbol_{expresion_postfijo}')
            
            dot.render(nombre_archivo, format='png')
            salida.write(f"Expresion Postfijo: {expresion_postfijo}\nDetalle de pasos:\n")
            for transformacion in transformaciones:
                salida.write(transformacion + "\n")
            salida.write("\n")

# Ejemplo de uso
archivo_entrada = 'resources/inregex.txt'
archivo_salida = 'resources/outregex.txt'
procesar_expresiones(archivo_entrada, archivo_salida)
