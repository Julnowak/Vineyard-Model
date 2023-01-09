import numpy as np
from DBFor_Testing import *
from Generators import *
from typing import List
from App import *
#from tabu_search import * #To do testow/ w wersji koncowej do wywalenia

#TODO
#test_generateSolutionFromNumber
#test_generateAllsolutions

#test_TabuSearch


def check_soils_TROJ(intput):
    for mont in range(len(intput)):
        for x in range(len(intput[mont])):
            for y in range(len(intput[mont][x])):
                if round(intput[mont][x][y], 2) < 0.20 or round(intput[mont][x][y], 2) > 1.0:
                    return "ERR:08: trojpolowka mods are not correct soil = ",intput[mont][x][y]
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
         #print("SHAPE NIE PRZESZEDL: ", np.shape(testedOutput),": < - > :", (12*years, len(maxFCap), numberOfTypes))
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

def my_Plants_Are_CountableV2(testedOutput: np.ndarray):
    for ver in range(0, 10):
        output = testedOutput[ver]
        shape = np.shape(output)
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    if type(output[x][y][z]) == np.int32 or type(output[x][y][z]) == int: pass
                    else:
                        return 'ERR:11: gen function problem'
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

def antiNumtest(aftergen, beforegen):
    if beforegen-1 == aftergen or beforegen+1 == aftergen:
        return True
    return " ERR :10: sth is not good with numbers"

def explain_my_tests(test_result, name):
    print("___.: ",name," :.___")
    for x in range(len(test_result)):
        print("TEST: [",x+1,"]",test_result[x],"")

def isInt(intput: int):
    if type(intput) == np.int32 or type(intput) == int:
        return True
    return "WARR:01: number type is not INT"

def isFloat(intput: float):
    if type(intput) == np.float64 or type(intput) == float:
        return True
    return "WARR:01: number type is not FLOAT"

def checkMyThirdies(gen_sol, testedOutput):
    pass
    lista = [2, 6, 10]
    for m in range(gen_sol.shape[0]):
        if m%12 in lista:
            for f in range(gen_sol.shape[1]):
                for t in range(gen_sol.shape[2]):
                    pass

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
        store_needs = intput[data][5]
        sol_Flag = intput[data][6]
        testedOutput = generate_solution(magCap, maxFCap, minFCap, numOYears, typesNum,store_needs, sol_Flag)
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

def test_generateAntiNum(intput):   #dla uproszczenia paczki danych, biorę liczbę miesięcy
    test_result = []
    for data in range(len(intput)):
        result = []
        number = (intput[data][4])*12

        output = generateAntiNum(number)

                    # TEST #
    # czy 'numer' to liczba float
        result.append(isFloat(output))
    # czy numer to liczba int
        result.append(isInt(output))
    # czy spełnia założenie dodania 1 gdy pażysta / odjęcia 1 gdzy nieparzysta
        result.append(antiNumtest(number, output))

        test_result.append(result)
    return explain_my_tests(test_result, "GENERATE ANTINUM")

def test_generateSolutionFromNumber():
    pass

def test_generateAllsolutions():
    pass

def test_gen(intput):
    test_result = []
    for data in range(0, len(intput)):
        result = []
        types = intput[data][0]
        typesNum = len(intput[data][0])
        magCap = intput[data][1]
        maxFCap = intput[data][2]
        minFCap = intput[data][3]
        numOYears = intput[data][4]
        store_needs = intput[data][5]
        sol_Flag = intput[data][6]

        gen_sol = generate_solution(magCap, maxFCap, minFCap, numOYears, typesNum, store_needs, sol_Flag)
        testedOutput = gen(gen_sol)
                          # TESTY #
        # czy liczby są ok
        result.append(my_Plants_Are_CountableV2(testedOutput))

        test_result.append(result)

    return explain_my_tests(test_result, "GEN")

def test_tabuSearch():
    pass

# ------------------------------------------------------------------------
'''
def tabuData():
    f = open("Wyniki/Tabele/test.out", 'w')
    sys.stdout = f

    np.set_printoptions(precision=4)

    testowe = np.array([[[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 300, 0],
                         [307, 0, 0],
                         [0, 258, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 300],
                         [0, 0, 372],
                         [275, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]],

                        [[301, 0, 0],
                         [0, 0, 205],
                         [0, 0, 351]],

                        [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]])

    epsilon = 0.01
    max_iter = 20
    num_of_years = 1
    magazine_capacity = 600
    magazine_cost = 2
    plants_per_bottle = 1
    transport_cost = 2
    bottling_cost = 2
    harvest_cost = 2
    ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}
    IsFertilized = 1
    fertilizer_bonus = 0.05
    fertilizer_cost = 2
    store_needs = [100, 100, 100]

    planting_cost = np.array([14.13, 13.53, 17.66])

    soil_quality = np.array([[[0.28, 0.25, 0.26],
                              [0.22, 0.23, 0.25],
                              [0.22, 0.25, 0.27]],

                             [[0.28, 0.25, 0.26],
                              [0.22, 0.23, 0.25],
                              [0.22, 0.25, 0.27]],

                             [[0.93, 0.83, 0.87],
                              [0.73, 0.76, 0.82],
                              [0.73, 0.83, 0.89]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.93, 0.83, 0.87],
                              [0.73, 0.76, 0.82],
                              [0.73, 0.83, 0.89]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.65, 0.58, 0.61],
                              [0.51, 0.53, 0.57],
                              [0.51, 0.58, 0.63]],

                             [[0.93, 0.83, 0.87],
                              [0.73, 0.76, 0.82],
                              [0.73, 0.83, 0.89]],

                             [[0.28, 0.25, 0.26],
                              [0.22, 0.23, 0.25],
                              [0.22, 0.25, 0.27]]])

    vineprice = [[41.03, 39.55, 36.31, 37.88, 40.64, 38.16, 43., 42.15, 37.73, 42.77, 34.36, 37.65],
                 [36.83, 43.16, 39.84, 41.39, 31.93, 36.5, 37.8, 39.06, 36.28, 42.55, 42.96, 30.38],
                 [55.46, 53.59, 53.75, 53.68, 53.72, 54.84, 53.17, 55.56, 55.59, 53.18, 53.63, 53.04]]

    def tabu_search(beg_sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    tabu_length=100, max_iter=500, epsilon=0.1):

        gain, loss = ocena(beg_sol, planting_cost,
                           IsFertilized, soil_quality,
                           fertilizer_bonus, fertilizer_cost,
                           harvest_cost, bottling_cost,
                           plants_per_bottle, transport_cost,
                           vineprice, magazine_cost, magazine_capacity, store_needs)

        # sol_present_yourself(gain, loss, beg_sol, ch_types)

        TL = []
        avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[
            2]))  # pamiec srednioteminowa zlicza rozwiazania dane
        streak = 0
        streaknum = -1

        solution = beg_sol
        past_sol = sum(gain) - sum(loss)

        # Najlepsze
        bs_solution = solution.copy()
        bs = sum(gain) - sum(loss)

        gain_rem = 0
        loss_rem = 0

        stop_iter = False
        stop_eps = False
        counter = 0

        limsta = []

        while not (stop_iter or stop_eps):

            mapa = gen(solution)
            # print(mapa)
            # print('\n-----------------------------------\n')
            neigh = [k for k, _ in mapa.items()]

            n_rem = None
            value = None
            maxi = -np.inf
            maxval = -np.inf

            for n in neigh:

                gain, loss = ocena(mapa[n], planting_cost,
                                   IsFertilized, soil_quality,
                                   fertilizer_bonus, fertilizer_cost,
                                   harvest_cost, bottling_cost,
                                   plants_per_bottle, transport_cost,
                                   vineprice, magazine_cost, magazine_capacity, store_needs)

                # + funkcja aspiracji
                value = sum(gain) - sum(loss)
                if n not in TL and value - avgMemory[n] * 2 > maxi:
                    maxi = sum(gain) - sum(loss) - avgMemory[n] * 2  # no jak było wybierane to mniej
                    maxval = sum(gain) - sum(loss)
                    gain_rem = gain
                    loss_rem = loss
                    n_rem = n
            # print(n_rem)

            limsta.append(maxval)

            avgMemory[n_rem] = avgMemory[n_rem] + 1
            if n_rem == streaknum:
                streak = streak + 1
            else:
                streaknum = n_rem
                streak = 1
            if streak > 99999:
                # wybralismy 9999 to smao rozw zróbmy coś dzikiego
                pass
            limsta.append(value)

            if maxval >= bs:
                solution = mapa[n_rem].copy()
            else:
                solution = mapa[n_rem].copy()

            print("pawel:", len(TL), tabu_length)

            if len(TL) < tabu_length:
                TL.append(generateAntiNum(n_rem))
            else:
                TL.pop(0)
                TL.append(generateAntiNum(n_rem))

            if counter > max_iter:
                stop_iter = True

            if abs(past_sol - maxval) <= epsilon:
                stop_eps = True

            past_sol = maxval

            counter += 1
            print(counter)
            if counter >= max_iter:
                stop_iter = True

        print(limsta)

        plt.plot(limsta)
        plt.title('Wykres wartości funkcji celu')
        plt.show()

        # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

        return bs_solution

    tabu_search(testowe, planting_cost,
                IsFertilized, soil_quality,
                fertilizer_bonus, fertilizer_cost,
                harvest_cost, bottling_cost,
                plants_per_bottle, transport_cost,
                vineprice, magazine_cost, magazine_capacity, store_needs, ch_types)

    f.close()
'''

def main():
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    magCap = 600
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
    sol_flag = 1
    store_needs = [150, 150, 150]
    # ------------------------------TESTY-------------------------------------
    test_generate_solution(make_Testing_Pack())
    test_plant_price_generator(make_Testing_Pack())
    test_soil_quality_generator_withOUT3polowka(make_Testing_Pack())
    test_soil_quality_generator_with3polowka(make_Testing_Pack())
    test_generateAntiNum(make_Testing_Pack())
    test_gen(make_Testing_Pack())
    # ------------------------------------------------------------------------


if __name__ == '__main__':
    main()

