import numpy as np
from typing import Union, List, Dict

# Funkcja celu - ocena jakości rozwiązania
def ocena(sol: np.ndarray, planting_costs: np.ndarray,
          Isfertilized, soil_quality, fertilizer_bonus, fertilizer_cost,
          harvest_cost, bottling_cost, plants_per_bottle, transport_cost,
          bottle_price, magazine_cost, magazine_capacity, store_needs=None, pruning: bool = True, usuwanie: bool = False):

    """
    :param sol:number_of_years * 12 x fields_num x types
    :param planting_costs: grape_types
    :param Isfertilized:
    :param soil_quality: fieldsNum - Nie soil_type tylko mnoznik jakościowy typu np. 0.7 przemnażany przez oczekiwaną ilośc plonów
    :param fertilizer_bonus:
    :param fertilizer_cost:
    :param harvest_cost:
    :param bottling_cost:
    :param plants_per_bottle:
    :param transport_cost:
    :param bottle_price: grape_types x 12
    :return:
    """

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
                    plant_cost = sol[m][f][t] * planting_costs[t] + Isfertilized * fertilizer_cost
                else:
                    plant_cost = 0

                # Ilość zbioru z pola
                if m % 12 in [0, 1, 11]:
                    gathering = 0
                else:
                    gathering = sol[m][f][t] * (soil_quality[m][f][t] + Isfertilized * fertilizer_bonus)

                # Koszt zbiorów
                if sol[m][f][t] != 0 and m%12 not in [0, 1, 11]:
                    ha_cost = sol[m][f][t] * harvest_cost
                else:
                    ha_cost = 0


                # Ilość butelek, które powstały
                bottles = int(gathering // plants_per_bottle) + remains[t]
                # if gathering / plants_per_bottle - bottles != 0:
                #     left = gathering / plants_per_bottle - bottles
                #     month_cost += left*20

                if store_needs_actual[t] >= bottles:
                    store_needs_actual[t] = store_needs_actual[t] - bottles
                    bottles_selled = bottles
                    bottles_remained = 0

                elif store_needs_actual[t] < bottles:
                    bottles_remained = bottles - store_needs_actual[t]
                    bottles_selled = bottles - bottles_remained
                    store_needs_actual[t] = 0


                # butelkowanie i transport
                bottrans_cost = bottles_selled * bottling_cost + transport_cost * bottles_selled

                bottle_gain = bottles_selled * bottle_price[t][m]

                month_cost += plant_cost + ha_cost + bottrans_cost + bottles_remained * magazine_cost

                month_gain += bottle_gain

                remains[t] = bottles_remained

        if magazine_capacity < sum(remains):
            remains[remains.index(max(remains))]= max(remains) - (sum(remains) - 600)
            month_gain += (sum(remains) - 600) * 0.5 * bottle_price[remains.index(max(remains))][m]

        # Plus opłata utrzymania winnicy
        cost.append(month_cost + np.random.uniform(low=1800.00, high=2800.00))
        gains.append(month_gain)

    return gains, cost
