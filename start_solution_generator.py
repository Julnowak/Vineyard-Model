import random
import numpy as np
from typing import Union, List, Dict


def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict],
                      min_fields_capacity: Union[List, Dict], number_of_years: int) -> np.ndarray:
    """
    :param max_magazine_capacity:
    :param max_fields_capacity:
    :param min_fields_capacity:
    :param number_of_years:
    :return:
    """

    fields_num = len(max_fields_capacity)
    solution = np.zeros((fields_num, number_of_years))

    for y in range(number_of_years):
        flaga = True
        while flaga:
            for fnr in range(fields_num):
                gen = random.randint(min_fields_capacity[fnr], max_fields_capacity[fnr])
                solution[fnr][y] = gen

            if np.sum(solution[:, y]) <= max_magazine_capacity:
                flaga = False

    return solution


# Test
m = 600
l = [800, 600, 800]    # Ograniczenia górne
h = [100, 100, 100]     # Ograniczenia dolne
yrs = 12

A = generate_solution(m, l, h, yrs)
print(A)


def ocena(sol: np.ndarray, planting_cost: np.ndarray, soil_quality: np.ndarray, Isfertilized,fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle,
          transport_cost, bottle_price, grape_types):
    """
    :param sol:
    :param planting_cost:
    :param soil_quality:
    :param Isfertilized:
    :param fertilizer_bonus:
    :param fertilizer_cost:
    :param harvest_cost:
    :param bottling_cost:
    :param plants_per_bottle:
    :param transport_cost:
    :param selling_gain:
    :param grape_types:
    :return:
    """

    # Sam przelicznik funkcji celu
    years = sol.shape[1]
    fields = sol.shape[0]
    solution = 0

    for y in range(years):
        for f in range(fields):
            for t in range(grape_types):
                # Rośliny
                plants_nr = sol[f][y]*(soil_quality[f][t] + Isfertilized * fertilizer_bonus)
                plants_cost = planting_cost + fertilizer_cost + harvest_cost  ## planting_cost - forma

                # Butelki
                bottles = plants_nr//plants_per_bottle
                bottle_cost = bottles * bottling_cost + bottles * transport_cost

                cost = plants_cost + bottle_cost
                gain = bottles * bottle_price

                solution = gain - cost
    return solution


print(ocena(A, 100.00, np.array([[0.90]*A.shape[1],[0.6]*A.shape[1],[0.8]*A.shape[1]]), 1, 0.5, 10, 5, 5, 1, 5, 40, 4))