import numpy as np
import matplotlib.pyplot as plt
from start_solution_generator import *

# example data and visualisation
num_of_years = 5
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
plant_cost = np.asarray([2.2, 4.5, 8])

gathernum = np.ones((types_of_grapes, 12, soil_types))
coeff1 = [1, 1, 0.5]
coeff2 = [2, 1, 0.5]
for i in range(types_of_grapes):
    for j in range(soil_types):
        gathernum[i, :, j] = [0, 0, 0, 1, 3, 7, 16, 17, 12, 2, 0, 0]
        gathernum[i, :, j] = gathernum[i, :, j] * coeff1[i] * coeff2[j]

bottle_prices = np.ones((types_of_grapes, 12))
bottle_prices[0, :] = [0, 0, 0, 1, 13, 71, 16, 17, 12, 2, 0, 0]
bottle_prices[1, :] = [71, 20, 15, 26, 30, 17, 16, 17, 12, 2, 0, 0]
bottle_prices[2, :] = [0, 0, 0, 1, 3, 7, 56, 47, 32, 50, 60, 0]

gain, loss = ocena(sol, plant_cost, gathernum, 1, [0, 1, 2], 1.2, 1, 0.5, 2, 3, 1,
             bottle_prices, types_of_grapes, 300, (gathernum+3)*3)
# print(k)
print(" ")
# print(v)
print(sum(gain)-sum(loss))

plt.plot(gain)
plt.plot(loss)
plt.title("wykres zysku i strat")
plt.legend(["zysk","strata"])
plt.show()

for i in range(3):
    plt.plot(bottle_prices[i])
plt.title("cena butelek wina")
plt.show()
import datavisualisation
