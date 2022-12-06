import random
import numpy as np
from typing import Union, List, Dict

# Generator rozwiązania początkowego
def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict],
                      min_fields_capacity: Union[List, Dict], number_of_years: int,
                      number_of_vinetypes: int) -> np.ndarray:

    if max_magazine_capacity < sum(min_fields_capacity):
        raise Exception('Magazine capacity too low!')

    fields_num = len(max_fields_capacity)
    solution = np.zeros((fields_num, number_of_years * 12, number_of_vinetypes))

    winter = []
    planting_breaks = []

    # Winter months
    for i in range(number_of_years):
        winter += [0+12*i, 1+12*i, 11+12*i]
        planting_breaks += [3+12*i, 4+12*i, 5+12*i, 7+12*i, 8+12*i, 9+12*i]
    # print(winter)

    for m in range(solution.shape[1]):
        if m in winter or m in planting_breaks:
            continue
        else:
            flaga = True

            typ = [random.randint(0, number_of_vinetypes - 1) for i in range(4)]

            while flaga:

                for fnr in range(fields_num):

                    gen = random.randint(min_fields_capacity[fnr], max_fields_capacity[fnr])
                    solution[fnr][m][typ[fnr]] = gen

                if np.sum(solution[:, m, :]) <= max_magazine_capacity:
                    flaga = False
    return solution


# Test
m = 1000
l = [2000, 1000, 2000]  # Ograniczenia górne
h = [300, 100, 100]  # Ograniczenia dolne
yrs = 1

A = generate_solution(m, l, h, yrs, 4)
print(A)


def ocena(sol: np.ndarray, planting_costs: np.ndarray, gather_number: np.ndarray, Isfertilized, soil_type,
          fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle,
          transport_cost, bottle_price, grape_types, max_fields_capacity: int, month_grow: np.ndarray):
    """

    :param sol:number_of_years * 12 x fields_num x types
    :param planting_costs: grape_types
    :param gather_number: grape_types x 12 x soil_types
    :param Isfertilized:
    :param soil_type: fieldsNum
    :param fertilizer_bonus:
    :param fertilizer_cost:
    :param harvest_cost:
    :param bottling_cost:
    :param plants_per_bottle:
    :param transport_cost:
    :param bottle_price: grape_types x 12
    :param grape_types:
    :param max_fields_capacity:
    :param month_grow: grape_types x 12 x soil_types
    :return:
    """

    # Sam przelicznik funkcji celu
    months = sol.shape[0]
    fields = sol.shape[1]

    field_grow = np.zeros(shape=(fields, max_fields_capacity))
    grape_type = np.ones(shape=(fields, max_fields_capacity), dtype=int)*-1
    solution = 0
    cost = []
    gains = []
    for y in range(months):
        month_cost = 0
        month = y % 12
        gatherings = np.zeros((grape_types))
        for f in range(fields):
            for t in range(grape_types):
                beg = (np.where(grape_type[f]==-1))[0][0]
                end=beg + sol[y][f][t]
                if month not in [0,1,2,3,12,11,10]:
                    grape_type[f, beg:end] = t

                month_cost = month_cost + planting_costs[t] * sol[y][f][t] + fertilizer_cost
            for p in range(max_fields_capacity):
                if grape_type[f][p] != -1:
                    if field_grow[f][p] < 100:
                        # growth of wines
                        field_grow[f][p] = field_grow[f][p] + \
                                           month_grow[grape_type[f][p]][month][soil_type[f]] \
                                           * Isfertilized * fertilizer_bonus
                        if field_grow[f][p]>100:
                            field_grow[f][p]=100
                        month_cost = month_cost + fertilizer_cost

                    else:
                        # gathering
                        gatherings[grape_type[f][p]] = gatherings[grape_type[f][p]] + \
                                                       gather_number[grape_type[f][p]][month][soil_type[f]] \
                                                       * Isfertilized * fertilizer_bonus
                        month_cost = month_cost + fertilizer_cost

        # butelkowanie i sprzedaz
        harvest_costs = harvest_cost * sum(gatherings)
        bottles = gatherings / plants_per_bottle
        cost_of_postprocessing = np.sum(bottles) * (bottling_cost + transport_cost)
        month_cost = month_cost + cost_of_postprocessing + harvest_costs
        cost.append(month_cost)
        gain = bottles.dot(bottle_price[:,month])
        gains.append(gain)

    return gains,cost


# print(ocena(A, 100.00, np.array([[0.90] * A.shape[1], [0.6] * A.shape[1], [0.8] * A.shape[1]]), 1, 0.5, 10, 5, 5, 1, 5,
#             40, 4, 300))
