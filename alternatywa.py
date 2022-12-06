import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Union, List, Dict
import random


# Generator rozwiązania początkowego dla lat
def generate_solution(max_magazine_capacity: int, max_fields_capacity: Union[List, Dict],
                      min_fields_capacity: Union[List, Dict], number_of_years: int) -> np.ndarray:

    fields_num = len(max_fields_capacity)
    solution = np.zeros((fields_num, number_of_years))
    print(solution)
    for y in range(solution.shape[1]):
        flaga = True
        while flaga:
            for fnr in range(fields_num):
                gen = random.randint(min_fields_capacity[fnr], max_fields_capacity[fnr])
                solution[fnr][y] = gen

            if np.sum(solution[:, y]) <= max_magazine_capacity:
                flaga = False

    return solution


# Test generatora
m = 600
l = [800, 600, 800]  # Ograniczenia górne
h = [100, 100, 100]  # Ograniczenia dolne
yrs = 1

A = generate_solution(m, l, h, yrs)
print(A)


field_nr = 3







# Losowana jakość gleby
np.set_printoptions(precision=2)
soil_quality = np.random.uniform(low=0.7, high=0.95, size=(field_nr, len(ch_types)))
print(soil_quality)

