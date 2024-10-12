import os
import time
from file_handler import readFile, writeOutput
from grammar_utils import convertToChomsky, evaluateExpression
from cyk_algorithm import cykParse
from tree_visualizer import generateAndVisualizeTree
from pprint import pprint
from config import DEFAULT_INPUT_FILE


if __name__ == '__main__':
    start_time = time.time()
    regex = "[A-z]+(\s)?->(\s)?(([A-Za-z0-9]|\s)*(\|)*)+|ε"
    file_path = os.path.abspath('input\gramatica.txt')
    data = readFile(file_path)
    for expression in data:
        if expression != '':
            if not evaluateExpression(regex=regex, expression=expression):
                print(f'La producción {expression} no cumple por lo que la gramática no es aceptada')
                exit(0)

    grammar: dict = {}

    entry: str = ''

    for expression in data:

        expressionSplit1 = expression.split('->')
        expressionSplit2 = expressionSplit1[1].split('|')
        splitted = []
        for i in expressionSplit2:
            splitted.append(i.strip())

        if entry == '':
            entry = expressionSplit1[0].strip()


        if expressionSplit1[0] not in grammar:
            grammar[expressionSplit1[0].strip()] = splitted
        else:
            grammar[expressionSplit1[0].strip()].extend(splitted)

    grammar: dict = convertToChomsky(grammar, entry) 
    pprint(grammar)
    sentence: list = input("Ingrese la frase que desea verificar: ").split()
    accept, table = cykParse(grammar, sentence)

    end_time = time.time()  # Tiempo de finalización

    # Calcular el tiempo total de ejecución
    execution_time = end_time - start_time
    print(f"El tiempo total de ejecución fue de {execution_time:.4f} segundos.")

    if accept:
        print("La frase SI es aceptada")
        generateAndVisualizeTree(grammar, table, sentence, entry)
    else:
        print("La frase NO es aceptada")