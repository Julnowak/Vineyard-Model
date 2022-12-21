from Command_files import *
from Generators import *
from Wykresy import *

np.set_printoptions(precision=4)
#
# # Types of vine, user choice
# # TODO - wybór przez użytkownika, interfejs??? tkinker?
# all_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo', 4: 'Arneis',
#              5: 'Dolcetto', 6: 'Cortese', 7: 'Grignolino', 8: 'Erbaluce'}
#
# ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
#
# # example data and visualisation
# num_of_years = 2
# types_of_grapes = len(ch_types)
# num_of_fields = 3
#
# m = 600
# l = [800, 800, 800]  # Ograniczenia górne
# h = [100, 100, 100]  # Ograniczenia dolne
#
# sol = generate_solution(m, l, h, num_of_years, types_of_grapes)
#
#
# planting_cost = plant_price_generator(ch_types)
#
# # są globalne
# # epsilon = 0.01
# # max_iter = 50
# IsFertilized = 1
# soil_quality = soil_quality_generator(3, num_of_years, ch_types)
# fertilizer_bonus = 0.05
# fertilizer_cost = 2
# harvest_cost = 3
# bottling_cost = 4
# plants_per_bottle = 1
# transport_cost = 3
# vineprice = vine_price_generator(ch_types, num_of_years)
# magazine_cost = 2
# magazine_capacity = 600
# store_needs = [100, 100, 100]

def tabu_search(beg_sol, planting_cost,
                IsFertilized, soil_quality,
                fertilizer_bonus, fertilizer_cost,
                harvest_cost, bottling_cost,
                plants_per_bottle, transport_cost,
                vineprice, magazine_cost, magazine_capacity,store_needs,ch_types,
                tabu_length=10, max_iter=50,epsilon=0.1):

    gain, loss = ocena(beg_sol, planting_cost,
                       IsFertilized, soil_quality,
                       fertilizer_bonus, fertilizer_cost,
                       harvest_cost, bottling_cost,
                       plants_per_bottle, transport_cost,
                       vineprice, magazine_cost, magazine_capacity,store_needs)

    sol_present_yourself(gain, loss, beg_sol, ch_types)

    TL = []
    avgMemory=np.zeros((2*sol.shape[0]*sol.shape[1]*sol.shape[2]))#pamiec srednioteminowa zlicza rozwiazania dane
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

        mapa = generateAllsolutions(solution)
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
            if len(TL) < tabu_length:
                TL.append(generateAntiNum(n_rem))
            else:
                TL.pop(0)
                TL.append(generateAntiNum(n_rem))
            solution = mapa[n_rem].copy()


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

    sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

    return bs_solution


#tabu_search(sol)


