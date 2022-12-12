import numpy as np
from typing import Union, List, Dict


def ocena(sol: np.ndarray, planting_costs: np.ndarray, gather_number: np.ndarray, Isfertilized, soil_quality,
          fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle, transport_cost,
          bottle_price, mfields_capacity: List, month_grow: np.ndarray, magazine_cost, pruning: bool = True,
          usuwanie: bool = False):


    """
    :param sol:number_of_years * 12 x fields_num x types
    :param planting_costs: grape_types
    :param gather_number: 12
    :param Isfertilized:
    :param soil_quality: fieldsNum - Nie soil_type tylko mnoznik jakościowy typu np. 0.7 przemnażany przez oczekiwaną ilośc plonów
    :param fertilizer_bonus:
    :param fertilizer_cost:
    :param harvest_cost:
    :param bottling_cost:
    :param plants_per_bottle:
    :param transport_cost:
    :param bottle_price: grape_types x 12
    :param grape_types:
    :param max_fields_capacity:
    :param month_grow: grape_types x 12
    :return:
    """

    # Sam przelicznik funkcji celu
    months = sol.shape[0]
    fields = sol.shape[1]
    grape_types = sol.shape[2]

    gains = []
    cost = []

    for m in range(months):
        month_cost = 0
        month_gain = 0
        month = m % 12
        if month not in [0, 1, 11]:
            for f in range(fields):
                 for t in range(grape_types):
                     # Koszt obsiania danego pola danym typem winogron
                    plant_cost = sol[m][f][t] * planting_costs[t] + Isfertilized * fertilizer_cost

                    # Ilość zbioru z pola
                    gathering = sol[m][f][t] * (soil_quality[f][t] + Isfertilized * fertilizer_bonus)

                    # Koszt zbiorów
                    ha_cost = sol[m][f][t] * harvest_cost

                    # TODO - wykombinować co zrobić z resztą

                    # Ilość butelek, które powstały
                    bottles = int(gathering // plants_per_bottle)

                    # butelkowanie i transport
                    bottrans_cost = bottles * bottling_cost + transport_cost * bottles
                    bottle_gain = bottles * bottle_price[t][m]

                    # Koszty i zyski dla danego pola i danego typu

                    month_cost += plant_cost + ha_cost + bottrans_cost + bottles * magazine_cost
                    month_gain += bottle_gain

        # Plus opłata utrzymania winnicy?
        cost.append(month_cost + 1200.00)
        gains.append(month_gain)

    return gains, cost


    # # TODO
    # max_fields_capacity = max(mfields_capacity)  # Do naprawy
    # field_grow = np.zeros(shape=(fields, max_fields_capacity)) # Tylko do rośnięcia
    # grape_type = np.ones(shape=(fields, max_fields_capacity), dtype=int) * -1
    # cost = []
    # gains = []
    # for y in range(months):
    #     month_cost = 0
    #     month = y % 12
    #     gatherings = np.zeros((grape_types))
    #     for f in range(fields):
    #         for t in range(grape_types):
    #             beg = (np.where(grape_type[f] == -1))
    #             if not beg == []:
    #                 beg = [0][0]
    #             if not beg == []:
    #                 beg = [0][0]
    #             end = beg + sol[y][f][t]
    #             if end > mfields_capacity[f]:
    #                 end = mfields_capacity[f]
    #             if month not in [0, 1, 11]:
    #                 grape_type[f, beg:end] = t
    #
    #             month_cost = month_cost + planting_costs[t] * sol[y][f][t] + fertilizer_cost
    #         for p in range(max_fields_capacity):
    #             if pruning and month == 10:
    #                 field_grow[f][p] = 0.7 * field_grow[f][p]
    #             if grape_type[f][p] != -1:
    #                 if field_grow[f][p] < 1:
    #                     # growth of wines
    #                     field_grow[f][p] = field_grow[f][p] + month_grow[month] * \
    #                                        (soil_type[f][grape_type[f][p]] + Isfertilized * fertilizer_bonus)
    #
    #                     if field_grow[f][p] > 1:
    #                         field_grow[f][p] = 1
    #                     month_cost = month_cost + fertilizer_cost
    #                 else:
    #                     # gathering
    #                     gatherings[grape_type[f][p]] = gatherings[grape_type[f][p]] + \
    #                                                    gather_number[month] * (soil_type[f][grape_type[f][
    #                         p]] * Isfertilized * fertilizer_bonus)
    #
    #                     month_cost = month_cost + fertilizer_cost
    #                     if usuwanie:
    #                         field_grow[f][p] = 0
    #                         grape_type[f][p] = -1
    #
    #     # butelkowanie i sprzedaz
    #     harvest_costs = harvest_cost * sum(gatherings)
    #     bottles = gatherings / plants_per_bottle
    #     cost_of_postprocessing = np.sum(bottles) * (bottling_cost + magazine_cost + transport_cost)
    #     month_cost = month_cost + cost_of_postprocessing + harvest_costs
    #     cost.append(month_cost)
    #     gain = bottles.dot(bottle_price[:, y])
    #     gains.append(gain)
    #
    # return gains, cost

# TODO - ograniczniki, kara za obniżenie
def IsOK(field: int, mini: int, maxi: int):
    """
    :param field: number of the field
    :param mini: minimal value of field capacity; can be lower in some cases
    :param maxi: maximal value of field capacity; can't be be increased
    :return:
    """
    ans = False
    if mini <= field <= maxi:
        ans = True
    return ans
