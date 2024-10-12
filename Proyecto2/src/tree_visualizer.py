import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

def generateAndVisualizeTree(grammar: dict, table: list, sentence: list, entry: str) -> None:
    class Node:
        def __init__(self, symbol):
            self.symbol = symbol
            self.children = []

        def addChild(self, child):
            self.children.append(child)

        def getChildren(self):
            return self.children
        
    def generateTree(table, grammar, i, j, symbol):
        if i == j:
            for rule, productions in grammar.items():
                for production in productions:
                    if len(production) == 1 and symbol in production:
                        return Node(symbol)
        
        for k in range(i, j):
            for rule, productions in grammar.items():
                for production in productions:
                    if symbol == rule and len(production) == 2:
                        left, right = production
                        if left in table[i][k] and right in table[k+1][j]:
                            node = Node(symbol)
                            node.addChild(generateTree(table, grammar, i, k, left))
                            node.addChild(generateTree(table, grammar, k+1, j, right))
                            return node

        node = Node(symbol)

        if len(node.getChildren()) == 0:
            outputs = grammar[symbol]
            terminals = []

            for term in outputs:
                if len(term) == 1:
                    terminals.append(term[0])

            for word in sentence:
                if word in terminals:
                    node.addChild(Node(word))
                    sentence.remove(word)
                    break

        return node
    
    def visualize(tree, output_path=None):
        G = nx.DiGraph()
        labels = {}

        def addNodeEdges(tree, G, parent=None, counter=0):
            node = f"{tree.symbol}{counter}"
            G.add_node(node)
            labels[node] = tree.symbol
            if parent is not None:
                G.add_edge(parent, node)
            counter += 1
            for child in tree.children:
                counter = addNodeEdges(child, G, node, counter)
            return counter

        addNodeEdges(tree, G)
        pos = graphviz_layout(G, "dot")
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", font_size=15)
        plt.title("Parse Tree")

        # Guardar la figura si se proporciona una ruta de salida
        if output_path:
            plt.savefig(output_path)
            print(f"Árbol de parseo guardado en: {output_path}")
        
        plt.show()  # Mostrar la figura en pantalla

    # Generar el árbol
    parseTree = generateTree(table, grammar, 0, len(table) - 1, entry)

    # Definir la ruta de salida para el archivo de imagen
    output_dir = os.path.abspath('/output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, 'parse_tree.png')

    # Visualizar y guardar el árbol
    visualize(parseTree, output_path)
