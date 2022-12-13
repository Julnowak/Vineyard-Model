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
    months = num_of_years * 12
    bottle_prices = np.ones((len(ch_types), months))
    c = 0
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

        plt.plot(range(1, months + 1), bottle_prices[c], label=v, linestyle='--', marker='o')
        c += 1

    # month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    np.set_printoptions(precision=2)

    plt.title(f"Zmiana ceny wina na przestrzeni {months} miesięcy")
    plt.legend()
    plt.xlabel('Miesiąc')
    plt.ylabel('Aktualna cena wina')
    plt.grid()
    # plt.xticks(range(1, months + 1), month)
    plt.show()
    return bottle_prices


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


def ocena(sol: np.ndarray, planting_costs: np.ndarray, gather_number: np.ndarray, Isfertilized, soil_type,fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle,  transport_cost,
          bottle_price, mfields_capacity: List, month_grow: np.ndarray,pruning:bool=True,usuwanie:bool=False):
    """

    :param sol:number_of_years * 12 x fields_num x types
    :param planting_costs: grape_types
    :param gather_number:  12
    :param Isfertilized:
    :param soil_type: fieldsNum - Nie soil_type tylko mnoznik jakościowy typu np. 0.7 przemnażany przez oczekiwaną ilośc plonów
    :param fertilizer_bonus:
    :param fertilizer_cost:
    :param harvest_cost:
    :param bottling_cost:
    :param plants_per_bottle:
    :param transport_cost:
    :param bottle_price: grape_types x 12
    :param grape_types:
    :param max_fields_capacity:
    :param month_grow: grape_types x 12
    :return:
    """

    winter = []
    planting_breaks = []

    # Winter months
    # for i in range(sol.shape[0]//12):
    # winter += [0+12*i, 1+12*i, 11+12*i]
    # planting_breaks += [3+12*i, 4+12*i, 5+12*i, 7+12*i, 8+12*i, 9+12*i]

    # Sam przelicznik funkcji celu
    months = sol.shape[0]
    fields = sol.shape[1]
    grape_types = sol.shape[2]

    max_fields_capacity = max(mfields_capacity)  # Do naprawy
    field_grow = np.zeros(shape=(fields, max_fields_capacity))
    grape_type = np.ones(shape=(fields, max_fields_capacity), dtype=int) * -1
    cost = []
    gains = []
    for y in range(months):
        month_cost = 0
        month = y % 12
        gatherings = np.zeros((grape_types))
        for f in range(fields):
            for t in range(grape_types):
                beg=(np.where(grape_type[f] == -1))
                if not beg == []:
                    beg=[0][0]
                # beg = (np.where(grape_type[f] == -1))[0][0]
                end = beg + sol[y][f][t]
                if end > mfields_capacity[f]:
                    end = mfields_capacity[f]
                if month not in [0, 1,  11]:
                    grape_type[f, beg:end] = t

                month_cost = month_cost + planting_costs[t] * sol[y][f][t] + fertilizer_cost
            for p in range(max_fields_capacity):
                if pruning and month == 10:
                    field_grow[f][p] = 0.7 * field_grow[f][p]
                if grape_type[f][p] != -1:
                    if field_grow[f][p] < 1:
                        # growth of wines
                        field_grow[f][p] = field_grow[f][p] + month_grow[month] * \
                                           (soil_type[f][grape_type[f][p]]+Isfertilized * fertilizer_bonus)

                        if field_grow[f][p] > 1:
                            field_grow[f][p] = 1
                        month_cost = month_cost + fertilizer_cost
                    else:
                        # gathering
                        gatherings[grape_type[f][p]] = gatherings[grape_type[f][p]] + \
                                                       gather_number[month]*(soil_type[f][grape_type[f][p]] * Isfertilized * fertilizer_bonus)

                        month_cost = month_cost + fertilizer_cost
                        if usuwanie:
                            field_grow[f][p] = 0
                            grape_type[f][p] = -1


        # butelkowanie i sprzedaz
        harvest_costs = harvest_cost * sum(gatherings)
        bottles = gatherings / plants_per_bottle
        cost_of_postprocessing = np.sum(bottles) * (bottling_cost + transport_cost)
        month_cost = month_cost + cost_of_postprocessing + harvest_costs
        cost.append(month_cost)
        gain = bottles.dot(bottle_price[:, y])
        gains.append(gain)

    return gains, cost



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
    buff=buff//solution.shape[1]
    posy = buff % solution.shape[1]
    buff = buff // solution.shape[2]
    posz = buff
    res=solution.copy();
    if plusmin == 0:
        res[posx][posy][posz]=res[posx][posy][posz]+1
    else:
        res[posx][posy][posz] = res[posx][posy][posz] - 1
    return res

#test  for basicv solution
# sol = np.zeros((2, 3, 4),dtype=int)
# for i in range(2*3*4*2):
#     res=generateSolutionFromNumber(i,sol)
