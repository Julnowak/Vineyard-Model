import numpy as np
from Generators import *

# Types of vine, user choice
all_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo', 4: 'Arneis',
         5: 'Dolcetto', 6: 'Cortese', 7: 'Grignolino', 8: 'Erbaluce'}

# ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}

# example data and visualisation
num_of_years = 1
types_of_grapes = 3
num_of_fields = 3
soil_types = 3

sol = np.zeros((num_of_years * 12, num_of_fields, types_of_grapes),dtype=int)
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
#print((sol))

m = 600
l = [800, 800, 800]  # Ograniczenia górne
h = [100, 100, 100]  # Ograniczenia dolne


sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
print(sol)

plant_cost = np.asarray([2.2, 4.5, 8])

gathernum = np.ones((types_of_grapes, 12, soil_types))
coeff1 = [1, 1, 0.5]
coeff2 = [2, 1, 0.5]
for i in range(types_of_grapes):
    for j in range(soil_types):
        gathernum[i, :, j] = [0, 0, 0, 1, 3, 7, 16, 17, 12, 2, 0, 0]
        gathernum[i, :, j] = gathernum[i, :, j] * coeff1[i] * coeff2[j]

bottle_prices = vine_price_generator({1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'},1)

gain, loss = ocena(sol, plant_cost, gathernum, 1, [0, 1, 2], 1.2, 1, 0.5, 2, 3, 1,
             bottle_prices, types_of_grapes, 800, (gathernum+3)*3)
# print(k)
print(" ")
# print(v)
print(sum(gain)-sum(loss))

plt.plot(gain)
plt.plot(loss)
plt.title("wykres zysku i strat")
plt.legend(["zysk", "strata"])
plt.show()


# import datavisualisation
