from Generators import *
from Command_files import *
from Wykresy import *

### Testy generatorów

# Test Generacji rozwiązania i jego dopuszczalności --- działa
m = 1000
l = [301, 1000, 2000]  # Ograniczenia górne
h = [300, 100, 100]  # Ograniczenia dolne
yrs = 1

A = generate_solution(m, l, h, yrs, 3)
# print(A)
# print(isOK_size(A, h, l, m))

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

np.set_printoptions(precision=2)
gain, loss = ocena(testowe, planting_cost,
                   IsFertilized, soil_quality,
                   fertilizer_bonus, fertilizer_cost,
                   harvest_cost, bottling_cost,
                   plants_per_bottle, transport_cost,
                   vineprice, magazine_cost, magazine_capacity, store_needs)

#
# print(gain, '\n', loss)
# # Testy głównych funkcji
#
#
# # Testy wykresów
# colors = ['darkorchid', 'slateblue', 'darkgoldenrod',
#           'orangered', 'crimson', 'teal', 'steelblue', 'firebrick']
# ch_types = {1: 'Barbera', 2: 'Chardonnay'}
# num_of_years = 2
# bottle_prices = vine_price_generator(ch_types,num_of_years)



# c = 0
# if len(ch_types) > 4:
#     k = 2
# else:
#     k = 1
# months = num_of_years * 12
#
# fig = plt.figure()
# for _, v in ch_types.items():
#     if k > 2:
#         ax = fig.add_subplot(len(ch_types)- len(ch_types)//2, k, c + 1)
#     else:
#         ax = fig.add_subplot(len(ch_types), k, c + 1)
#
#     if num_of_years <= 2:
#         ax.plot(range(1, months + 1), bottle_prices[c], linestyle='--', marker='o', c=colors[c])
#     else:
#         ax.plot(range(1, months + 1), bottle_prices[c], c=colors[c])
#     ax.grid()
#     ax.legend((v,), loc='best')
#
#     c += 1
#
# fig.suptitle(f"Zmiana ceny wina na przestrzeni {months} miesięcy", y=0.97)
# fig.supylabel('Aktualna cena wina')
#
# if months == 12:
#     month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#     plt.xticks(range(1, months + 1), month)
#     fig.supxlabel('Miesiąc')
# else:
#     fig.supxlabel('Nr.miesiąca')
# fig.tight_layout()

plt.show()
import pandas as pd
fields = 5

soil_quality = soil_quality_generator(fields, num_of_years, ch_types)
writer = pd.ExcelWriter('Wyniki/Tabele/jakosc_gleby.xlsx', engine='xlsxwriter')
for i in range(num_of_years * 12):
    df2 = pd.DataFrame(data=soil_quality[i, :, :].astype(float))
    df2.insert(loc=0, column='Pole', value=list(range(fields)))
    df2.to_excel('Wyniki/Tabele/jakosc_gleby.xlsx', sheet_name=f'Miesiac {i + 1}',
                 header=['Pole']+list(ch_types.values()), index=False)
writer.close()