import random
import numpy as np
from typing import Union, List, Dict
import matplotlib.pyplot as plt
import sys

# Generator rozwiązania początkowego - działa
def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict],
                      min_fields_capacity: Union[List, Dict], number_of_years: int,
                      number_of_grapetypes: int,store_needs, sol_flag: int,fields_num=None) -> np.ndarray:

    if fields_num is None:
        fields_num = len(min_fields_capacity)

    for x in range(len(min_fields_capacity)):
        if min_fields_capacity[x] > max_fields_capacity[x]:
            print('TU PROBLEM - gensol')
            raise Exception('Cannot set minimum capacity of field greater than maximum capacity of field.')


    solution = np.zeros((number_of_years * 12, fields_num, number_of_grapetypes))

    winter = []
    planting_breaks = []

    # Winter months
    for i in range(number_of_years):
        winter += [0 + 12 * i, 1 + 12 * i, 11 + 12 * i]
        planting_breaks += [3 + 12 * i, 4 + 12 * i, 5 + 12 * i, 7 + 12 * i, 8 + 12 * i, 9 + 12 * i]

    for m in range(solution.shape[0]):
        if m in winter or m in planting_breaks:
            continue
        else:
            if sol_flag == 1:
                flaga = True
                typ = [random.randint(0, number_of_grapetypes - 1) for _ in range(fields_num)]
                print(typ)
                it =0
                while flaga:
                    for fnr in range(fields_num):
                        gen = random.randint(min_fields_capacity[fnr], max_fields_capacity[fnr])
                        solution[m][ fnr][typ[fnr]] = gen
                    it+=1
                    if np.sum(solution[m, :, :]) <= max_magazine_capacity or it == 10:
                        flaga = False
            elif sol_flag == 2: # 50% ograniczeń górnych
                typ = [random.randint(0, number_of_grapetypes - 1) for _ in range(fields_num)]
                for fnr in range(fields_num):
                    gen = max_fields_capacity[fnr]
                    if gen*0.5 < min_fields_capacity[fnr]:
                        mamk = min_fields_capacity[fnr]
                    else:
                        mamk = int(gen*0.5)
                    solution[m, fnr, typ[fnr]] = mamk
            elif sol_flag == 3: # Tylko ograniczenia dolne
                typ = [random.randint(0, number_of_grapetypes - 1) for _ in range(fields_num)]
                for fnr in range(fields_num):
                    gen = min_fields_capacity[fnr]
                    if gen == 0:
                        mamk = gen + np.ceil(max_fields_capacity[fnr]*0.1)
                    else:
                        mamk = gen
                    solution[m, fnr, typ[fnr]] = mamk
            elif sol_flag == 4: # Nakierowany na zapotrzebowanie
                typ = list(range(number_of_grapetypes))
                for fnr in range(fields_num):
                    gen = store_needs[fnr]
                    if gen < min_fields_capacity[fnr]:
                        gen = min_fields_capacity[fnr]
                    elif gen > max_fields_capacity[fnr]:
                        gen = max_fields_capacity[fnr]

                    solution[m, fnr, typ[fnr]] = gen
    return np.array(solution, dtype=int)


def vine_price_generator(ch_types: Dict, num_of_years: int):

    months = num_of_years * 12
    bottle_prices = np.ones((len(ch_types), months))
    c = 0
    for _, v in ch_types.items():
        if v == 'Barbera':
            bottle_prices[c, :] = np.random.uniform(low=30.01, high=45.12, size=(1, months))
        elif v == 'Chardonnay':
            bottle_prices[c, :] = np.random.uniform(low=30.01, high=45.12, size=(1, months))
        elif v == 'Nebbiolo':
            bottle_prices[c, :] = np.random.uniform(low=53.01, high=55.65, size=(1, months))
        elif v == 'Arneis':
            bottle_prices[c, :] = np.random.uniform(low=66.01, high=71.12, size=(1, months))
        elif v == 'Dolcetto':
            bottle_prices[c, :] = np.random.uniform(low=58.50, high=63.50, size=(1, months))
        elif v == 'Cortese':
            bottle_prices[c, :] = np.random.uniform(low=60.11, high=65.57, size=(1, months))
        elif v == 'Grignolino':
            bottle_prices[c, :] = np.random.uniform(low=50.00, high=55.19, size=(1, months))
        elif v == 'Erbaluce':
            bottle_prices[c, :] = np.random.uniform(low=132.00, high=137.00, size=(1, months))
        else:
            raise Exception(f'There is no grape type: "{v}"')
        c += 1

    return bottle_prices


def plant_price_generator(ch_types: Dict):
    planting_prices = np.ones((len(ch_types), 1))
    c = 0
    for _, v in ch_types.items():
        if v == 'Barbera':
            planting_prices[c,:] = np.random.uniform(low=10.00, high=15.50)
        elif v == 'Chardonnay':
            planting_prices[c, :] = np.random.uniform(low=10.04, high=15.50)
        elif v == 'Nebbiolo':
            planting_prices[c, :] = np.random.uniform(low=17.64, high=18.38)
        elif v == 'Arneis':
            planting_prices[c, :] = np.random.uniform(low=22.50, high=23.67)
        elif v == 'Dolcetto':
            planting_prices[c, :] = np.random.uniform(low=19.48, high=19.90)
        elif v == 'Cortese':
            planting_prices[c, :] = np.random.uniform(low=20.00, high=22.00)
        elif v == 'Grignolino':
            planting_prices[c, :] = np.random.uniform(low=16.50, high=18.20)
        elif v == 'Erbaluce':
            planting_prices[c, :] = np.random.uniform(low=43.56, high=47.70)
        else:
            raise Exception(f'There is no grape type: "{v}"')
        c += 1

    return planting_prices.reshape((len(ch_types)))


def soil_quality_generator(field_nr: int, years:int, ch_types: Dict, troj = False):
    """
    :param field_nr: number of all available fields
    :param ch_types: Types of grapes that have been chosen by user
    :return: a matrix of soil quality for each field, depending on grape type in % [0.00]
    """

    mapk = dict()
    count = 0
    for k in ch_types.keys():
        mapk[k] = count
        count +=1

    np.set_printoptions(precision=2)
    months = 12*years
    if not troj:
         soil_quality = np.zeros((months, field_nr, len(ch_types)))
         sq = np.random.uniform(low=0.7, high=0.95, size=(field_nr, len(ch_types)))
         for m in range(months):
             if m%12 in [0,1,11]:
                 soil_quality[m, :, :] = sq * 0.3
             elif m%12 in [3,4,5,7,8,9]:
                 soil_quality[m, :, :] = sq * 0.4
             else:
                soil_quality[m, :, :] = sq
    else:
        # Trójpolówka
        # Jej działanie to dodawanie jakości dla gleby dla danej, losowej sekwencji
        # Jakość dodawana jednakowa dla wszystkich pól

        trojlist = []
        soil_quality = np.zeros((months, field_nr, len(ch_types)))
        rem = np.zeros((months, field_nr, len(ch_types)))
        sq = np.random.uniform(low=0.7, high=0.95, size=(field_nr, len(ch_types)))

        for t in ch_types.keys():
            seq = []
            seq.append(t)
            k = t
            for i in range(2):
                if len(ch_types)>2:
                    while k in seq:
                        k = random.choice(list(ch_types))
                    seq.append(k)
                elif len(ch_types)==2:
                    seq.append(list(ch_types)[i])

                else:
                    k = random.choice(list(ch_types))
                    seq.append(k)
            trojlist.append(seq)
        mix=[]

        for i in range(field_nr):
            mix.append(random.choice(trojlist))

        # Sekwencje dla każdego pola
        cop = mix.copy()

        for m in range(months):
            if m%12 in [2, 6, 10]:
                for f in range(field_nr):
                    if m%12 == 2:
                        if m!= 2:
                            rem[m][f][mapk[cop[f][0]]] += 0.25
                    if m%12 == 6:
                        rem[m][f][mapk[cop[f][1]]] += 0.25
                    if m%12 == 10:
                        rem[m][f][mapk[cop[f][2]]] += 0.25

            else:
                rem[m,:,:] = 0

            if m % 12 in [0, 1, 11]:
                soil_quality[m, :, :] = sq * 0.3
            elif m % 12 in [3, 4, 5, 7, 8, 9]:
                soil_quality[m, :, :] = sq * 0.4
            else:
                soil_quality[m, :, :] = sq
        soil_quality = np.add(rem, soil_quality)

    soil_quality[soil_quality>1] = 1.0

    return soil_quality

# test
# ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}
# num_of_years = 2
# types_of_grapes = 3
# num_of_fields = 3
# soil_types = 3
#
# m = 600
# l = [800, 800, 800]  # Ograniczenia górne
# h = [100, 100, 100]  # Ograniczenia dolne
#
# sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
#
#
# planting_cost = plant_price_generator(ch_types)
#
# epsilon = 0.01
# max_iter = 50
# IsFertilized = 1
# soil_quality = soil_quality_generator(3, num_of_years, ch_types,True)
# print(soil_quality)

#ok so last bit tells us if its adding or subtracting so
#oposite is jut makeing number odd or even
def generateAntiNum(num):
    if num %2 ==0:
        return num+1
    else:
        return num - 1

#num should be in range from 0 to shape[0]*shape[1]*shape[2]*2
#num defines direction of solution but value can be random
def generateSolutionFromNumber(num,solution,gorne,randomFlag,min,max,norm):
    plusmin=num%2
    buff=num//2

    posx=buff%solution.shape[0]
    buff=buff//solution.shape[0]
    posy = buff % solution.shape[1]
    buff = buff // solution.shape[1]
    res=solution.copy()
    posz = buff
    val=np.sum(res[posx,posy,:])
    res[posx, posy, :]=0
    if  not randomFlag:
        addNum=norm
    else:
        addNum=random.randint(min, max)
    if plusmin == 0 and posx not in [0,1,3,4,5,7,8,9,11]:
        res[posx][posy][posz]=val + addNum
    elif posx not in [0,1,3,4,5,7,8,9,11]:
        res[posx][posy][posz] =val - addNum
    else:
        res[posx][posy][posz] = 0

    if (res<0).any():
        return solution.copy()
    for i in range(len(gorne)):
        if (res[:,i,:]>gorne[i]).any():
            return solution.copy()
    # invaild solution we return basic solution

    return res

def przelicz(num,s0,s1):
    plusmin = num % 2
    buff = num // 2

    posx = buff % s0
    buff = buff // s0
    posy = buff % s1
    buff = buff // s1
    posz = buff
    return plusmin,posx,posy,posz

# number of solutions should be between 0.1 and 1
def generateAllsolutions(sol,gorne,numberofsolutions,rand,min,max,norm):
    res={}
    randTable=np.random.rand(2*sol.shape[0]*sol.shape[1]*sol.shape[2])
    for i in range(len(randTable)):
        if randTable[i]>=numberofsolutions:
            continue
        buff = generateSolutionFromNumber(i, sol,gorne,rand,min,max,norm)
        if not (buff==sol).all():
            res[i]=buff
    return res

import time

def gen(sol):
    res={}
    lista = [2,6,10]
    counter=0
    for m in range(sol.shape[0]):
        if m%12 in lista:
            for f in range(sol.shape[1]):
                for t in range(sol.shape[2]):
                    if sol[m][f][t] != 0:

                        res[counter] = sol.copy()
                        res[counter][m][f][t] += 30
                        counter += 1
                        res[counter] = sol.copy()
                        res[counter][m][f][t] -= 30
                        counter += 1


    return res

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

# print(gen(testowe))