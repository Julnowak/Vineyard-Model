import numpy as np
from DBFor_Testing import *
from Generators import *
from typing import List

def my_Wines_Are_Real(chtypes:dict):
    names = {1:'Barbera',2:'Chardonnay',3:'Nebbiolo',4:'Arneis',5:'Dolcetto',6:'Cortese',7:'Grignolino',8:'Erbaluce'}
    for x in chtypes.values():
        if x not in names.values():
            return "ERR:04: tested wine type not exist"
    return True

def check_My_Shape(years: int, maxFCap: Union[List, Dict], minFCap: Union[List, Dict], numberOfTypes: int, testedOutput):
    if np.shape(maxFCap) == np.shape(minFCap):
         if np.shape(testedOutput) == (12*years, len(maxFCap), numberOfTypes):
             return True
    return 'ERR:01: shape of fields capacity is not equal'

def my_Plants_Are_Countable(testedOutput: np.ndarray):
    shape = np.shape(testedOutput)
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                if type(testedOutput[x][y][z]) == np.int32 or type(testedOutput[x][y][z]) == int: pass
                else:
                    return 'ERR:02: plants defy the laws of nature'
    return True

def my_Granary_Is_Overflowing(maxFCap: List, plantsOnField: np.ndarray):
    for x in range(len(plantsOnField)):
        for capacity in range(len(maxFCap)):
            if sum(plantsOnField[x][capacity]) > maxFCap[capacity]:
                return 'ERR:03: The plants have grown beyond the field'
    return True


def test_generate_solution(input):
    test_result = []
    for data in range(0, len(input)):
        result = []
        types = input[data][0]
        typesNum = len(input[data][0])
        magCap = input[data][1]
        maxFCap = input[data][2]
        minFCap = input[data][3]
        numOYears = input[data][4]
        testedOutput = generate_solution(magCap, maxFCap, minFCap, numOYears, typesNum)
                    #TESTY#
            #czy tablica ma dobry shape
        result.append(check_My_Shape(numOYears, maxFCap, minFCap, typesNum, testedOutput))
            #czy wynik jest liczbą
        result.append(my_Plants_Are_Countable(testedOutput))
            #czy pojemność pola jest w porządku
        result.append(my_Granary_Is_Overflowing(maxFCap, testedOutput))
            #czy nazwy się zgadzają
        result.append(my_Wines_Are_Real(types))
            #podsumowanie dla pakietu
        test_result.append(result)
        #pełny wynik dla paczki danych
    return explain_my_tests(test_result)

def explain_my_tests(test_result):
    for x in range(len(test_result)):
        print("TEST: [",x,"]",test_result[x],"")





def main():
    test_generate_solution(make_Testing_Pack())
if __name__ == '__main__':
    main()

