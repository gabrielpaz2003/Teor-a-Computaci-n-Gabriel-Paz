# UNIVERSIDAD DEL VALLE DE GUATEMALA
# TEORIA DE LA COMPUTACIÓN
# PROYECTO FINAL
# GABRIEL ALBERTO PAZ GONZÁLEZ 221087

from turing_machine.parser import read_yaml
from turing_machine.machine import turingMachine
from colorama import Fore, Style, init

init(autoreset=True)

def display_table(table):
    print(Fore.CYAN + "\n--- Progreso de la simulación ---")
    for step, state in enumerate(table, start=1):
        formatted_state = "".join(['␣' if x is None else x for x in state])
        print(Fore.YELLOW + f"Paso {step}: {formatted_state}")
    print(Fore.CYAN + "--- Fin de la simulación ---\n")

if __name__ == '__main__':
    data = read_yaml('input/modifier_machine.yaml')
    total_accepted = 0
    total_rejected = 0

    print(Fore.GREEN + "=== Simulación de Máquina de Turing ===")
    for index, j in enumerate(data['simulation_strings'], start=1):
        print(Fore.MAGENTA + f"\n--- Cadena {index}: '{j}' ---")
        mt = turingMachine(data, j)
        accept, table = mt.simulate()

        if accept:
            display_table(table)
            print(Fore.GREEN + "Resultado: La máquina SÍ acepta la cadena de entrada.\n")
            total_accepted += 1
        else:
            print(Fore.RED + "Resultado: La máquina NO acepta la cadena de entrada.\n")
            total_rejected += 1

        input(Fore.CYAN + "Presione Enter para continuar...")

    print(Fore.GREEN + "\n=== Resumen de Simulación ===")
    print(Fore.YELLOW + f"Cadenas aceptadas: {total_accepted}")
    print(Fore.RED + f"Cadenas rechazadas: {total_rejected}")
