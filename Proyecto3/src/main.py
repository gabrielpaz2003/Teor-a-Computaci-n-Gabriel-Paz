# UNIVERSIDAD DEL VALLE DE GUATEMALA
# TEORIA DE LA COMPUTACIÓN
# PROYECTO FINAL
# GABRIEL ALBERTO PAZ GONZÁLEZ 221087

import yaml
from icecream import ic
from pprint import pprint
import copy

#Función que lee el archivo yaml
def readYaml(filename: str) -> dict:
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    
class turingMachine:
    def __init__(self, data: dict, tape: str):
        self.satates: list = data['q_states']['q_list']
        self.initialState: str = data['q_states']['initial']
        self.finalStates: str = data['q_states']['final']
        self.trapState: str = data['q_states']['trap']
        self.alphabet: list = data['alphabet']
        if data['tape_alphabet'] != None:
            self.tapeAlphabet: list = data['tape_alphabet'] + data['alphabet']
        else:
            self.tapeAlphabet: list = data['alphabet']
        self.tape: list = list(tape)
        self.transitions = data['delta']
        self.currentState: str = data['q_states']['initial']
        self.headPosition: int = 0
        self.cache: str = None

    def inAlphabert(self) -> bool:
        for i in self.tape:
            if i not in self.tapeAlphabet:
                return False
        return True

    def simulate(self):
        currentState: str = self.initialState
        position: int = self.headPosition
        tape: list = self.tape
        cache: str = self.cache

        if not self.inAlphabert():
            print("La cinta no es aceptada porque la entrada no coincide con el alfabeto")
            return False
        
 
        position = 0
        print("La cinta si es aceptada por el alfabeto")

        running: bool = True

        ids = []

        state = str(f'[{currentState},{cache}]')
        idtape = copy.deepcopy(tape)
        idtape.insert(position,state)

        ids.append(idtape)

        while running:
            running = False
            for i in self.transitions:

                if (currentState == self.trapState):
                    return False, ids
                    
                if (currentState in self.finalStates):
                    return True, ids

                if (i['params']['initial_state'] != currentState):
                    continue

                if cache == None:
                    W = tape[position]
                else:
                    W = cache

                if (i['params']['tape_input'] == tape[position]):
                    if i['params']['mem_cache_value'] == cache:
                        
                        if i['output']['tape_output'] == 'W':
                            tape[position] == W
                        else:
                            tape[position] = i['output']['tape_output']

                        if (i['output']['mem_cache_value'] == 'W'):
                            cache = W
                        else:
                            cache = i['output']['mem_cache_value']
                        
                        currentState = i['output']['final_state']

                        direction = i['output']['tape_displacement']
                        if (direction == 'R'):
                            position += 1
                            if position == len(tape):
                                tape.append(None)
                        elif (direction == 'L'):
                            if position == 0:
                                tape.insert(0,None)
                            else:
                                position -= 1
                        elif (direction == 'S'):
                            pass

                        running = True

                        if cache == None:
                            state = str(f'[{currentState},␣]')
                        else:
                            state = str(f'[{currentState},{cache}]')
                        idtape = copy.deepcopy(tape)
                        idtape.insert(position,state)

                        ids.append(idtape)

                    elif i['params']['mem_cache_value'] == 'W':
                        
                        currentState = i['output']['final_state']
                        if i['output']['tape_output'] == 'W':
                            tape[position] == W
                        else:
                            tape[position] = i['output']['tape_output']

                        if (i['output']['mem_cache_value'] == 'W'):
                            cache = W
                        else:
                            cache = i['output']['mem_cache_value']

                        direction = i['output']['tape_displacement']
                        if (direction == 'R'):
                            position += 1
                            if position == len(tape):
                                tape.append(None)
                        elif (direction == 'L'):
                            if position == 0:
                                tape.insert(0,None)
                            else:
                                position -= 1
                        elif (direction == 'S'):
                            pass
                        running = True

                        if cache == None:
                            state = str(f'[{currentState},␣]')
                        else:
                            state = str(f'[{currentState},{cache}]')
                        idtape = copy.deepcopy(tape)
                        idtape.insert(position,state)

                        ids.append(idtape)

                elif (i['params']['tape_input'] == 'W') and (tape[position] == W):
                    if i['params']['mem_cache_value'] == cache:
                        
                        currentState = i['output']['final_state']
                        if i['output']['tape_output'] == 'W':
                            tape[position] == W
                        else:
                            tape[position] = i['output']['tape_output']

                        if (i['output']['mem_cache_value'] == 'W'):
                            cache = W
                        else:
                            cache = i['output']['mem_cache_value']

                        direction = i['output']['tape_displacement']
                        if (direction == 'R'):
                            position += 1
                            if position == len(tape):
                                tape.append(None)
                        elif (direction == 'L'):
                            if position == 0:
                                tape.insert(0,None)
                            else:
                                position -= 1
                        elif (direction == 'S'):
                            pass
                        running = True

                        
                        if cache == None:
                            state = str(f'[{currentState},␣]')
                        else:
                            state = str(f'[{currentState},{cache}]')
                        idtape = copy.deepcopy(tape)
                        idtape.insert(position,state)

                        ids.append(idtape)


                    elif i['params']['mem_cache_value'] == 'W':
                        

                        currentState = i['output']['final_state']
                        if i['output']['tape_output'] == 'W':
                            tape[position] == W
                        else:
                            tape[position] = i['output']['tape_output']

                        if (i['output']['mem_cache_value'] == 'W'):
                            cache = W
                        else:
                            cache = i['output']['mem_cache_value']

                        direction = i['output']['tape_displacement']
                        if (direction == 'R'):
                            position += 1
                            if position == len(tape):
                                tape.append(None)
                        elif (direction == 'L'):
                            if position == 0:
                                tape.insert(0,None)
                            else:
                                position -= 1
                        elif (direction == 'S'):
                            pass
                        running = True

                        if cache == None:
                            state = str(f'[{currentState},␣]')
                        else:
                            state = str(f'[{currentState},{cache}]')
                        idtape = copy.deepcopy(tape)
                        idtape.insert(position,state)

                        ids.append(idtape)

        return False, None
                    

if __name__ == '__main__':
    data: dict = readYaml('input/MTR1.yaml') 

    for j in data['simulation_strings']:
        mt: turingMachine = turingMachine(data, j)

        accept, table = mt.simulate()



        if accept:
            newTable = []
            for i in table:
                newTable.append("".join(['␣' if x == None else x for x in i]) + " => ")

            pprint(newTable)
            print("La máquina si acepta la cadena de entrada")
        else:
            print("La máquina no acepta la cadena de entrada")

        input("Presione enter para continuar")
