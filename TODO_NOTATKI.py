# TYLKO NOTATKI, BRAK UŻYTEGO KODU

# TODO - Dodać miarę dopuszczalności - funkcja kary konieczna!

# TODO - trójpolówka - jest

# TODO - magazynowanie - (w teorii uwzględnione)

# TODO - zapotrzebowanie sklepu - (większośc)

# TODO lista długoterminowa - częstotliwość wystąpień zmian
# TODO - ogarnąć tabu list

# TODO - funkcja !!!

# TODO ograniczenia

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



# month_grow = np.random.uniform(low=0.34, high=0.34, size=(12))
# grow = np.ones(shape=(12)) * 0.5
# capacity = [800, 800, 800]

# coeff1 = [1, 1, 0.5]
# coeff2 = [2, 1, 0.5]
# for i in range(types_of_grapes):
#     for j in range(soil_types):
#         gathernum[i, :, j] = [0, 0, 0, 1, 3, 7, 16, 17, 12, 2, 0, 0]
#         gathernum[i, :, j] = gathernum[i, :, j] * coeff1[i] * coeff2[j]

# bottle_prices = vine_price_generator({1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}, num_of_years)

# gain, loss = ocena(sol, plant_cost, gathernum, 1, [0, 1, 2], 1.2, 1, 0.5, 2, 3, 1,
#              bottle_prices, types_of_grapes, [300,400,300], (gathernum+3)*3)
