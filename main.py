from Command_files import *
from Generators import *
from Wykresy import *

import sys
f = open("test.out", 'w')
sys.stdout = f

np.set_printoptions(precision=4)
testowe = np.array([[[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 300, 0],
                     [307, 0, 0],
                     [0, 258, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 300],
                     [0, 0, 372],
                     [275, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[301, 0, 0],
                     [0, 0, 205],
                     [0, 0, 351]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]])

epsilon = 0.01
max_iter = 20
num_of_years = 1
magazine_capacity = 600
magazine_cost = 2
plants_per_bottle = 1
transport_cost = 2
bottling_cost = 2
harvest_cost = 2
ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}
IsFertilized = 1
fertilizer_bonus = 0.05
fertilizer_cost = 2
store_needs = [100, 100, 100]

planting_cost = np.array([14.13, 13.53, 17.66])

soil_quality = np.array([[[0.28, 0.25, 0.26],
                          [0.22, 0.23, 0.25],
                          [0.22, 0.25, 0.27]],

                         [[0.28, 0.25, 0.26],
                          [0.22, 0.23, 0.25],
                          [0.22, 0.25, 0.27]],

                         [[0.93, 0.83, 0.87],
                          [0.73, 0.76, 0.82],
                          [0.73, 0.83, 0.89]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.93, 0.83, 0.87],
                          [0.73, 0.76, 0.82],
                          [0.73, 0.83, 0.89]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.65, 0.58, 0.61],
                          [0.51, 0.53, 0.57],
                          [0.51, 0.58, 0.63]],

                         [[0.93, 0.83, 0.87],
                          [0.73, 0.76, 0.82],
                          [0.73, 0.83, 0.89]],

                         [[0.28, 0.25, 0.26],
                          [0.22, 0.23, 0.25],
                          [0.22, 0.25, 0.27]]])

vineprice = [[41.03, 39.55, 36.31, 37.88, 40.64, 38.16, 43., 42.15, 37.73, 42.77, 34.36, 37.65],
             [36.83, 43.16, 39.84, 41.39, 31.93, 36.5, 37.8, 39.06, 36.28, 42.55, 42.96, 30.38],
             [55.46, 53.59, 53.75, 53.68, 53.72, 54.84, 53.17, 55.56, 55.59, 53.18, 53.63, 53.04]]



def tabu_search(beg_sol, planting_cost,
                IsFertilized, soil_quality,
                fertilizer_bonus, fertilizer_cost,
                harvest_cost, bottling_cost,
                plants_per_bottle, transport_cost,
                vineprice, magazine_cost, magazine_capacity,store_needs, ch_types,
                tabu_length=100, max_iter=500, epsilon=0.1):

    gain, loss = ocena(beg_sol, planting_cost,
                       IsFertilized, soil_quality,
                       fertilizer_bonus, fertilizer_cost,
                       harvest_cost, bottling_cost,
                       plants_per_bottle, transport_cost,
                       vineprice, magazine_cost, magazine_capacity,store_needs)

    # sol_present_yourself(gain, loss, beg_sol, ch_types)

    TL = []
    avgMemory=np.zeros((2*beg_sol.shape[0]*beg_sol.shape[1]*beg_sol.shape[2])) #pamiec srednioteminowa zlicza rozwiazania dane
    streak=0
    streaknum=-1


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

        mapa = gen(solution)
        # print(mapa)
        # print('\n-----------------------------------\n')
        neigh = [k for k, _ in mapa.items()]

        n_rem = None
        value = None
        maxi = -np.inf
        maxval = -np.inf

        for n in neigh:

            gain, loss = ocena(mapa[n], planting_cost,
                               IsFertilized, soil_quality,
                               fertilizer_bonus, fertilizer_cost,
                               harvest_cost, bottling_cost,
                               plants_per_bottle, transport_cost,
                               vineprice, magazine_cost, magazine_capacity, store_needs)

            # + funkcja aspiracji
            value=sum(gain) - sum(loss)
            if n not in TL and value-avgMemory[n]*2  > maxi:
                maxi = sum(gain) - sum(loss)-avgMemory[n]*2#no jak było wybierane to mniej
                maxval=sum(gain) - sum(loss)
                gain_rem = gain
                loss_rem = loss
                n_rem = n
        #print(n_rem)


        limsta.append(maxval)

        avgMemory[n_rem]=avgMemory[n_rem]+1
        if n_rem==streaknum:
            streak=streak+1
        else:
            streaknum=n_rem
            streak=1
        if streak>99999:
            # wybralismy 9999 to smao rozw zróbmy coś dzikiego
            pass
        limsta.append(value)


        if maxval >= bs:
            solution = mapa[n_rem].copy()
        else:
            solution = mapa[n_rem].copy()

        print("pawel:",len(TL) , tabu_length)

        if len(TL) < tabu_length:
            TL.append(generateAntiNum(n_rem))
        else:
            TL.pop(0)
            TL.append(generateAntiNum(n_rem))

        if counter > max_iter:
            stop_iter = True

        if abs(past_sol - maxval) <= epsilon:
            stop_eps = True

        past_sol = maxval

        counter += 1
        print(counter)
        if counter >= max_iter:
            stop_iter = True

    print(limsta)

    plt.plot(limsta)
    plt.title('Wykres wartości funkcji celu')
    plt.show()

    # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

    return bs_solution

tabu_search(testowe, planting_cost,
                   IsFertilized, soil_quality,
                   fertilizer_bonus, fertilizer_cost,
                   harvest_cost, bottling_cost,
                   plants_per_bottle, transport_cost,
                   vineprice, magazine_cost, magazine_capacity, store_needs,ch_types)

f.close()