import yaml

def read_yaml(filename: str) -> dict:
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
