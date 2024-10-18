import time
from file_handler import readFile, log_result
from grammar_utils import convertToChomsky, evaluateExpression
from cyk_algorithm import cykParse
from tree_visualizer import generateAndVisualizeTree
from pprint import pprint
from config import DEFAULT_INPUT_FILE, OUTPUT_DIR

if __name__ == '__main__':
    try:
        # Inicia el cronómetro antes de cualquier procesamiento
        start_time = time.time()

        # Leer la gramática desde el archivo
        data = readFile(DEFAULT_INPUT_FILE)
        if data is None:
            raise ValueError(f"No se pudo leer el archivo {DEFAULT_INPUT_FILE}")
        
        # Validar cada producción
        regex = "[A-z]+(\s)?->(\s)?(([A-Za-z0-9]|\s)*(\|)*)+|ε"
        for expression in data:
            if expression != '':
                if not evaluateExpression(regex=regex, expression=expression):
                    raise ValueError(f"La producción {expression} no cumple con el formato esperado.")

        # Conversión a CNF
        grammar: dict = {}
        entry: str = ''
        for expression in data:
            expressionSplit1 = expression.split('->')
            expressionSplit2 = expressionSplit1[1].split('|')
            splitted = [i.strip() for i in expressionSplit2]

            if entry == '':
                entry = expressionSplit1[0].strip()

            if expressionSplit1[0].strip() not in grammar:
                grammar[expressionSplit1[0].strip()] = splitted
            else:
                grammar[expressionSplit1[0].strip()].extend(splitted)

        
        # Convertir la gramática a CNF
        grammar = convertToChomsky(grammar, entry)
        pprint(grammar)

        # Pausar el cronómetro para esperar la entrada del usuario
        execution_time = time.time() - start_time

        # Pedir al usuario que ingrese una frase
        frase = input("Ingrese la frase que desea verificar: ")
        sentence = frase.split()

        # Reanudar el cronómetro
        resume_time = time.time()

        # Aplicar el algoritmo CYK
        accept, table = cykParse(grammar, sentence)

        # Mostrar los resultados
        if accept:
            print("La frase SI es aceptada")
            generateAndVisualizeTree(grammar, table, sentence, entry)
        else:
            print("La frase NO es aceptada")

        # Guardar los resultados en el archivo de log
        print("Probando la frase desde el main", frase)
        log_result(accept, frase, OUTPUT_DIR)

        # Detener el cronómetro y calcular el tiempo total de ejecución (sin contar la entrada del usuario)
        total_time = time.time() - resume_time + execution_time
        print(f"Tiempo de ejecución (sin incluir la entrada del usuario): {total_time:.4f} segundos")

    except Exception as e:
        print(f"Error: {e}")
