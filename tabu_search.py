
from Command_files import *
import numpy as np
from Wykresy import *
from Generators import *




def tabu_search(beg_sol,            # <- generate solution
                planting_cost,      # <- plant price gen
                IsFertilized,       # const 1 or 0
                soil_quality,       # soil quality gen
                fertilizer_bonus,   # 0.05, 0.10, 0.17 [%]
                fertilizer_cost,    # 2.00, 4.00, 7.00 [$]
                harvest_cost,       # const float [$]
                bottling_cost,      # const float [$]
                plants_per_bottle,  # const int
                transport_cost,     # const float [$]
                vineprice,          # <- vine price gen
                magazine_cost,      # const float [$]
                magazine_capacity,  # const int
                store_needs,        # [100, 100,.., per type]
                ch_types,           # wine types dict
                #       const       #
                tabu_length=10,     #
                max_iter=50,        #
                epsilon=0.1,        #
                upper=[800,800,800],#
                lower=[100,100,100] ):
    #FLAGI#
    #
    #   TYP SĄSIEDZTWA  #
    #
    constval = 0             # stały      #
    rand = 1                 # czy tryb losowy ON?
    minrand = 5              # min losowy #
    maxrand = 40             # max losowy #

                                                #checkbox działa jako 1/0 czy true/false?
    LongTermMem = 1                   # chekcbox czy długoterminowa
    SolutionSpaceCoverage = 0.5       # cześć sąsiedztwa
                                      #
    #MidTermMem =                     # non implemented (are you sure ab that O.o)
                                      #
    tabulist = 1                      # checkbox czy krótkoteminowa?
    midtemmemTreshold = 10            # długość listy tabu

    gain, loss = ocena(beg_sol, planting_cost,IsFertilized, soil_quality,fertilizer_bonus, fertilizer_cost,harvest_cost,
                       bottling_cost,plants_per_bottle, transport_cost,vineprice, magazine_cost, magazine_capacity,
                       store_needs, upper, lower)

    beg = round(sum(gain) - sum(loss), 2)

    #self.stat.setText(str(beg))
    #self.c2.plot_main(gain, loss, 'beginning_main_linear_plot')
    #self.c2.setVisible(True)
    #self.c3.plot_bar(gain, loss, 'beginning_bar_plot')
    #self.c3.setVisible(True)
    #self.c4.plot_bar2(gain, loss, beg_sol.shape[0], 'beginning_detailed_bar_plot')
    #self.c4.setVisible(True)
    #self.t.setVisible(True)

    TL = []     # AVG_Memory -> pamiec srednioteminowa zlicza rozwiazania dane
    avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[2]))

    streak = 0  # Do kryterium aspiracji

    # Aktualne
    solution = beg_sol.copy()
    past_sol = None

    # Najlepsze
    bs_solution = solution.copy()
    bs = sum(gain) - sum(loss)
    bs_gain_rem = gain
    bs_loss_rem = loss
    bs_counter_rem = 0

    # Aktualne REM????
    gain_rem = 0
    loss_rem = 0

    stop_iter = False
    stop_eps = False
    counter = 0
    aspi_counter = 0

    #self.pb.setTextVisible(True)        #progress bar
    #self.pb.setMaximum(max_iter)

    minieps = np.inf
    # DANE
    dane = [[counter, round(sum(gain), 2), round(sum(loss), 2), round(sum(gain) - sum(loss), 2), len(TL),
             wypisz(beg_sol, ch_types)]]

    limsta = []
    while not (stop_iter or stop_eps):
        if counter == 0:
            past_sol = 0

        #self.pb.setValue(counter)
        mapa = generateAllsolutions(solution, upper, SolutionSpaceCoverage, rand, minrand, maxrand, constval)
        neigh = [k for k, _ in mapa.items()]

        n_rem = None
        maxi = -np.inf
        maxval = -np.inf

        for n in neigh:
            gain, loss = ocena(beg_sol, planting_cost, IsFertilized, soil_quality, fertilizer_bonus, fertilizer_cost,
                               harvest_cost, bottling_cost, plants_per_bottle, transport_cost, vineprice, magazine_cost,
                               magazine_capacity,store_needs, upper, lower)

            # + funkcja aspiracji
            # TODO - dodać licznik użyć kryterium aspiracji
            value = sum(gain) - sum(loss)
            if n not in TL and value - avgMemory[n] * 50 > maxi:
                maxi = value - avgMemory[n] * 50  # no jak było wybierane to mniej
                maxval = value
                gain_rem = gain
                loss_rem = loss
                n_rem = n
            # print(n_rem)
            # TODO - Przy długich tabu listach jest problem - maxval = -np.inf
        limsta.append(maxval)

        if LongTermMem:
            avgMemory[n_rem] = avgMemory[n_rem] + 1

        if maxval <= past_sol:
            streak += 1
            print(maxval - past_sol)
        else:
            streak = 0

        if maxval >= bs:
            bs_solution = mapa[n_rem].copy()
            bs_gain_rem = gain_rem
            bs_loss_rem = loss_rem
            bs = maxval
            bs_counter_rem = counter + 1

        # Obecne rozwiązanie
        solution = mapa[n_rem].copy()

        if (tabulist):
            nik = generateAntiNum(n_rem)
            if len(TL) < tabu_length and nik not in TL:
                TL.append(nik)
            elif len(TL) < tabu_length and nik in TL:
                idx = TL.index(nik)
                TL.pop(idx)
                TL.append(nik)
            elif len(TL) >= tabu_length and nik in TL:
                idx = TL.index(nik)
                TL.pop(idx)
                TL.append(nik)
            elif len(TL) >= tabu_length and nik not in TL:
                TL.pop(0)
                TL.append(nik)

        print(TL)
        # Kryterium aspiracji tu ma być
        if streak >= midtemmemTreshold:
            print('--------------------------------yuk')
            solution = beg_sol  # Tutaj dajemy możliwość wyboru z tabu listy i mamy kryterium aspiracji
            streak = 0
            aspi_counter += 1
            # tutaj ten reset ale nei wiem jak to zrobić
            # nalepiej sol=gennewcompletlynewsol()

        if abs(past_sol - maxval) <= epsilon:
            stop_eps = True

        counter += 1

        if abs(past_sol - maxval) <= minieps:
            minieps = round(abs(past_sol - maxval), len(str(epsilon)))
            #self.stat6.setText(str(minieps) + '/ it: ' + str(counter)) #wyswietlanie

        dane.append(
            [counter, round(sum(gain_rem), 2), round(sum(loss_rem), 2), round(sum(gain_rem) - sum(loss_rem), 2),
             len(TL), wypisz(solution, ch_types)])

        print(counter)
        if counter >= max_iter:
            stop_iter = True

        past_sol = maxval
    '''                                     # to chyba też wyświetlanie?
    if stop_eps and stop_iter:
        self.stat9.setText('Kryterium dokładności i maksymalnej liczby iteracji')
    elif stop_eps:
        self.stat9.setText('Kryterium dokładności')
    elif stop_iter:
        self.stat9.setText('Kryterium maksymalnej liczby iteracji')
    else:
        print("WARNING!")
    
        # print(avgMemory)
    self.stat5.setText(str(counter) + '/' + str(max_iter))
    '''
    ac = limsta[0]
    better_counter = 0
    worse_counter = 0

    for i in limsta[1:]:
        if i < ac:
            worse_counter += 1
        elif i > ac:
            better_counter += 1
        ac = i

    #self.stat7.setText(str(better_counter))
    #self.stat8.setText(str(worse_counter))

    #self.pb.setValue(max_iter)

    #self.c.plotting(limsta)
    #self.c.setVisible(True)

    #self.stat3.setText(str(round(limsta[-1], 2)) + f'/ it: {counter}')
    #self.stat2.setText(str(round(sum(bs_gain_rem) - sum(bs_loss_rem), 2)) + f'/ it: {bs_counter_rem}')
    # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)
    #self.stat10.setText(wypisz(bs_solution, self.ch_types))

    #self.stat4.setText(str(aspi_counter))

    #self.c5.plot_main(bs_gain_rem, bs_loss_rem, 'ending_main_linear_plot')
    #self.c5.setVisible(True)

    #self.c6.plot_bar(bs_gain_rem, bs_loss_rem, 'ending_bar_plot')
    #self.c6.setVisible(True)

    #self.c7.plot_bar2(bs_gain_rem, bs_loss_rem, bs_solution.shape[0], 'ending_detailed_bar_plot')
    #self.c7.setVisible(True)

    #self.t.setRowCount(len(dane))
    #self.t.setColumnCount(len(dane[0]))
    #self.t.setHorizontalHeaderLabels(["Iteracja", "zysk", "strata", "bilans", "Aktualna długość TL", "Opis"])

    #for k in range(len(dane)):
    #    for i in range(len(dane[0])):
    #        self.t.setItem(k, i, QTableWidgetItem(str(dane[k][i])))
    #self.t.resizeColumnsToContents()
    #self.t.resizeRowsToContents()

    return bs_solution