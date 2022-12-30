import numpy as np

from typing import Union, List, Dict

# Funkcja celu - ocena jakości rozwiązania
def ocena(sol: np.ndarray, planting_costs: np.ndarray,
          Isfertilized, soil_quality, fertilizer_bonus, fertilizer_cost,
          harvest_cost, bottling_cost, plants_per_bottle, transport_cost,
          bottle_price, magazine_cost, magazine_capacity, store_needs=None):

    if store_needs is None:
        store_needs = [np.inf] * sol.shape[2]

    # Sam przelicznik funkcji celu
    months = sol.shape[0]
    fields = sol.shape[1]
    grape_types = sol.shape[2]

    gains = []
    cost = []

    remains = [0] * len(store_needs)
    bottles_selled = 0
    bottles_remained =0
    for m in range(months):
        store_needs_actual = store_needs.copy()
        month_cost = 0
        month_gain = 0

        for f in range(fields):
             for t in range(grape_types):

                 # Koszt obsiania danego pola danym typem winogron
                if sol[m][f][t] != 0 and m%12 not in [0,1,11]:
                    plant_cost = sol[m][f][t] * planting_costs[t] + Isfertilized * fertilizer_cost*sol[m][f][t]
                else:
                    plant_cost = 0
                # print('------',m,' ',f, ' ',t,'------' )
                # print('zasadzono:',sol[m][f][t])
                # print('koszt obsadzenia',plant_cost)

                # Ilość zbioru z pola
                if m % 12 in [0, 1, 11]:
                    gathering = 0
                else:
                    gathering = sol[m][f][t] * (soil_quality[m][f][t] + Isfertilized * fertilizer_bonus)

                # print('zebrano:', gathering)

                # Koszt zbiorów
                if sol[m][f][t] != 0 and m%12 not in [0, 1, 11]:
                    ha_cost = gathering * harvest_cost
                else:
                    ha_cost = 0

                # print('koszt zbioru:', ha_cost)

                # Ilość butelek, które powstały
                bottles = int(gathering // plants_per_bottle) + remains[t]
                bottling_expenses = int(gathering // plants_per_bottle) * bottling_cost

                # print('koszt butelkowania:', bottling_expenses)
                # print('Nowe butelki:', int(gathering // plants_per_bottle))
                # print('Pozostałe butelki:', remains[t])


                if store_needs_actual[t] >= bottles:
                    store_needs_actual[t] = store_needs_actual[t] - bottles
                    bottles_selled = bottles
                    bottles_remained = 0

                elif store_needs_actual[t] < bottles:
                    bottles_remained = bottles - store_needs_actual[t]
                    bottles_selled = bottles - bottles_remained
                    store_needs_actual[t] = 0

                # print('butelki po tej rundzie:', bottles_remained)
                # print('butelki sprzedane:', bottles_selled)

                # butelkowanie i transport
                bottrans_cost = bottling_expenses + transport_cost * bottles_selled

                # print('koszty transportu:', transport_cost * bottles_selled)
                bottle_gain = bottles_selled * bottle_price[t][m]

                # print('zysk ze sprzedaży:', bottle_gain)

                month_cost += plant_cost + ha_cost + bottrans_cost + bottles_remained * magazine_cost
                # print(month_cost)
                # print(bottles_remained * magazine_cost)

                month_gain += bottle_gain

                remains[t] = bottles_remained
                # print(remains)

        if magazine_capacity < sum(remains):
            remains[remains.index(max(remains))] = max(remains) - (sum(remains) - magazine_capacity)
            month_gain += (sum(remains) - magazine_capacity) * 0.5 * bottle_price[remains.index(max(remains))][m]
        # Sprzedajemy po połowie ceny

        # Kara
        for i in store_needs_actual:
            if i != 0:
                month_cost += i * 1.0

        # Plus opłata utrzymania winnicy
        cost.append(round(month_cost + np.random.uniform(low=1600.00, high=2000.00), 2))
        gains.append(round(month_gain,2))

    return gains, cost

# Czy plony mieszczą się w zakresie ograniczeń
def isOK_size(sol, minimum, maximum, mag):
    flaga = True
    for m in range(sol.shape[0]):
        if m%12 not in [0,1,3,4,5,7,8,9,11]:
            for f in range(sol.shape[1]):
                if np.sum(sol[m][f]) > maximum[f] or np.sum(sol[m][f]) < minimum[f]:
                    flaga = False

        # Nie jest to ograniczenie ostatecze magazynu
        if np.sum(sol[m]) > mag:
            flaga = False
    return flaga


