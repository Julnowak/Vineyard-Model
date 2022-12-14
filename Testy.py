from Generators import *
from Command_files import *
from Wykresy import *

# Testy generatorów

m = 1000
l = [2000, 1000, 2000]  # Ograniczenia górne
h = [300, 100, 100]  # Ograniczenia dolne
yrs = 1

A = generate_solution(m, l, h, yrs, 4)
#print(A)


plt.close('all')
# Testy głównych funkcji

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

plant_cost = np.asarray([2.2, 4.5, 8])
gather_number = np.ones(shape=(12)) * 6
vineprice = vine_price_generator(ch_types, num_of_years)
planting_cost = plant_price_generator(ch_types)

month_grow = np.random.uniform(low=0.34, high=0.34, size=(12))
grow = np.ones(shape=(12)) * 0.5
capacity = [800, 800, 800]

# Dla zerowej
ik = sol.shape
#print(ik)
sol = np.zeros(ik)

gain, loss = ocena(sol, plant_cost, gather_number,
                   1, soil_quality_generator(3, ch_types,sol),
                   0.05, 2, 3, 4, 1, 3,
                   vineprice, capacity, month_grow, 2,
                   [200, 100, 100], True, False)

#sol_present_yourself(gain, loss, sol,ch_types)


# Dla sadzenia w zimie
ik = sol.shape
sol = np.zeros(ik)
sol[1,1,1] = 1
gain, loss = ocena(sol, plant_cost, gather_number,
                   1, soil_quality_generator(3, ch_types,sol),
                   0.05, 2, 3, 4, 1, 3,
                   vineprice, capacity, month_grow, 2,
                   [200, 100, 100], True, False)

#sol_present_yourself(gain, loss, sol,ch_types)

# Dla sadzenia w dobrej porze
ik = sol.shape
sol = np.zeros(ik)
sol[2,1,2] = 200
gain, loss = ocena(sol, plant_cost, gather_number,
                   1, soil_quality_generator(3, ch_types,sol),
                   0.05, 2, 3, 4, 1, 3,
                   vineprice, capacity, month_grow, 2,
                   [200, 100, 100], True, False)

#sol_present_yourself(gain, loss, sol,ch_types)

# Testy wykresów


