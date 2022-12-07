import numpy as np
from typing import Union, List, Dict


def ocena(sol: np.ndarray, planting_costs: np.ndarray, gather_number: np.ndarray, Isfertilized, soil_type,
          fertilizer_bonus,
          fertilizer_cost, harvest_cost, bottling_cost, plants_per_bottle, transport_cost,
          bottle_price, mfields_capacity: List, month_grow: np.ndarray, magazine_cost, pruning: bool = True,
          usuwanie: bool = False):
    """

    :param sol:number_of_years * 12 x fields_num x types
    :param planting_costs: grape_types
    :param gather_number:  12
    :param Isfertilized:
    :param soil_type: fieldsNum - Nie soil_type tylko mnoznik jakościowy typu np. 0.7 przemnażany przez oczekiwaną ilośc plonów
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

    winter = []
    planting_breaks = []

    # Winter months
    # for i in range(sol.shape[0]//12):
    # winter += [0+12*i, 1+12*i, 11+12*i]
    # planting_breaks += [3+12*i, 4+12*i, 5+12*i, 7+12*i, 8+12*i, 9+12*i]

    # Sam przelicznik funkcji celu
    months = sol.shape[0]
    fields = sol.shape[1]
    grape_types = sol.shape[2]

    # TODO
    max_fields_capacity = max(mfields_capacity)  # Do naprawy
    field_grow = np.zeros(shape=(fields, max_fields_capacity))
    grape_type = np.ones(shape=(fields, max_fields_capacity), dtype=int) * -1
    cost = []
    gains = []
    for y in range(months):
        month_cost = 0
        month = y % 12
        gatherings = np.zeros((grape_types))
        for f in range(fields):
            for t in range(grape_types):
                beg = (np.where(grape_type[f] == -1))
                if not beg == []:
                    beg = [0][0]
                if not beg == []:
                    beg = [0][0]
                end = beg + sol[y][f][t]
                if end > mfields_capacity[f]:
                    end = mfields_capacity[f]
                if month not in [0, 1, 11]:
                    grape_type[f, beg:end] = t

                month_cost = month_cost + planting_costs[t] * sol[y][f][t] + fertilizer_cost
            for p in range(max_fields_capacity):
                if pruning and month == 10:
                    field_grow[f][p] = 0.7 * field_grow[f][p]
                if grape_type[f][p] != -1:
                    if field_grow[f][p] < 1:
                        # growth of wines
                        field_grow[f][p] = field_grow[f][p] + month_grow[month] * \
                                           (soil_type[f][grape_type[f][p]] + Isfertilized * fertilizer_bonus)

                        if field_grow[f][p] > 1:
                            field_grow[f][p] = 1
                        month_cost = month_cost + fertilizer_cost
                    else:
                        # gathering
                        gatherings[grape_type[f][p]] = gatherings[grape_type[f][p]] + \
                                                       gather_number[month] * (soil_type[f][grape_type[f][
                            p]] * Isfertilized * fertilizer_bonus)

                        month_cost = month_cost + fertilizer_cost
                        if usuwanie:
                            field_grow[f][p] = 0
                            grape_type[f][p] = -1

        # butelkowanie i sprzedaz
        harvest_costs = harvest_cost * sum(gatherings)
        bottles = gatherings / plants_per_bottle
        cost_of_postprocessing = np.sum(bottles) * (bottling_cost + magazine_cost + transport_cost)
        month_cost = month_cost + cost_of_postprocessing + harvest_costs
        cost.append(month_cost)
        gain = bottles.dot(bottle_price[:, y])
        gains.append(gain)

    return gains, cost


def IsOK(field, mini: int, maxi: int):
    ans = False
    if mini <= field <= maxi:
        ans = True
    return ans
