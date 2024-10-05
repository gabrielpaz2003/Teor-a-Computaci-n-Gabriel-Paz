# UNIVERSIDAD DEL VALLE DE GUATEMALA
# Teoria de la Computacion
# Gabriel Alberto Paz González - 221087
# Fecha: 2024-10-05

# Descripcion: Programa que recibe un archivo de texto con una gramatica libre de contexto y elimina las producciones epsilon

# Importacion de librerias
import re
import itertools
from pprint import pprint


def evaluate_expression(pattern: str, expression: str) -> bool: # Funcion para evaluar si una expresion cumple con un patron
    return bool(re.match(pattern, expression))


def build_power_set(items: set) -> list: # Funcion para construir el conjunto potencia de un conjunto
    return list(itertools.chain.from_iterable(
        itertools.combinations(items, i) for i in range(len(items) + 1)
    ))


def remove_epsilon_productions(grammar: dict) -> dict: # Funcion para remover producciones epsilon

    nullable = {key for key in grammar if 'ε' in grammar[key]}

    changed = True
    while changed:
        changed = False
        for key in grammar:
            if any(item in grammar[key] for item in nullable) and key not in nullable:
                nullable.add(key)
                changed = True

    for key in grammar:
        grammar[key] = [prod for prod in grammar[key] if prod != 'ε']

    power_set = build_power_set(nullable)
    updated_grammar = {key: list(grammar[key]) for key in grammar}

    for key in grammar:
        for production in grammar[key]:
            for subset in power_set:
                new_production = production
                for nullable_item in subset:
                    new_production = new_production.replace(nullable_item, '')
                if new_production and new_production not in updated_grammar[key]:
                    updated_grammar[key].append(new_production)

    return updated_grammar


def read_file(file_path: str) -> list[str] | None: # Funcion para leer un archivo
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: No se pudo abrir el archivo {file_path}")
        return None


if __name__ == '__main__': # Funcion principal
    regex = r"[A-Z]->(([A-Za-z0-9])*(\|)*)+|ε"
    
    for file_index in range(1, 3):
        data = read_file(f'./resources/input{file_index}.txt')
        if not data:
            exit(1)
        
        if any(not evaluate_expression(regex, line) for line in data if line):
            print(f'Error: Gramática no aceptada en el archivo input{file_index}.txt')
            exit(1)

        print(f"Todas las producciones en input{file_index}.txt son válidas.")

        grammar = {
            line.split('->')[0]: line.split('->')[1].split('|')
            for line in data if '->' in line
        }

        new_grammar = remove_epsilon_productions(grammar)
        pprint(new_grammar)
