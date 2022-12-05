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
                gen = random.randint(0, max_fields_capacity[fnr])
                solution[fnr][y] = gen

            if np.sum(solution[:, y]) <= max_magazine_capacity:
                flaga = False

    return solution


m = 600
l = [800, 600]
h = [0, 0]
yrs = 12

print(generate_solution(m,l,h, yrs))