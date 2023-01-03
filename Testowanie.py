import numpy as np
from DBFor_Testing import *
from Generators import *
from typing import List

#TODO
#Poprawić testy dla trójpolowki
#test_generateAntiNum
#test_generateSolutionFromNumber
#test_generateAllsolutions


def check_soils_TROJ(intput):
    for mont in range(len(intput)):
        if mont%12 in [0, 1, 11]:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < (0.7*0.3) or round(intput[mont][x][y], 2) > (0.95*0.3):
                        return "ERR:08: trojpolowka mods are not correct"
                    else: pass
                        # print("ODP:month: ",mont," x= ",x," y= ",y, " ==== ", intput[mont][x][y])
        elif mont%12 in [3, 4, 5, 7, 8, 9]:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < (0.7*0.7) or round(intput[mont][x][y], 2) > (0.95*0.7):
                        return "ERR:08: trojpolowka mods are not correct"
                    else: pass
                        # print("ODP:month: ", mont, " x= ", x, " y= ", y, " ==== ", intput[mont][x][y])
        else:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < 0.7 or round(intput[mont][x][y], 2) > 0.95:
                        return "ERR:08: trojpolowka mods are not correct"
                    else: pass
                        #print("ODP:month: ", mont, " x= ", x, " y= ", y, " ==== ", intput[mont][x][y])
    return True

def check_soils(intput):
    for mont in range(len(intput)):
        if mont%12 in [0, 1, 11]:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < (0.7*0.3) or round(intput[mont][x][y], 2) > (0.95*0.3):
                        return "ERR:07: soil mods are not correct"
                    else: pass
                        # print("ODP:month: ",mont," x= ",x," y= ",y, " ==== ", intput[mont][x][y])
        elif mont%12 in [3, 4, 5, 7, 8, 9]:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < (0.7*0.7) or round(intput[mont][x][y], 2) > (0.95*0.7):
                        return "ERR:07: soil mods are not correct"
                    else: pass
                        # print("ODP:month: ", mont, " x= ", x, " y= ", y, " ==== ", intput[mont][x][y])
        else:
            for x in range(len(intput[mont])):
                for y in range(len(intput[mont][x])):
                    if round(intput[mont][x][y], 2) < 0.7 or round(intput[mont][x][y], 2) > 0.95:
                        return "ERR:07: soil mods are not correct"
                    else: pass
                        #print("ODP:month: ", mont, " x= ", x, " y= ", y, " ==== ", intput[mont][x][y])
    return True

def my_Wines_Are_Real(chtypes:dict):
    names = {1:'Barbera',2:'Chardonnay',3:'Nebbiolo',4:'Arneis',5:'Dolcetto',6:'Cortese',7:'Grignolino',8:'Erbaluce'}
    for x in chtypes.values():
        if x not in names.values():
            return "ERR:01: tested wine type not exist"
    return True

def check_My_Shape(years: int, maxFCap: Union[List, Dict], minFCap: Union[List, Dict], numberOfTypes: int, testedOutput):
    if np.shape(maxFCap) == np.shape(minFCap):
         if np.shape(testedOutput) == (12*years, len(maxFCap), numberOfTypes):
             return True
         print("SHAPE NIE PRZESZEDL: ", np.shape(testedOutput),": < - > :", (12*years, len(maxFCap), numberOfTypes))
    return 'ERR:02: shape of fields capacity is not equal'

def my_Plants_Are_Countable(testedOutput: np.ndarray):
    shape = np.shape(testedOutput)
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                if type(testedOutput[x][y][z]) == np.int32 or type(testedOutput[x][y][z]) == int: pass
                else:
                    return 'ERR:03: plants defy the laws of nature'
    return True

def my_Soil_Are_Soilable(testedOutput: np.ndarray):
    shape = np.shape(testedOutput)
    for x in range(shape[0]):
        for y in range(shape[1]):
            for z in range(shape[2]):
                if type(testedOutput[x][y][z]) == np.float64 or type(testedOutput[x][y][z]) == float:
                    pass
                else:
                    return 'ERR:04: soils not working or not found'
    return True

def my_Granary_Is_Overflowing(maxFCap: List, plantsOnField: np.ndarray):
    for x in range(len(plantsOnField)):
        for capacity in range(len(maxFCap)):
            if sum(plantsOnField[x][capacity]) > maxFCap[capacity]:
                return 'ERR:05: The plants have grown beyond the field'
    return True

def check_price_type(intput):
    for x in range(len(intput)):
        if type(intput[x]) == float or type(intput[x]) == np.float64:
            return True
        else:
            return "ERR:06: your price is not legal price"

def explain_my_tests(test_result, name):
    print("___.: ",name," :.___")
    for x in range(len(test_result)):
        print("TEST: [",x+1,"]",test_result[x],"")

def test_generate_solution(intput):
    test_result = []
    for data in range(0, len(intput)):
        result = []
        types = intput[data][0]
        typesNum = len(intput[data][0])
        magCap = intput[data][1]
        maxFCap = intput[data][2]
        minFCap = intput[data][3]
        numOYears = intput[data][4]
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
    return explain_my_tests(test_result,"GEN. SOLUTION")

def test_plant_price_generator(intput):
    test_result = []
    for data in range(0, len(intput)):
        result = []
        types = intput[data][0]


                #TESTY#
    # Czy nazwy wina się zgadzają
        if my_Wines_Are_Real(types) is True:
            testedOutput = plant_price_generator(types)
        result.append(my_Wines_Are_Real(types))
    # Czy wygenerowane ceny są liczbami [floatami]
        if "testedOutput" in locals():
            for x in range(len(testedOutput)):
                if type(testedOutput[x]) == float or type(testedOutput[x]) == np.float64:
                    result.append(True)
                else:
                    result.append("ERR:06: your price is not legal price")
                    break
            test_result.append(result)
        else:
            test_result.append("ERR:404: TESTED_OUTPUT was not found ")
    return explain_my_tests(test_result,"PLANT PRICE")

def test_soil_quality_generator_withOUT3polowka(intput):
    test_result = []
    for data in range(len(intput)):
        result = []
        ch_types = intput[data][0]
        maxFCap = intput[data][2]
        field_nr = len(maxFCap)
        minFCap = intput[data][3]
        years = intput[data][4]
        troj = False

        testedOutput =  soil_quality_generator(field_nr, years, ch_types, troj)

                    # TESTY #
    #czy tablica ma dobry shape
        result.append(check_My_Shape(years, maxFCap, minFCap, len(ch_types), testedOutput))
    # czy wygenerowane współczynniki mieszczą się w dobrym przedziale
        result.append(check_soils(testedOutput))
    # czy to na pewno liczby float + (mają dwa miejsca po przecinku?)
        result.append(my_Soil_Are_Soilable(testedOutput))

        test_result.append(result)
    return explain_my_tests(test_result, "SOIL QUALITY WITHOUT 'TROJPOLOWKA'")

def test_soil_quality_generator_with3polowka(intput):
    test_result = []
    for data in range(len(intput)):
        result = []
        ch_types = intput[data][0]
        maxFCap = intput[data][2]
        field_nr = len(maxFCap)
        minFCap = intput[data][3]
        years = intput[data][4]
        troj = True

        testedOutput = soil_quality_generator(field_nr, years, ch_types, troj)

                     # TESTY #
            # czy tablica ma dobry shape
        result.append(check_My_Shape(years, maxFCap, minFCap, len(ch_types), testedOutput))
            # czy wygenerowane współczynniki mieszczą się w dobrym przedziale
        result.append(check_soils_TROJ(testedOutput))
            # czy to na pewno liczby float + (mają dwa miejsca po przecinku?)
        result.append(my_Soil_Are_Soilable(testedOutput))

        test_result.append(result)
    return explain_my_tests(test_result, "SOIL QUALITY WITH 'TROJPOLOWKA'")

def test_generateAntiNum():
    pass

def test_generateSolutionFromNumber():
    pass

def test_generateAllsolutions():
    pass



def main():
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    magCap = 600
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
    # ------------------------------TESTY-------------------------------------
    test_generate_solution(make_Testing_Pack())
    test_plant_price_generator(make_Testing_Pack())
    test_soil_quality_generator_withOUT3polowka(make_Testing_Pack())
    # ------------------------------------------------------------------------

    output = soil_quality_generator(len(maxFCap), simYears, ch_types, True)
    print(output)
if __name__ == '__main__':
    main()

