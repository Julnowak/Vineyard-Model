import random
import numpy as np
from typing import Union, List, Dict
import matplotlib.pyplot as plt


# Generator rozwiązania początkowego
def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict],
                      min_fields_capacity: Union[List, Dict], number_of_years: int,
                      number_of_grapetypes: int) -> np.ndarray:

    if max_magazine_capacity < sum(min_fields_capacity):
        raise Exception('Magazine capacity too low!')

    fields_num = len(max_fields_capacity)
    solution = np.zeros((number_of_years * 12, fields_num, number_of_grapetypes))

    winter = []
    planting_breaks = []

    # Winter months
    for i in range(number_of_years):
        winter += [0 + 12 * i, 1 + 12 * i, 11 + 12 * i]
        planting_breaks += [3 + 12 * i, 4 + 12 * i, 5 + 12 * i, 7 + 12 * i, 8 + 12 * i, 9 + 12 * i]
    # print(winter)

    for m in range(solution.shape[0]):
        if m in winter or m in planting_breaks:
            continue
        else:
            flaga = True
            typ = [random.randint(0, number_of_grapetypes - 1) for _ in range(fields_num)]
            while flaga:
                for fnr in range(fields_num):
                    gen = random.randint(min_fields_capacity[fnr], max_fields_capacity[fnr])
                    solution[m, fnr, typ[fnr]] = gen
                if np.sum(solution[m, :, :]) <= max_magazine_capacity:
                    flaga = False
    return np.array(solution, dtype=int)


def vine_price_generator(ch_types: Dict, num_of_years: int):
    # colors = ['darkorchid','slateblue','darkgoldenrod',
    #           'orangered','crimson','teal','steelblue','firebrick']
    print(ch_types)

    months = num_of_years * 12
    bottle_prices = np.ones((len(ch_types), months))
    c = 0
    # fig, ax = plt.subplots(len(ch_types), 1)
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

    #     np.set_printoptions(precision=2)
    #     if num_of_years <= 2:
    #        ax[c].plot(range(1, months + 1), bottle_prices[c], label=v, linestyle='--', marker='o', c=colors[c])
    #     else:
    #         ax[c].plot(range(1, months + 1), bottle_prices[c], label=v, c=colors[c])
    #     ax[c].grid()
    #     ax[c].legend(loc='best')
        c += 1
    #
    # fig.suptitle(f"Zmiana ceny wina na przestrzeni {months} miesięcy")
    # fig.supylabel('Aktualna cena wina')
    #
    # if months == 12:
    #     month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    #     plt.xticks(range(1, months + 1), month)
    #     fig.supxlabel('Miesiąc')
    # else:
    #     fig.supxlabel('Nr.miesiąca')
    # plt.show()
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


def soil_quality_generator(field_nr: int,years:int, ch_types: Dict, troj = False):
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
                 soil_quality[m, :, :] = sq * 0.7
             else:
                soil_quality[m, :, :] = sq
    else:
        # Trójpolówka
        # Jej działanie to dodawanie jakości dla gleby dla danej, losowej sekwencji
        # Jakość dodawana jednakowa dla wszystkich pól

        trojka = []
        soil_quality = np.zeros((months, field_nr, len(ch_types)))
        rem = np.zeros((months, field_nr, len(ch_types)))
        sq = np.random.uniform(low=0.7, high=0.95, size=(field_nr, len(ch_types)))

        for t in ch_types.keys():
            seq = []
            seq.append(t)
            k = t
            for _ in range(2):
                if len(ch_types)>2:
                    while k in seq:
                        k = random.choice(list(ch_types))
                    seq.append(k)
                else:
                    k = random.choice(list(ch_types))
                    seq.append(k)
            trojka.append(seq)

        trojka = random.choice(trojka)
        cop = trojka.copy()

        for m in range(months):
            if m!= 0:
                if m%3 == 1:
                    rem[m, :, mapk[cop[0]]] += 0.2
                elif m%3 == 2:
                    rem[m, :, mapk[cop[0]]] += 0.2
                elif m%3 == 0:
                    cop = trojka.copy()
                    rem[m, :, mapk[cop[0]]] += 0.2
                cop.pop(0)
            else:
                rem[m,:,:] = 0
                cop.pop(0)

            if m % 12 in [0, 1, 11]:
                soil_quality[m, :, :] = sq * 0.3
            elif m % 12 in [3, 4, 5, 7, 8, 9]:
                soil_quality[m, :, :] = sq * 0.7
            else:
                soil_quality[m, :, :] = sq

        soil_quality = np.add(rem, soil_quality)
    return soil_quality

# test
# ch_types = {1: 'Barbera',5: 'Dolcetto', 6: 'Cortese', 8: 'Erbaluce'}
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
# soil_quality = soil_quality_generator(3, num_of_years, ch_types)
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
def generateSolutionFromNumber(num,solution,gorne,randomFlag=True):
    plusmin=num%2
    buff=num//2

    posx=buff%solution.shape[0]
    buff=buff//solution.shape[0]
    posy = buff % solution.shape[1]
    buff = buff // solution.shape[1]
    posz = buff
    res=solution.copy()
    val=np.sum(res[posx,posy,:])
    res[posx, posy, :]=0
    if  not randomFlag:
        addNum=20
    else:
        addNum=random.randint(5, 30)
    if plusmin == 0:
        res[posx][posy][posz]=val + addNum
    else:
        res[posx][posy][posz] =val - addNum

    if (res<0).any():
        return solution.copy()
    for i in range(len(gorne)):
        if (res[:,i,:]>gorne[i]).any():#hardlimit 500 zasian na pole
            return solution.copy()
    # invaild solution we return basic solution

    return res

#idk if it works
def generateAllsolutions(sol,gorne=[800,800,800]):
    res={}
    for i in range(2*sol.shape[0]*sol.shape[1]*sol.shape[2]):
        buff = generateSolutionFromNumber(i, sol,gorne)
        if not (buff==sol).all():
            res[i]=buff
    return res

# # test  for basicv solution
# sol = np.zeros((2, 3, 4),dtype=int)
# sol[0,:,0]=1

import time

# get the start time
# st = time.time()
# generateAllsolutions(sol)
# end=time.time()
# print(end-st)
