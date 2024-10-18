import os
from datetime import datetime
from config import OUTPUT_DIR

def readFile(fileName: str) -> list[str]:
    if not os.path.exists(fileName):
        raise FileNotFoundError(f"El archivo {fileName} no existe.")
    
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            data = file.read().split('\n')
            if not data:
                raise ValueError(f"El archivo {fileName} está vacío.")
            return data
    except Exception as e:
        raise IOError(f"Error al leer el archivo {fileName}: {e}")


def log_result(accepted: bool, sentence: str, output_dir: str):
    print("Guardando resultados en el archivo de log...")
    print("Testeando la frae: ", sentence)
    log_file = os.path.join(output_dir, 'resultado.txt')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Construir mensaje de log
    if accepted:
        log_message = f"[{timestamp}] La frase '{' '.join(sentence)}' fue aceptada.\n"
    else:
        log_message = f"[{timestamp}] La frase '{' '.join(sentence)}' NO fue aceptada.\n"
    
    # Guardar en el archivo de logs
    try:
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(log_message)
    except IOError as e:
        print(f"Error al escribir en el archivo de log: {e}")