import numpy as np
from Generators import *
from typing import List

def create_My_Shape(years: int, maxFCap: Union[List, Dict], minFCap: Union[List, Dict], numberOfTypes: int):
    if np.shape(maxFCap) == np.shape(minFCap):
         return (12*years, len(maxFCap), numberOfTypes)
    else:
        raise Exception('ERR:01: shape of fields capacity is not equal')

def my_Plants_Are_Countable(testedOutput: np.ndarray):
    #tacticalCounter = 0
    shape = np.shape(testedOutput)
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                if type(testedOutput[x][y][z]) == np.int32 or type(testedOutput[x][y][z]) == int: pass
                else:
                    raise Exception('ERR:02: plants defy the laws of nature')
    return True

def my_Granary_Is_Overflowing(maxFCap: List, plantsOnField: np.ndarray):
    for x in range(len(plantsOnField)):
        for capacity in range(len(maxFCap)):
            if sum(plantsOnField[x][capacity]) > maxFCap[capacity]:
                raise Exception('ERR:02: The plants have grown beyond the field')
    return True


def test_generate_solution(input: List) -> bool:#, excepted_output: np.ndarray
    test_result = []
    for data in range(0, len(input)):
        result = []
        #print("data: ",data)
        typesNum = len(input[data][0])
        magCap = input[data][1]
        maxFCap = input[data][2]
        minFCap = input[data][3]
        numOYears = input[data][4]

        testedOutput = generate_solution(magCap, maxFCap, minFCap, numOYears, typesNum)
        #print(numberOfGrapes," \n ",max_magazine_cap," \n ",max_field_capacity," \n ",min_field_capacity," \n ",number_of_years)

        #TESTY#
        #czy tablica ma dobry shape
        if np.shape(testedOutput) == create_My_Shape(numOYears,maxFCap,minFCap,typesNum):
            result.append(True)
        #czy wynik jest liczbą
        result.append(my_Plants_Are_Countable(testedOutput))
        #czy pojemność pola jest w porządku
        result.append(my_Granary_Is_Overflowing(maxFCap, testedOutput))

        for x in result:
            if x is not True:
                return False
        return True
def main():
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    magCap = 600
    maxFCap = [800, 800, 800]  # Ograniczenia górne
    minFCap = [100, 100, 100]  # Ograniczenia dolne
    simYears = 2
    numberOfGrapes = len(ch_types)

    #print(np.shape(maxFCap))
    #print(len(maxFCap))
    dataPack = [[ch_types,magCap,maxFCap,minFCap,simYears,numberOfGrapes]]
    print(test_generate_solution(dataPack))

    ch_types = {1: 'falafela', 6: 'twojastara', 8: 'BROWAR_AGH'}
    magCap = 200
    maxFCap = [800, 100, 800, 50]  # Ograniczenia górne
    minFCap = [100, 100, 100, 50]  # Ograniczenia dolne
    simYears = 3
    numberOfGrapes = len(ch_types)

    dataPack_2 = [ch_types,magCap,maxFCap,minFCap,simYears,numberOfGrapes]
    dataPack.append(dataPack_2)
    print(test_generate_solution(dataPack))     #DODAC WARUNEK SPRAWDZAJĄCY POPRAWNOSC NAZWY WINA
    '''
    answer = generate_solution(magCap,maxFCap,minFCap,simYears,numberOfGrapes)
    print(len(answer[0]))
    print("---ANSWER---\n", answer[2][0], answer[2], answer[2][0][2])
    print("shape: ",np.shape(answer))
    x = np.shape(answer)
    y = create_My_Shape(simYears,maxFCap, minFCap, numberOfGrapes)
    print("shape of CREATE_MY_SHAPE: ",create_My_Shape(simYears,maxFCap, minFCap, numberOfGrapes))

    shape = np.shape(answer)
    print(shape, shape[0], shape[1], shape[2])
    #print(answer[0][0][0])
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                pass
                #print(answer[x][y][z])
                #print(type(answer[x][y][z]))

    #print(my_Plants_Are_Countable(answer))
    #print(type(answer[2][0]))
    #for y in range(len(answer)):
     #   for x in range(len(answer[y])):
      #      print(answer[y][x])
    for x in maxFCap:
        print(x)
    '''

if __name__ == '__main__':
    main()

