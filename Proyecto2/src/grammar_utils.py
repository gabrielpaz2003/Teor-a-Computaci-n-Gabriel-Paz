import re
import copy
import itertools
from pprint import pprint

def evaluateExpression(regex: str, expression: str) -> bool:
    if re.match(regex, expression):
        return True
    else:
        return False

    if re.fullmatch("([a-z]|[0-9]|\s)*", symbol):
        return True
    else:
        return False 
    
def identifyTerms(grammar: dict) -> (set, set):
    nonTerminals: set = set(grammar.keys())
    terminals: set = set()

    for productions in grammar.values():
        for production in productions:
            for term in production.split(" "):
                if term not in nonTerminals:
                    terminals.add(term)

    return nonTerminals, terminals

def buildPowerSet(set: set) -> list[str]:
    powerSet = []
    for i in range(len(set)+1):
        powerSet.extend(itertools.combinations(set, i))
    return powerSet

def isTerminal(term: str) -> bool:
    if re.fullmatch("([a-z]|[0-9]|\s)*", term):
        return True
    else:
        return False
    
def isNonTerminal(term: str) -> bool:
    if re.fullmatch("(([A-Z])+|([0-9]*))*", term):
        return True
    else:
        return False
    
#SECCION DE SIMPLIFICACION DE GRAMATICAS PARA FORMAL NORMAL DE CHOMSKY
#ELIMINACION DE PRODUCCIONES EPSILON
def removeEpsilonProductions(grammar: dict) -> dict:
    nullable = set()

    for i in grammar:
        if 'ε' in grammar[i]:
            nullable.add(i)

    changed = True
    while changed:
        changed = False
        tempSet = set()
        for i in grammar:
            for j in nullable:
                if (j in grammar[i]) and (i not in nullable):
                    tempSet.add(i)
                    changed = True
        
        nullable = nullable.union(tempSet)
    
    #Eliminar produccion epsilon
    for i in grammar:
        if 'ε' in grammar[i]:
            grammar[i].remove('ε')

    powerSet = buildPowerSet(nullable)

    newGrammar = {}

    for i in grammar:
        newGrammar[i] = []
        for j in grammar[i]:
            newGrammar[i].append(j.strip())

        for j in grammar[i]:
            for k in powerSet:
                newProduction = j
                for l in k:
                    newProduction = newProduction.replace(l, '')
                    newProduction = newProduction.strip()
                if newProduction != '' and (newProduction not in newGrammar[i]):
                    newGrammar[i].append(newProduction)

    
    grammar = newGrammar
    newGrammar = copy.deepcopy(grammar)

    for i in grammar:
        for j in grammar[i]:
            if j == ' ':
                newGrammar[i].remove(j)
            elif isTerminal(j):
                temp = j
                temp = temp.replace(' ', '')
                newGrammar[i].append(temp)
                newGrammar[i].remove(j)

    return newGrammar

#ELIMINACION DE PRODUCCIONES UNITARIAS
def removeUnitProductions(grammar: dict) -> dict: 
    newGrammar = {}
    for i in grammar:
        newGrammar[i] = []
        for j in grammar[i]:
            newGrammar[i].append(j)

    changed = True
    while changed:
        changed = False
        for i in newGrammar:
            for j in newGrammar[i]:
                if len(j) == 1 and j.isupper():
                    for k in newGrammar[j]:
                        if k not in newGrammar[i]:
                            newGrammar[i].append(k)
                    newGrammar[i].remove(j)
                    changed = True

    return newGrammar 

#ELIMINACION DE SIMBOLOS QUE NO DERIVEN
def removeNonDerivableSymbols(grammar: dict) -> dict:
    nonTerminals, terminals = identifyTerms(grammar)
    derivable = set()

    for i in grammar:
        for j in grammar[i]:
            for k in j.split():
                if k in terminals:
                    derivable.add(i)


    changed = True
    while changed:
        changed = False
        for i in grammar:
            for j in grammar[i]:
                elementsInDerivable = 0
                for k in j.split(" "):
                    if k in derivable:
                        elementsInDerivable += 1
                
                if elementsInDerivable == len(j.split(" ")) and (i not in derivable):
                    derivable.add(i)
                    changed = True

    newGrammar = {}

    for i in derivable:
        newGrammar[i] = []
        for j in grammar[i]:
            newGrammar[i].append(j)
    

    return newGrammar

#ELIMINACION DE PRODUCCIONES INALCANZABLES
def removeUnreachableProductions(grammar: dict, entry:str) -> dict:
    reachable = set(entry)
    newGrammar = {}

    nonTerminals: set = set(grammar.keys())
    terminals: set = set()

    for productions in grammar.values():
        for production in productions:
            for term in production.split(" "):
                if term not in nonTerminals:
                    terminals.add(term)

    changed = True
    while changed:
        changed = False
        tempSet = set()
        for i in reachable:
            for j in grammar[i]:
                jsplit = j.split(" ")
                for k in jsplit:
                    if k in nonTerminals and k not in reachable:
                        tempSet.add(k)
                        changed = True


        reachable = reachable.union(tempSet)
    
    for i in reachable:
        newGrammar[i] = []
        for j in grammar[i]:
            newGrammar[i].append(j)
    for i in grammar:
        for j in grammar[i]:
            for k in j.split(" "):
                if k not in nonTerminals and k not in terminals:
                    newGrammar[i].remove(j)
                    break

    return newGrammar

#CONVERSION DE GRAMATICA A FORMA NORMAL DE CHOMSKY
def convertToChomsky(Grammar: dict, entry: str) -> dict:
    #Simplificar gramatica
    grammar = removeEpsilonProductions(Grammar)
    grammar = removeUnitProductions(grammar)
    grammar = removeNonDerivableSymbols(grammar)
    grammar = removeUnreachableProductions(grammar, entry)
    #Convertir a forma normal de Chomsky

    pprint(grammar)

    grammarSplit = {}

    for i in grammar:
        grammarSplit[i] = []
        for j in grammar[i]:
            grammarSplit[i].append(j.split(" "))


    #Cambiar terminales
    terminales = {}

    t = 0 
    changed = True
    while changed:
        changed = False
        newGrammar = copy.deepcopy(grammarSplit)
        for i in grammarSplit:
            for j in range(len(grammarSplit[i])):
                for k in range(len(grammarSplit[i][j])):
                    if (not (isNonTerminal(grammarSplit[i][j][k]))) and (len(grammarSplit[i][j]) > 1):
                        if grammarSplit[i][j][k] not in terminales.keys():
                            terminales[grammarSplit[i][j][k]] = f"T{t}"
                            newGrammar[i][j][k] = f"T{t}"
                            t += 1
                            changed = True
                        else:
                            newGrammar[i][j][k] = terminales[grammarSplit[i][j][k]]
                            changed = True
        grammarSplit = newGrammar

    for i in terminales:
        grammarSplit[terminales[i]] = [[i]]
      
    grammar = grammarSplit

    nonTerminals = {}

    nt = 0
    changed = True
    while changed:
        changed = False
        newGrammar = copy.deepcopy(grammar)
        for i in grammar:
            for j in grammar[i]:
                if len(j) > 2:
                    separated = j[1:]
                    if " ".join(separated) not in nonTerminals.keys():
                        nonTerminals[" ".join(separated)] = f"NT{nt}"
                        newGrammar[i].append([j[0], f"NT{nt}"])
                        newGrammar[i].remove(j)
                        nt += 1
                        changed = True
                    else:
                        newGrammar[i].append([j[0], nonTerminals[" ".join(separated)]])
                        newGrammar[i].remove(j)
                        changed = True
        grammar = newGrammar

    for i in nonTerminals:
        grammar[nonTerminals[i]] = [i.split()]

    return grammar