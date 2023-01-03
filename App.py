from PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui
from Command_files import *
from Generators import *
from Wykresy import *
from canvas import *
import pandas as pd
import xlsxwriter
import os
cur = os.path.abspath(os.getcwd())


# import sys
# f = open("Wyniki/Tabele/algorytm.txt", 'w')
# sys.stdout = f

class UI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.clicked = None
        uic.loadUi("Projekt/app.ui", self)
        self.setWindowIcon(QtGui.QIcon("Projekt/2836932.png"))

        ### Scrolle
        self.st = self.findChild(QStackedWidget, "stackedWidget")
        self.st2 = self.findChild(QStackedWidget, "stackedWidget_2")
        self.st3 = self.findChild(QStackedWidget, "stackedWidget_3")
        self.st4 = self.findChild(QStackedWidget, "st4")

        # Wyzerowanie scrolli
        self.st.setCurrentIndex(1)
        self.st2.setCurrentIndex(1)
        self.st3.setCurrentIndex(1)
        self.st4.setCurrentIndex(0)

        ### MENU



        ## Menu przyciski

        self.bset = self.findChild(QPushButton, "btn_set")
        self.bset.clicked.connect(lambda: self.st.setCurrentIndex(0))

        self.b2 = self.findChild(QPushButton, "btn_page_1")
        self.b2.clicked.connect(lambda: self.st.setCurrentIndex(1))

        self.b3 = self.findChild(QPushButton, "btn_page_2")
        self.b3.clicked.connect(lambda: self.st.setCurrentIndex(2))

        self.b4 = self.findChild(QPushButton, "btn_page_3")
        self.b4.clicked.connect(lambda: self.st.setCurrentIndex(3))

        self.b4 = self.findChild(QPushButton, "btn_page4")
        self.b4.clicked.connect(lambda: self.st.setCurrentIndex(4))

        self.b5 = self.findChild(QPushButton, "btn_info")
        self.b5.clicked.connect(lambda: self.st.setCurrentIndex(5))

        # progressbar w MENUu

        self.pb = self.findChild(QProgressBar, "pb")
        self.pb.setTextVisible(False)

        # START w MENU
        self.button3 = self.findChild(QPushButton, "start")
        self.button3.clicked.connect(self.start_tabu)

        # Rozpiska w menu
        self.text = self.findChild(QLabel, 'text')
        self.text2 = self.findChild(QLabel, 'text_2')
        self.text3 = self.findChild(QLabel, 'text_3')
        self.text4 = self.findChild(QLabel, 'text_4')
        self.text5 = self.findChild(QLabel, 'text_5')
        self.text6 = self.findChild(QLabel, 'text_6')

        self.mn = self.findChild(QPushButton, "mn")
        self.mn.clicked.connect(lambda: self.st4.setCurrentIndex(1))

        self.mn2 = self.findChild(QPushButton, "mn_2")
        self.mn2.clicked.connect(lambda: self.st4.setCurrentIndex(0))

        # self.mn3 = self.findChild(QPushButton, "mn_3")
        # self.mn3.clicked.connect(lambda: self.st4.setCurrentIndex(2))

        ## TABELE
        self.lik = self.findChild(QLabel, 'p_1')
        txt = cur + r'\Wyniki\Tabele\ceny_wina.csv'
        self.lik.setText(f'<a href="{txt}" style="color: white;">Ceny win</a>' )




        ### WYKRESY

        ## Przyciski
        # Przyciemnienie
        self.d = self.findChild(QLabel, 'dark')
        self.d1 = self.findChild(QLabel, 'dark_2')
        self.d2 = self.findChild(QLabel, 'dark_3')
        self.d3 = self.findChild(QLabel, 'dark_4')
        self.d4 = self.findChild(QLabel, 'dark_5')
        self.d5 = self.findChild(QLabel, 'dark_6')
        self.d6 = self.findChild(QLabel, 'dark_7')
        self.d7 = self.findChild(QLabel, 'dark_8')
        self.shader(self.d)

        # ceny wina
        self.w = self.findChild(QPushButton, "w_1")
        self.w.clicked.connect(lambda: (self.st3.setCurrentIndex(1), self.shader(self.d)))

        # wykres początkowy
        self.w1 = self.findChild(QPushButton, "w_2")
        self.w1.clicked.connect(lambda: (self.st3.setCurrentIndex(2), self.shader(self.d1)))

        # słupki początkowe 1
        self.w2 = self.findChild(QPushButton, "w_3")
        self.w2.clicked.connect(lambda: (self.st3.setCurrentIndex(3), self.shader(self.d2)))

        # słupki początkowe 2
        self.w21 = self.findChild(QPushButton, "w_31")
        self.w21.clicked.connect(lambda: (self.st3.setCurrentIndex(4), self.shader(self.d3)))

        # tabu search
        self.w3 = self.findChild(QPushButton, "w_4")
        self.w3.clicked.connect(lambda: (self.st3.setCurrentIndex(0), self.shader(self.d4)))

        # wykres początkowy
        self.w4 = self.findChild(QPushButton, "w_5")
        self.w4.clicked.connect(lambda: (self.st3.setCurrentIndex(5), self.shader(self.d5)))

        # słupki początkowe 1
        self.w5 = self.findChild(QPushButton, "w_6")
        self.w5.clicked.connect(lambda: (self.st3.setCurrentIndex(6), self.shader(self.d6)))

        # słupki początkowe 2
        self.w51 = self.findChild(QPushButton, "w_61")
        self.w51.clicked.connect(lambda: (self.st3.setCurrentIndex(7), self.d7.setVisible(True), self.shader(self.d7)))

        # Wykres 0 - tabu search
        self.c = self.findChild(QWidget, 'widget')
        self.c.setVisible(False)

        # Wykres 1 - ceny win
        self.c1 = self.findChild(QWidget, 'widget_2')
        self.c1.setVisible(False)

        # Wykres 2 - główny plot dla poczatkowego
        self.c2 = self.findChild(QWidget, 'widget_3')
        self.c2.setVisible(False)

        # Wykres 3 - bar plot dla poczatkowego 1
        self.c3 = self.findChild(QWidget, 'widget_4')
        self.c3.setVisible(False)

        # Wykres 5 - bar plot dla poczatkowego 2
        self.c4 = self.findChild(QWidget, 'widget_5')
        self.c4.setVisible(False)

        # Wykres 6 - główny plot dla końcowego
        self.c5 = self.findChild(QWidget, 'widget_6')
        self.c5.setVisible(False)

        # Wykres 7 - bar plot dla końcowego 1
        self.c6 = self.findChild(QWidget, 'widget_7')
        self.c6.setVisible(False)

        # Wykres 8 - bar plot dla końcowego 2
        self.c7 = self.findChild(QWidget, 'widget_8')
        self.c7.setVisible(False)

        #
        self.t = self.findChild(QTableWidget, 'tw')
        self.t.setVisible(False)

        ### USTAWIENIA
        ## Ustawienia - przyciski
        self.n = self.findChild(QPushButton, "next")
        self.n.clicked.connect(lambda: self.st2.setCurrentIndex(0))

        self.n1 = self.findChild(QPushButton, "next_2")
        self.n1.clicked.connect(lambda: self.st2.setCurrentIndex(2))

        self.n2 = self.findChild(QPushButton, "next_3")
        self.n2.clicked.connect(lambda: self.st2.setCurrentIndex(3))

        self.p = self.findChild(QPushButton, "prev")
        self.p.clicked.connect(lambda: self.st2.setCurrentIndex(1))

        self.p1 = self.findChild(QPushButton, "prev_2")
        self.p1.clicked.connect(lambda: self.st2.setCurrentIndex(0))

        self.p2 = self.findChild(QPushButton, "prev_3")
        self.p2.clicked.connect(lambda: self.st2.setCurrentIndex(2))

        ## Ustawienia - podstawowe dane

        # tabela
        self.tab = self.findChild(QTableWidget, "tableWidget")

        # flaga
        self.flaga = self.findChild(QCheckBox, "flaga")
        self.flaga2 = self.findChild(QCheckBox, "flaga_2")
        self.store_need = [100,100,100]

        # Liczba pól
        self.nr_field = self.findChild(QSpinBox, "fieldnum")
        self.fields = int(self.nr_field.text())

        # Liczba lat/miesięcy
        self.nr_time = self.findChild(QSpinBox, "timenum")
        self.num_of_years = int(self.nr_time.text())

        # Zapotrzebowanie
        self.zap = self.findChild(QTableWidget, "zap")
        self.ch_types = {1: 'Barbera', 2: 'Chardonnay', 3: 'Nebbiolo'}
        self.xclear = self.findChild(QPushButton, "xclear")
        self.xclear .clicked.connect(lambda: self.zap.clearContents())

        # Odświeżanie tabeli
        self.rt = self.findChild(QPushButton, "refreshtab")
        self.rt.clicked.connect(
            lambda: (self.tab.setRowCount(int(self.nr_field.text())), self.grape_type_choice()))

        # Czyszczenie tabeli
        self.ct = self.findChild(QPushButton, "cleartab")
        self.ct.clicked.connect(lambda: self.tab.clearContents())


        ## Ustawienia - rodzaje,nawozy,zbiory

        # Odczyt typów wina
        self.v1 = self.findChild(QCheckBox, 'Barbera')
        self.v2 = self.findChild(QCheckBox, 'Chardonnay')
        self.v3 = self.findChild(QCheckBox, 'Nebbiolo')
        self.v4 = self.findChild(QCheckBox, 'Arneis')
        self.v5 = self.findChild(QCheckBox, 'Dolcetto')
        self.v6 = self.findChild(QCheckBox, 'Cortese')
        self.v7 = self.findChild(QCheckBox, 'Grignolino')
        self.v8 = self.findChild(QCheckBox, 'Erbaluce')

        # Czy używamy trojpolówki?
        self.troj = self.findChild(QCheckBox, "troj")
        self.troj.toggled.connect(lambda: self.checktroj())
        self.trojka = False

        # Czy używamy nawozu
        self.ch1 = self.findChild(QCheckBox, "checkBox")
        self.IsFertilized = 1
        self.ch1.toggled.connect(lambda: self.check())

        # Typ nawozu
        self.nawoz = self.findChild(QComboBox, "nawoz")
        self.fertilizer_bonus = 0.05
        self.fertilizer_cost = 2.00

        # Koszt zbioru
        self.zbior = self.findChild(QDoubleSpinBox, "zbior")
        self.harvest_cost = float(self.zbior.text())

        ## Ustawienia - butelkowanie, magazynowanie, transport

        # Pojemność magazynu
        self.magcap = self.findChild(QSpinBox, "capacity")
        self.magazine_capacity = int(self.magcap.text())

        # Koszt magazynowania
        self.magcost = self.findChild(QDoubleSpinBox, "magcost")
        self.magazine_cost = float(self.magcost.text())

        # Ilość jednostek winogron na butelkę
        self.jperbot = self.findChild(QSpinBox, "jperbot")
        self.plants_per_bottle = int(self.jperbot.text())

        # Koszt transportu
        self.transcost = self.findChild(QDoubleSpinBox, "transcost")
        self.transport_cost = float(self.transcost.text())

        # Koszt butelkowania
        self.botcost = self.findChild(QDoubleSpinBox, "botcost")
        self.bottling_cost = float(self.botcost.text())

        # Odświeżanie tabeli
        self.rt2 = self.findChild(QPushButton, "refreshtab_2")
        self.rt2.clicked.connect(
            lambda: (self.zap.setRowCount(len(self.ch_types) + 1),
                     self.zap.setVerticalHeaderLabels(list(self.ch_types.values()) + ['']), self.grape_type_choice()))

        ## Ustawienia - ustawienia algorytmu

        # Epsilon
        self.eps = self.findChild(QDoubleSpinBox, "eps")
        self.epsilon = float(self.eps.text())

        # Iteracje
        self.iter = self.findChild(QSpinBox, "iter")
        self.max_iter = int(self.iter.text())

        # Długość TL
        self.tl = self.findChild(QSpinBox, "TL")
        self.tabu_length = int(self.tl.text())

        # Typy TL
        self.smol = self.findChild(QCheckBox, "smol")
        self.tabulist = self.smol.isChecked()

        self.med = self.findChild(QCheckBox, "med")
        self.MidTermMem = self.med.isChecked()

        self.lon = self.findChild(QCheckBox, "lon")
        self.LongTermMem = self.lon.isChecked()

        # Typy sąsiedztwa
        self.sasiad = self.findChild(QCheckBox, "sasiedztwo")
        self.sasiad2 = self.findChild(QCheckBox, "sasiedztwo_2")
        self.sasiad3 = self.findChild(QCheckBox, "sasiedztwo_3")
        self.sasiad4 = self.findChild(QCheckBox, "sasiedztwo_4")
        self.som = self.findChild(QDoubleSpinBox, "som")
        self.SolutionSpaceCoverage = float(self.som.text())

        # Typy rozwiązania początkowego
        self.pocz = self.findChild(QCheckBox, "roz_beg")
        self.pocz2 = self.findChild(QCheckBox, "roz_beg_2")
        self.pocz3 = self.findChild(QCheckBox, "roz_beg_3")
        self.pocz4 = self.findChild(QCheckBox, "roz_beg_4")

        # Kryterium aspiracji - tak/nie
        self.aspik= self.findChild(QCheckBox, "aspi")
        self.aspicheck = self.aspik.isChecked()

        # Długość do kryterium aspiracji
        self.aspinum = self.findChild(QSpinBox, "aspi_2")
        self.midtemmemTreshold = int(self.aspinum.text())

        ## Ustawienia przyciski

        # zatwierdź
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.get)

        # Czyszczenie
        self.button2 = self.findChild(QPushButton, "pushButton_2")

        # TODO: Dopisać wartości podstawowe dla reszty przycisków
        self.button2.clicked.connect(lambda: self.input.setValue(0.10))
        self.button2.clicked.connect(lambda: self.input2.setValue(50))

        self.warn = self.findChild(QLabel, 'warnin')
        self.warn1 = self.findChild(QLabel, 'warn1')
        self.warn2 = self.findChild(QLabel, 'warn2')
        self.warn2.setVisible(False)

        self.warn3 = self.findChild(QLabel, 'warn3')
        self.warnin2 = self.findChild(QLabel, 'warnin_2')
        self.warnin2.setVisible(False)

        self.warn4 = self.findChild(QLabel, 'warn4')
        self.warnin3 = self.findChild(QLabel, 'warnin_3')
        self.warnin3.setVisible(False)

        self.warnin4 = self.findChild(QLabel, 'warnin_4')
        self.warnin4.setVisible(False)

        self.upper = [800, 800, 800]
        self.lower = [100, 100, 100]
        self.show_yourself()
        self.set()

    def set(self):
        self.text.setText(str(self.num_of_years))
        self.text2.setText(str(self.nr_field.text()))
        self.text3.setText(str(self.max_iter))
        self.text4.setText(str(self.epsilon))
        self.text5.setText(str(self.tabu_length))
        self.text6.setText(str(self.magazine_capacity))

    def shader(self, cur):
        for d in [self.d, self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7]:
            if d != cur:
                d.setVisible(False)
            else:
                d.setVisible(True)

    def check(self):
        if self.ch1.isChecked():
            self.IsFertilized = 1
        else:
            self.IsFertilized = 0

    def checktroj(self):
        if self.troj.isChecked():
            self.trojka = True
        else:
            self.trojka = False

    # Tworzy słownik wybranych rodzajów wina
    def grape_type_choice(self):
        d = dict()
        types = [self.v1, self.v2, self.v3, self.v4,
                 self.v5, self.v6, self.v7, self.v8]
        c = 1
        for t in types:
            if t.isChecked():
                d[c] = t.text()
            c += 1
        self.ch_types = d

    def get(self):
        self.warn.clear()
        self.warn1.clear()
        self.warn2.setVisible(False)
        self.warn2.clear()

        self.grape_type_choice()
        if self.ch_types == {}:
            self.warn.setText(u"\u26A0" + ' Musisz ustawić co najmniej jeden typ!')
            self.warn1.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')
        else:

            self.epsilon = float(self.eps.text())
            self.max_iter = int(self.iter.text())
            self.num_of_years = int(self.nr_time.text())
            self.magazine_capacity = int(self.magcap.text())
            self.magazine_cost = float(self.magcost.text())
            self.plants_per_bottle = int(self.jperbot.text())
            self.transport_cost = float(self.transcost.text())
            self.bottling_cost = float(self.botcost.text())
            self.harvest_cost = float(self.zbior.text())
            self.acctab()
            self.acczap()
            self.tab.setRowCount(int(self.nr_field.text()))
            self.zap.setRowCount(len(self.ch_types) + 1)
            self.zap.setVerticalHeaderLabels(list(self.ch_types.values()) + [''])

            self.tabulist = self.smol.isChecked()
            self.MidTermMem = self.med.isChecked()
            self.LongTermMem = self.lon.isChecked()
            self.SolutionSpaceCoverage = float(self.som.text())
            self.aspicheck = self.aspik.isChecked()
            self.midtemmemTreshold = int(self.aspinum.text())

            if self.nawoz.currentText() == 'Standardowy (+5%) - 2zł/szt':
                self.fertilizer_bonus = 0.05
                self.fertilizer_cost = 2.00
            elif self.nawoz.currentText() == 'Wyższej jakości (+10%) - 4zł/szt':
                self.fertilizer_bonus = 0.10
                self.fertilizer_cost = 4.00
            else:
                self.fertilizer_bonus = 0.17
                self.fertilizer_cost = 7.00

        self.set()


    def start_tabu(self):
        try:

            self.show_yourself()
            
            sol = generate_solution(self.magazine_capacity, self.upper, self.lower, self.num_of_years, len(self.ch_types))
            writer = pd.ExcelWriter('Wyniki/Tabele/rozwiazanie_pocz.xlsx', engine='xlsxwriter')
            for i in range(self.num_of_years * 12):
                df0 = pd.DataFrame(data=sol[i, :, :].astype(int))
                df0.insert(loc=0, column='Pole', value=list(range(1,self.fields+1)))
                df0.to_excel(writer, sheet_name=f'Miesiac {i + 1}',
                             header=['Pole'] + list(self.ch_types.values()), index=False)
            writer.close()


            planting_cost = plant_price_generator(self.ch_types)
            df1 = pd.DataFrame(data={'Typ':list(self.ch_types.values()), 'Cena': planting_cost.astype(float)})
            df1.to_csv('Wyniki/Tabele/ceny_sadzenia.csv', sep=' ', header=None, float_format='%.2f', index=False)

            soil_quality = soil_quality_generator(self.fields, self.num_of_years, self.ch_types, self.trojka)
            writer = pd.ExcelWriter('Wyniki/Tabele/jakosc_gleby.xlsx', engine='xlsxwriter')
            for i in range(self.num_of_years * 12):
                df2 = pd.DataFrame(data=soil_quality[i, :, :].astype(float))
                df2.insert(loc=0, column='Pole', value=list(range(1,self.fields+1)))
                df2.to_excel(writer, sheet_name=f'Miesiac {i + 1}',
                             header=['Pole'] + list(self.ch_types.values()), index=False)
            writer.close()

            vineprice = vine_price_generator(self.ch_types, self.num_of_years)
            df3 = pd.DataFrame(data=vineprice.astype(float),columns=list('m'+str(i) for i in range(1,self.num_of_years*12+1)))
            df3.insert(loc=0,column='Typ',value=list(self.ch_types.values()))
            df3.to_csv('Wyniki/Tabele/ceny_wina.csv', sep=' ', index=False)

            self.c1.plot_vineprice(self.ch_types, self.num_of_years, vineprice)
            self.c1.setVisible(True)


            # Tabu search wbudowany
            self.tabu_search(sol, planting_cost,
                             self.IsFertilized, soil_quality,
                             self.fertilizer_bonus, self.fertilizer_cost,
                             self.harvest_cost, self.bottling_cost,
                             self.plants_per_bottle, self.transport_cost,
                             vineprice, self.magazine_cost, self.magazine_capacity, self.store_need, self.ch_types,
                             self.tabu_length, self.max_iter, self.epsilon)
            self.pb.setValue(0)
            self.pb.setTextVisible(False)

        except:
            print('Coś poszło nie tak!')

    def tabu_search(self, beg_sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    tabu_length=10, max_iter=50, epsilon=0.1):



        #flagi

        LongTermMem=self.LongTermMem
        SolutionSpaceCoverage=self.SolutionSpaceCoverage
        MidTermMem=self.MidTermMem#non implemented
        tabulist=self.tabulist
        midtemmemTreshold=self.midtemmemTreshold

        gain, loss = ocena(beg_sol, planting_cost,
                           IsFertilized, soil_quality,
                           fertilizer_bonus, fertilizer_cost,
                           harvest_cost, bottling_cost,
                           plants_per_bottle, transport_cost,
                           vineprice, magazine_cost, magazine_capacity, store_needs)

        self.beg = sum(gain) - sum(loss)

        self.c2.plot_main(gain, loss,'beginning_main_linear_plot')
        self.c2.setVisible(True)

        self.c3.plot_bar(gain, loss,'beginning_bar_plot')
        self.c3.setVisible(True)

        self.c4.plot_bar2(gain, loss, beg_sol.shape[0],'beginning_detailed_bar_plot')
        self.c4.setVisible(True)

        self.t.setVisible(True)
        # sol_present_yourself(gain, loss, beg_sol, ch_types)

        TL = []
        avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[
            2]))  # pamiec srednioteminowa zlicza rozwiazania dane
        streak = 0

        solution = beg_sol.copy()
        past_sol = sum(gain) - sum(loss)

        # Najlepsze
        bs_solution = solution.copy()
        bs = sum(gain) - sum(loss)

        gain_rem = 0
        loss_rem = 0

        stop_iter = False
        stop_eps = False
        counter = 0
        self.pb.setTextVisible(True)
        self.pb.setMaximum(max_iter)

        # DANE
        dane = [[counter, round(sum(gain), 2), round(sum(loss), 2), round(sum(gain) - sum(loss), 2), len(TL),
                 wypisz(beg_sol, ch_types)]]

        limsta = []
        # print(solution)
        print('----------------------------------------------------')
        while not (stop_iter or stop_eps):
            self.pb.setValue(counter)
            mapa = generateAllsolutions(solution,numberofsolutions=SolutionSpaceCoverage)
            # print(mapa)
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
                value = sum(gain) - sum(loss)
                if n not in TL and value - avgMemory[n] * 2 > maxi:
                    maxi = sum(gain) - sum(loss) - avgMemory[n] * 2  # no jak było wybierane to mniej
                    maxval = sum(gain) - sum(loss)
                    gain_rem = gain
                    loss_rem = loss
                    n_rem = n
            # print(n_rem)

            limsta.append(maxval)
            if LongTermMem:
                avgMemory[n_rem] = avgMemory[n_rem] + 1




            limsta.append(value)

            if maxval >= bs:
                solution = mapa[n_rem].copy()
                streak = 0
            else:
                if MidTermMem:
                    streak = streak + 1
                solution = mapa[n_rem].copy()

            if(tabulist):
                if len(TL) < tabu_length:
                    TL.append(generateAntiNum(n_rem))
                else:
                    TL.pop(0)
                    TL.append(generateAntiNum(n_rem))

            if streak > midtemmemTreshold:
                print('--------------------------------yuk')
                solution = beg_sol
                counter = 0
                #tutaj ten reset ale nei wiem jak to zrobić
                #nalepiej sol=gennewcompletlynewsol()


            if abs(past_sol - maxval) <= epsilon:
                stop_eps = True

            past_sol = maxval

            counter += 1
            dane.append(
                [counter, round(sum(gain_rem), 2), round(sum(loss_rem), 2), round(sum(gain_rem) - sum(loss_rem), 2),
                 len(TL), wypisz(solution, ch_types)])
            print(counter)
            if counter >= max_iter:
                stop_iter = True

        self.pb.setValue(max_iter)

        self.c.plotting(limsta)
        self.c.setVisible(True)

        # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

        self.c5.plot_main(gain_rem, loss_rem,'ending_main_linear_plot')
        self.c5.setVisible(True)

        self.c6.plot_bar(gain_rem, loss_rem,'ending_bar_plot')
        self.c6.setVisible(True)

        self.c7.plot_bar2(gain_rem, loss_rem, bs_solution.shape[0],'ending_detailed_bar_plot')
        self.c7.setVisible(True)

        self.t.setRowCount(len(dane))
        self.t.setColumnCount(len(dane[0]))
        self.t.setHorizontalHeaderLabels(["Iteracja", "zysk", "strata", "bilans", "Aktualna długość TL", "Opis"])

        self.best = None
        self.actual = None
        for k in range(len(dane)):
            for i in range(len(dane[0])):
                self.t.setItem(k, i, QTableWidgetItem(str(dane[k][i])))
        self.t.resizeColumnsToContents()
        self.t.resizeRowsToContents()

        return bs_solution

    def acctab(self):
        try:
            upper = []
            lower = []
            for row in range(self.tab.rowCount()):
                for column in range(self.tab.columnCount()):
                    _item = self.tab.item(row, column)

                    if _item:
                        try:
                            item = int(self.tab.item(row, column).text())
                        except:
                            raise TypeError
                    else:
                        item = 0

                    if column == 0:
                        upper.append(item)
                    elif column == 1:
                        upper[row] *= item
                    else:
                        lower.append(item)


            if upper[0] != 0 and self.flaga.isChecked():
                upper = [upper[0]] * self.tab.rowCount()
                lower = [lower[0]] * self.tab.rowCount()

            self.upper = upper
            self.lower = lower
            self.warnin2.setVisible(False)
            self.warn3.setText("")
            self.warn2.setVisible(False)
            self.warnin4.setVisible(False)

            for x in range(len(lower)):
                if lower[x] > upper[x]:
                    raise ValueError
                if upper[x] == 0:
                    raise ZeroDivisionError
                if lower[x] < 0 or 0 > upper[x]:
                    raise AttributeError

            if sum(lower) > self.magazine_capacity:
                raise InterruptedError

        except ValueError:
            self.warnin2.setVisible(True)
            self.warnin2.setText(u"\u26A0" + ' Złe wejście tabeli! Ograniczenie górne mniejsze od dolnego.')

            self.warn3.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

        except InterruptedError:
            self.warnin4.setVisible(True)
            self.warnin4.setText(u"\u26A0" + ' Za mała pojemność magazynu!')

            self.warn4.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

        except AttributeError:
            self.warnin2.setVisible(True)
            self.warnin2.setText(u"\u26A0" + ' Złe wejście tabeli! Nie mogą być mniejsze od 0!')

            self.warn3.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

        except ZeroDivisionError:

            self.warnin2.setVisible(True)
            self.warnin2.setText(u"\u26A0" + ' Złe wejście tabeli! Ograniczenie górne nie może być równe 0.')

            self.warn3.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

        except TypeError:

            self.warnin2.setVisible(True)
            self.warnin2.setText(u"\u26A0" + ' Złe wejście tabeli!')

            self.warn3.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

        except:
            self.warnin2.setVisible(True)
            self.warnin2.setText(u"\u26A0" + 'Coś poszło nie tak!')

            self.warn3.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.upper = []
            self.lower = []

    def acczap(self):
        try:
            zap = []
            for row in range(self.zap.rowCount()):
                for column in range(self.zap.columnCount()):
                    print('h')
                    _item = self.zap.item(row, column)
                    if _item:
                        try:
                            item = int(self.zap.item(row, column).text())
                        except:
                            raise TypeError
                    else:
                        item = 0

                    zap.append(item)

            if zap[0] != 0 and self.flaga2.isChecked():
                zap = [zap[0]] * self.zap.rowCount()

            for x in zap:
                if x < 0:
                    raise ArithmeticError

            self.store_need = zap[:-1]
            self.warnin3.setVisible(False)
            self.warn4.setText("")

        except TypeError:

            self.warnin3.setVisible(True)
            self.warnin3.setText(u"\u26A0" + ' Złe wejście tabeli!')

            self.warn4.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.store_need = []

        except ArithmeticError:

            self.warnin3.setVisible(True)
            self.warnin3.setText(u"\u26A0" + ' Wartość mniejsza od 0!')

            self.warn4.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.store_need = []

        except:
            self.warnin3.setVisible(True)
            self.warnin3.setText(u"\u26A0" + ' Coś poszło nie tak!')

            self.warn4.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

            self.store_need = []


        print(self.store_need)

    def show_yourself(self):
        print(self.epsilon,'\n',
              self.max_iter,'\n',
              self.num_of_years,'\n',
              self.magazine_capacity,'\n',
              self.magazine_cost,'\n',
              self.plants_per_bottle,'\n',
              self.transport_cost,'\n',
              self.bottling_cost,'\n',
              self.harvest_cost,'\n',
              self.lower,'\n',
              self.upper,'\n',
              self.ch_types)


app = QApplication([])
window = UI()
window.show()
app.exec()

# f.close()
