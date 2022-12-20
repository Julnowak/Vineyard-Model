import copy

import numpy as np
from Command_files import *
from Generators import *
from Wykresy import *
from copy import deepcopy

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

m = 600
l = [800, 800, 800]  # Ograniczenia górne
h = [100, 100, 100]  # Ograniczenia dolne

sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
#print(sol)

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

gain, loss = ocena(sol, plant_cost, gather_number,
                   1, soil_quality_generator(3, ch_types,sol),
                   0.05, 2, 3, 4, 1, 3,
                   vineprice, capacity, month_grow, 2,
                   [200, 100, 100], True, False)


# Prezentacja wyników
sol_present_yourself(gain, loss, sol,ch_types)

epsilon = 0.01
max_iter = 100
yuk = soil_quality_generator(3, ch_types)

def tabu_search(beg_sol, tabu_length=10):
    # zmien
    gain, loss = ocena(beg_sol, plant_cost, gather_number,
                       1, yuk,
                       0.05, 2, 3, 4, 1, 3,
                       vineprice, capacity, month_grow, 2,
                       [100, 100, 100], True, False)
    #sol_present_yourself(gain,loss,beg_sol,ch_types)
    TL = []
    avgMemory=np.zeros((2*sol.shape[0]*sol.shape[1]*sol.shape[2]))#pamiec srednioteminowa zlicza rozwiazania dane

    solution = beg_sol
    past_sol = sum(gain) - sum(loss)

    # Najlepsze
    bs_solution = solution.copy()
    bs = sum(gain) - sum(loss)

    gain_rem = 0
    loss_rem = 0

    stop_iter = False
    stop_eps = False
    counter = 0

    limsta = []

    while not (stop_iter or stop_eps):

        mapa = generateAllsolutions(solution)
        neigh = [k for k, _ in mapa.items()]

        n_rem = None
        maxi = -np.inf

        for n in neigh:

            gain, loss = ocena(mapa[n], plant_cost, gather_number,
                       1,yuk ,
                       0.05, 2, 3, 4, 1, 3,
                       vineprice, capacity, month_grow, 2,
                       [100,100,100], True, False)

            # + funkcja aspiracji
            value=sum(gain) - sum(loss)
            if n not in TL and value > maxi:
                maxi = sum(gain) - sum(loss)
                gain_rem = gain
                loss_rem = loss
                n_rem = n
        #print(n_rem)


        limsta.append(maxi)


        if maxi >= bs:
            solution = mapa[n_rem].copy()
        else:
            if len(TL) < tabu_length:
                TL.append(generateAntiNum(n_rem))
            else:
                TL.pop(0)
                TL.append(generateAntiNum(n_rem))
            solution = mapa[n_rem].copy()

        if counter > max_iter:
            stop_iter = True

        if abs(past_sol - maxi) <= epsilon:
            stop_eps = True

        past_sol = maxi

        counter += 1
        print(counter)

    print(limsta)

    plt.plot(limsta)
    plt.title('Wykres wartości funkcji celu')
    plt.show()

    sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

    return bs_solution


tabu_search(sol)


