from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic
from Generators import *
import sys

# Types of vine, user choice
# TODO - wybór przez użytkownika, interfejs??? tkinker?
all_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo', 4: 'Arneis',
             5: 'Dolcetto', 6: 'Cortese', 7: 'Grignolino', 8: 'Erbaluce'}

ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}

# example data and visualisation
num_of_years = 2
types_of_grapes = 3
num_of_fields = 3
soil_types = 3

m = 600
l = [800, 800, 800]  # Ograniczenia górne
h = [100, 100, 100]  # Ograniczenia dolne

sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
planting_cost = plant_price_generator(ch_types)
IsFertilized = 1
soil_quality = soil_quality_generator(3, num_of_years, ch_types)
fertilizer_bonus = 0.05
fertilizer_cost = 2
harvest_cost = 3
bottling_cost = 4
plants_per_bottle = 1
transport_cost = 3
vineprice = vine_price_generator(ch_types, num_of_years)
magazine_cost = 2
magazine_capacity = 600
store_needs = [100, 100, 100]

epsilon = 0.01
max_iter = 50