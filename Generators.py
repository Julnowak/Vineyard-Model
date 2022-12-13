import random
import numpy as np
from typing import Union, List, Dict
import matplotlib.pyplot as plt

np.set_printoptions(precision=4)

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
    colors = ['darkorchid','slateblue','darkgoldenrod',
              'orangered','crimson','teal','steelblue','firebrick']
    months = num_of_years * 12
    bottle_prices = np.ones((len(ch_types), months))
    c = 0
    fig, ax = plt.subplots(len(ch_types), 1)
    for _, v in ch_types.items():
        if v == 'Barbera':
            bottle_prices[c, :] = np.random.uniform(low=30.01, high=45.12, size=(1, months))
        elif v == 'Chardonnay':
            bottle_prices[c, :] = np.random.uniform(low=30.01, high=45.12, size=(1, months))
        elif v == 'Nebbiolo':
            bottle_prices[c, :] = np.random.uniform(low=83.01, high=89.65, size=(1, months))
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

        np.set_printoptions(precision=2)
        if num_of_years <= 2:
           ax[c].plot(range(1, months + 1), bottle_prices[c], label=v, linestyle='--', marker='o', c=colors[c])
        else:
            ax[c].plot(range(1, months + 1), bottle_prices[c], label=v, c=colors[c])
        ax[c].grid()
        ax[c].legend(loc='best')
        c += 1

    fig.suptitle(f"Zmiana ceny wina na przestrzeni {months} miesięcy")
    fig.supylabel('Aktualna cena wina')

    if months == 12:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        plt.xticks(range(1, months + 1), month)
        fig.supxlabel('Miesiąc')
    else:
        fig.supxlabel('Nr.miesiąca')
    plt.show()
    return bottle_prices

def plant_price_generator(ch_types: Dict):
    planting_prices = np.ones((len(ch_types), 1))
    c = 0
    for _, v in ch_types.items():
        if v == 'Barbera':
            planting_prices[c, :] = np.random.uniform(low=5.00, high=8.50)
        elif v == 'Chardonnay':
            planting_prices[c, :] = np.random.uniform(low=5.04, high=8.50)
        elif v == 'Nebbiolo':
            planting_prices[c, :] = np.random.uniform(low=9.50, high=12.99)
        elif v == 'Arneis':
            planting_prices[c, :] = np.random.uniform(low=4.50, high=6.20)
        elif v == 'Dolcetto':
            planting_prices[c, :] = np.random.uniform(low=7.00, high=8.50)
        elif v == 'Cortese':
            planting_prices[c, :] = np.random.uniform(low=6.00, high=7.00)
        elif v == 'Grignolino':
            planting_prices[c, :] = np.random.uniform(low=5.70, high=6.70)
        elif v == 'Erbaluce':
            planting_prices[c, :] = np.random.uniform(low=13.20, high=13.70)
        else:
            raise Exception(f'There is no grape type: "{v}"')



def soil_quality_generator(field_nr: int, ch_types: Dict):
    """
    :param field_nr: number of all available fields
    :param ch_types: Types of grapes that have been chosen by user
    :return: a matrix of soil quality for each field, depending on grape type in % [0.00]
    """

    np.set_printoptions(precision=2)

    soil_quality = np.random.uniform(low=0.7, high=0.95, size=(field_nr, len(ch_types)))
    return soil_quality


# Test
# m = 1000
# l = [2000, 1000, 2000]  # Ograniczenia górne
# h = [300, 100, 100]  # Ograniczenia dolne
# yrs = 1

# A = generate_solution(m, l, h, yrs, 4)
# print(A)

#ok so last bit tells us if its adding or subtracting so
#oposite is jut makeing number odd or even
def generateAntiNum(num):
    if num %2 ==0:
        return +num
    else:
        return num - 1

#num should be in range from 0 to shape[0]*shape[1]*shape[2]*2
def generateSolutionFromNumber(num,solution):
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
    if plusmin == 0:

        res[posx][posy][posz]=val + 5
    else:
        res[posx][posy][posz] =val - 5

    if not (res<0).any():
        return res
    # invaild solution we return basic solution
    return solution.copy()

#idk if it works
def generateAllsolutions(sol):
    res={}
    for i in range(2*sol.shape[0]*sol.shape[1]*sol.shape[2]):
        buff = generateSolutionFromNumber(i, sol)
        if not (buff==sol).all():
            res[i]=buff
    return res
# test  for basicv solution
sol = np.zeros((2, 3, 4),dtype=int)
sol[0,:,0]=1

import time

# get the start time
# st = time.time()
# generateAllsolutions(sol)
# end=time.time()
# print(end-st)
