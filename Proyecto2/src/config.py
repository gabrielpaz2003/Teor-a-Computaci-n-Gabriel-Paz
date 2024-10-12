import os

# Define las rutas de los directorios de entrada y salida
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, '../input')
OUTPUT_DIR = os.path.join(BASE_DIR, '../output')

# Nombre del archivo de gramática por defecto
DEFAULT_INPUT_FILE = '../input/gramatica1.txt'

# Crea las carpetas si no existen
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
