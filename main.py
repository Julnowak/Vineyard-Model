import numpy as np
from Command_files import *
from Generators import *

np.set_printoptions(precision=4)

# Types of vine, user choice
# TODO - wybór przez użytkownika, interfejs??? tkinker?
all_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo', 4: 'Arneis',
             5: 'Dolcetto', 6: 'Cortese', 7: 'Grignolino', 8: 'Erbaluce'}

ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}

# example data and visualisation
num_of_years = 1
types_of_grapes = 3
num_of_fields = 3
soil_types = 3

sol = np.zeros((num_of_years * 12, num_of_fields, types_of_grapes), dtype=int)
sol[5, 0, 0] = 100
sol[5, 1, 1] = 100
sol[5, 2, 1] = 100
sol[6, 0, 0] = 100
sol[6, 1, 1] = 100
sol[6, 2, 1] = 100
sol[7, 0, 0] = 50
sol[7, 1, 1] = 50
sol[7, 2, 1] = 50
sol[8, 0, 0] = 49
sol[8, 1, 1] = 49
sol[8, 2, 1] = 49
# print((sol))

m = 600
l = [800, 800, 800]  # Ograniczenia górne
h = [100, 100, 100]  # Ograniczenia dolne

sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
print(sol)

plant_cost = np.asarray([2.2, 4.5, 8])
gather_number = np.ones(shape=(12)) * 6
vineprice = vine_price_generator(ch_types, num_of_years)
planting_cost = plant_price_generator(ch_types)

month_grow = np.random.uniform(low=0.34, high=0.34, size=(12))
grow = np.ones(shape=(12)) * 0.5
capacity = [800, 800, 800]

# coeff1 = [1, 1, 0.5]
# coeff2 = [2, 1, 0.5]
# for i in range(types_of_grapes):
#     for j in range(soil_types):
#         gathernum[i, :, j] = [0, 0, 0, 1, 3, 7, 16, 17, 12, 2, 0, 0]
#         gathernum[i, :, j] = gathernum[i, :, j] * coeff1[i] * coeff2[j]

# bottle_prices = vine_price_generator({1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}, num_of_years)

# gain, loss = ocena(sol, plant_cost, gathernum, 1, [0, 1, 2], 1.2, 1, 0.5, 2, 3, 1,
#              bottle_prices, types_of_grapes, [300,400,300], (gathernum+3)*3)

gain, loss = ocena(sol, plant_cost, gather_number, 1, soil_quality_generator(3, ch_types), 0.05, 2, 3, 4, 1, 3,
                   vineprice, capacity, month_grow, 10, True, False)

# WYKRESY
# print(k)
print(" ")
# print(v)

# Łącznie - wartość funkcji celu
print(sum(gain) - sum(loss))
print(gain)
# Wykresy ogólne
plt.plot(gain)
plt.plot(loss)
plt.title("Wykres zysku i strat")
plt.grid()
plt.legend(["zysk", "strata"])
plt.show()

# TODO
## Zmnienić na Bar ploty

# Bar ploty
plt.bar(1, sum(gain))
plt.bar(2, sum(loss))
plt.title("Porównanie zysków i strat")
plt.grid(axis='y')
plt.xticks([1, 2],['Zyski','Straty'])
plt.xlabel('Ilość pieniędzy w zł')
plt.show()

w = []
for i in range(len(gain)):
    w.append(gain[i] - loss[i])

plt.plot(w)
plt.title("Wykres sumarycznego zysku")
plt.ylabel('Wartość przychodu miesięcznego')
plt.xlabel('Nr miesiąca')
plt.grid()
plt.show()
# import datavisualisation
