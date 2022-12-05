import random
import numpy as np
from typing import Union, List, Dict


def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict], min_fields_capacity: Union[List, Dict], number_of_years: int):
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


def ocena(sol: np.ndarray, planting_cost: float, soil_quality, Isfertilized,fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle,
          transport_cost, selling_gain,):
    # Sam przelicznik funkcji celu
    years = sol.shape[1]
    fields = sol.shape[0]
    solution = 0

    for y in range(years):
        for f in range(fields):
            # Rośliny
            plants_nr = sol[f][y]*(soil_quality + Isfertilized * fertilizer_bonus)
            plants_cost = planting_cost + fertilizer_cost + harvest_cost

            # Butelki
            bottles = plants_nr//plants_per_bottle
            bottle_cost = bottles * bottling_cost + bottles * transport_cost

            cost = plants_cost + bottle_cost
            gain = bottles * selling_gain

            solution = gain - cost
    return solution


print(ocena(A, 100.00, 0.90, 1, 0.5, 10, 5, 5, 5, 5, 40))