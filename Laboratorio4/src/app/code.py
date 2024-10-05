import graphviz
import re

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class AFN:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        self.transiciones = []

    def agregar_transicion(self, desde, simbolo, hacia):
        self.transiciones.append((desde, simbolo, hacia))

    def dibujar_afn(self, nombre_archivo):
        dot = graphviz.Digraph()

        # Dibujar estados
        estados = set()
        for transicion in self.transiciones:
            desde, simbolo, hacia = transicion
            estados.add(desde)
            estados.add(hacia)

        for estado in estados:
            if estado == self.final:
                dot.node(str(estado), str(estado), shape='doublecircle')
            else:
                dot.node(str(estado), str(estado))

        # Dibujar transiciones
        for transicion in self.transiciones:
            desde, simbolo, hacia = transicion
            dot.edge(str(desde), str(hacia), label=simbolo)

        dot.render(nombre_archivo, format='png')

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

    def construir_afn(self, nodo):
        if nodo.valor.isalnum() or nodo.valor == 'ε':
            inicio = Nodo('inicio')
            final = Nodo('final')
            afn = AFN(inicio, final)
            afn.agregar_transicion(inicio, nodo.valor, final)
            return afn
        elif nodo.valor == '|':
            afn_izquierda = self.construir_afn(nodo.izquierda)
            afn_derecha = self.construir_afn(nodo.derecha)
            inicio = Nodo('inicio')
            final = Nodo('final')
            afn = AFN(inicio, final)
            afn.agregar_transicion(inicio, 'ε', afn_izquierda.inicio)
            afn.agregar_transicion(inicio, 'ε', afn_derecha.inicio)
            afn.agregar_transicion(afn_izquierda.final, 'ε', final)
            afn.agregar_transicion(afn_derecha.final, 'ε', final)
            afn.transiciones.extend(afn_izquierda.transiciones)
            afn.transiciones.extend(afn_derecha.transiciones)
            return afn
        elif nodo.valor == '.':
            afn_izquierda = self.construir_afn(nodo.izquierda)
            afn_derecha = self.construir_afn(nodo.derecha)
            afn = AFN(afn_izquierda.inicio, afn_derecha.final)
            afn.transiciones.extend(afn_izquierda.transiciones)
            afn.agregar_transicion(afn_izquierda.final, 'ε', afn_derecha.inicio)
            afn.transiciones.extend(afn_derecha.transiciones)
            return afn
        elif nodo.valor == '*':
            afn_sub = self.construir_afn(nodo.izquierda)
            inicio = Nodo('inicio')
            final = Nodo('final')
            afn = AFN(inicio, final)
            afn.agregar_transicion(inicio, 'ε', afn_sub.inicio)
            afn.agregar_transicion(inicio, 'ε', final)
            afn.agregar_transicion(afn_sub.final, 'ε', afn_sub.inicio)
            afn.agregar_transicion(afn_sub.final, 'ε', final)
            afn.transiciones.extend(afn_sub.transiciones)
            return afn

    def simular_afn(self, afn, cadena):
        def epsilon_clausura(estados):
            stack = list(estados)
            clausura = set(estados)
            while stack:
                estado = stack.pop()
                for desde, simbolo, hacia in afn.transiciones:
                    if desde == estado and simbolo == 'ε' and hacia not in clausura:
                        clausura.add(hacia)
                        stack.append(hacia)
            return clausura

        def mover(estados, simbolo):
            resultado = set()
            for estado in estados:
                for desde, transicion_simbolo, hacia in afn.transiciones:
                    if desde == estado and transicion_simbolo == simbolo:
                        resultado.add(hacia)
            return resultado

        estados_actuales = epsilon_clausura({afn.inicio})
        for simbolo in cadena:
            estados_actuales = epsilon_clausura(mover(estados_actuales, simbolo))

        return afn.final in estados_actuales

def procesar_expresiones(archivo_entrada, archivo_salida):
    analizador = AnalizadorRegex()
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w', encoding='utf-8') as salida:
        for linea in entrada:
            expresion = linea.strip()
            print(f"Procesando expresión regular: {expresion}")
            cadena = input(f"Introduce la cadena a evaluar contra la expresión '{expresion}': ")

            expresion_postfijo, _ = analizador.convertir_a_postfijo(expresion)
            arbol = analizador.construir_arbol(expresion_postfijo)
            afn = analizador.construir_afn(arbol)
            nombre_archivo = re.sub(r'[<>:"/\\|?*ε]', '_', f'afn_{expresion_postfijo}')
            afn.dibujar_afn(nombre_archivo)
            resultado = 'sí' if analizador.simular_afn(afn, cadena) else 'no'
            salida.write(f"Expresión: {expresion}, Cadena: {cadena}, Resultado: {resultado}\n")
            print(f"Resultado: {resultado}\n")

# Ejemplo de uso
archivo_entrada = 'resources/inregex.txt'
archivo_salida = 'resources/outregex.txt'
procesar_expresiones(archivo_entrada, archivo_salida)
