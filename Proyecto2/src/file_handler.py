import os
from config import OUTPUT_DIR

def readFile(fileName: str) -> list[str] | None:
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            data = file.read()
            return data.split('\n')  # Devuelve las líneas del archivo
    except Exception as e:
        print(f"Error al leer el archivo {fileName}: {e}")
        return None  # Devuelve None si ocurre un error


def writeOutput(fileName: str, content: str) -> None:
    filePath = os.path.join(OUTPUT_DIR, fileName)
    try:
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Resultado guardado en {filePath}")
    except Exception as e:
        print(f"Error al escribir en el archivo {filePath}: {e}")
