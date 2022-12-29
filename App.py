from PyQt6.QtWidgets import *
from PyQt6 import uic,QtGui
from Command_files import *
from Generators import *
from Wykresy import *
from canvas import *


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

        # Wyzerowanie scrolli
        self.st.setCurrentIndex(1)
        self.st2.setCurrentIndex(1)
        self.st3.setCurrentIndex(1)

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

        self.pb = self.findChild(QProgressBar,"pb")
        self.pb.setTextVisible(False)

        # START w MENU
        self.button3 = self.findChild(QPushButton, "start")
        self.button3.clicked.connect(self.start_tabu)

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
        self.w4.clicked.connect(lambda: (self.st3.setCurrentIndex(5),self.shader(self.d5)))

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
        # self.t.setVisible(False)


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
        self.tab = self.findChild(QTableWidget,"tableWidget")

        # flaga
        self.flaga = self.findChild(QCheckBox,"flaga")

        # Liczba pól
        self.nr_field = self.findChild(QSpinBox,"fieldnum")


        # Liczba lat/miesięcy
        self.nr_time = self.findChild(QSpinBox, "timenum")
        self.num_of_years = int(self.nr_time.text())

        # Zapotrzebowanie
        self.zap = self.findChild(QTableWidget, "zap")
        self.ch_types = {1:'Barbera', 2:'Chardonnay', 3: 'Nebbiolo'}
        # Odświeżanie tabeli
        self.rt = self.findChild(QPushButton,"refreshtab")
        self.rt.clicked.connect(lambda: (self.tab.setRowCount(int(self.nr_field.text())),self.zap.setRowCount(len(self.ch_types)+1),
                                         self.zap.setVerticalHeaderLabels(list(self.ch_types.values())+[''])))

        # Czyszcenie tabeli
        self.ct = self.findChild(QPushButton,"cleartab")
        self.ct.clicked.connect(lambda: self.tab.clearContents())

        # Zaakceptowanie tabeli
        self.at = self.findChild(QPushButton,"accepttab")
        self.at.clicked.connect(lambda: self.acctab())


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

        ## Ustawienia przyciski

        # zatwierdź
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.get)
        self.button.clicked.connect(self.grape_type_choice)

        # Czyszczenie
        self.button2 = self.findChild(QPushButton, "pushButton_2")

        # TODO: Dopisać wartości podstawowe dla reszty przycisków
        self.button2.clicked.connect(lambda: self.input.setValue(0.10))
        self.button2.clicked.connect(lambda: self.input2.setValue(50))

        self.warn = self.findChild(QLabel, 'warnin')
        self.warn1 = self.findChild(QLabel, 'warn1')
        self.warn2 = self.findChild(QLabel, 'warn2')
        self.warn2.setVisible(False)

        self.h = [800,800,800]
        self.l = [100,100,100]

    def shader(self, cur):
        for d in [self.d,self.d1,self.d2,self.d3,self.d4,self.d5,self.d6,self.d7]:
            if d != cur:
                d.setVisible(False)
            else:
                d.setVisible(True)

    def check(self):
        if self.ch1.isChecked():
            self.IsFertilized = 1
        else:
            self.IsFertilized = 0

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

        return d

    def get(self):

        if self.grape_type_choice() == {}:
            self.warn.setText(u"\u26A0"+' Musisz ustawić co najmniej jeden typ!')
            self.warn1.setText(u"\u26A0")
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0"+' Coś poszło nie tak! Sprawdź ustawienia.')
        else:
            self.warn.clear()
            self.warn1.clear()
            self.warn2.setVisible(False)
            self.warn2.clear()

            self.epsilon = float(self.eps.text())
            self.max_iter = int(self.iter.text())
            self.num_of_years = int(self.nr_time.text())
            self.magazine_capacity = int(self.magcap.text())
            self.magazine_cost = float(self.magcost.text())
            self.plants_per_bottle = int(self.jperbot.text())
            self.transport_cost = float(self.transcost.text())
            self.bottling_cost = float(self.botcost.text())
            self.harvest_cost = float(self.zbior.text())
            self.ch_types = self.grape_type_choice()
            self.acctab()

            if self.nawoz.currentText() == 'Standardowy (+5%) - 2zł/szt':
                self.fertilizer_bonus = 0.05
                self.fertilizer_cost = 2.00
            elif self.nawoz.currentText() == 'Wyższej jakości (+10%) - 4zł/szt':
                self.fertilizer_bonus = 0.10
                self.fertilizer_cost = 4.00
            else:
                self.fertilizer_bonus = 0.17
                self.fertilizer_cost = 7.00


    def start_tabu(self):

            if self.ch_types != {}:

                sol = generate_solution(self.magazine_capacity,  self.h, self.l, self.num_of_years, len(self.ch_types))

                planting_cost = plant_price_generator(self.ch_types)
                soil_quality = soil_quality_generator(len(self.ch_types), self.num_of_years, self.ch_types)
                vineprice = vine_price_generator(self.ch_types, self.num_of_years)

                self.c1.plot_vineprice(self.ch_types, self.num_of_years, vineprice)
                self.c1.setVisible(True)

                store_needs = [100, 100, 100]
                # Tabu search wbudowany
                self.tabu_search(sol, planting_cost,
                            self.IsFertilized, soil_quality,
                            self.fertilizer_bonus, self.fertilizer_cost,
                            self.harvest_cost, self.bottling_cost,
                            self.plants_per_bottle, self.transport_cost,
                            vineprice, self.magazine_cost, self.magazine_capacity, store_needs, self.ch_types,
                            self.tabu_length, self.max_iter, self.epsilon)

                self.pb.setValue(0)
                self.pb.setTextVisible(False)
            else:
                self.warn.setText(u"\u26A0" + ' Musisz ustawić co najmniej jeden typ!')
                self.warn1.setText(u"\u26A0")
                self.warn2.setVisible(True)
                self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

    def tabu_search(self, beg_sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    tabu_length=10, max_iter=50, epsilon=0.1):



        gain, loss = ocena(beg_sol, planting_cost,
                           IsFertilized, soil_quality,
                           fertilizer_bonus, fertilizer_cost,
                           harvest_cost, bottling_cost,
                           plants_per_bottle, transport_cost,
                           vineprice, magazine_cost, magazine_capacity, store_needs)

        self.c2.plot_main(gain,loss)
        self.c2.setVisible(True)

        self.c3.plot_bar(gain, loss)
        self.c3.setVisible(True)

        self.c4.plot_bar2(gain, loss, beg_sol.shape[0])
        self.c4.setVisible(True)
        # sol_present_yourself(gain, loss, beg_sol, ch_types)

        TL = []
        avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[
            2]))  # pamiec srednioteminowa zlicza rozwiazania dane
        streak = 0
        streaknum = -1

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
        self.pb.setTextVisible(True)
        self.pb.setMaximum(max_iter)

        # DANE
        dane_excel = [[counter, gain, loss, sum(gain) - sum(loss), len(TL), TL]]
        dane = [[counter, round(sum(gain),2),  round(sum(loss),2),  round(sum(gain)-sum(loss),2), len(TL), wypisz(beg_sol, ch_types)]]

        limsta = []

        while not (stop_iter or stop_eps):
            self.pb.setValue(counter)
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
                value = sum(gain) - sum(loss)
                if n not in TL and value - avgMemory[n] * 2 > maxi:
                    maxi = sum(gain) - sum(loss) - avgMemory[n] * 2  # no jak było wybierane to mniej
                    maxval = sum(gain) - sum(loss)
                    gain_rem = gain
                    loss_rem = loss
                    n_rem = n
            # print(n_rem)

            limsta.append(maxval)

            avgMemory[n_rem] = avgMemory[n_rem] + 1
            if n_rem == streaknum:
                streak = streak + 1
            else:
                streaknum = n_rem
                streak = 1
            if streak > 99999:
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
            print(TL)
            if counter > max_iter:
                stop_iter = True

            if abs(past_sol - maxval) <= epsilon:
                stop_eps = True

            past_sol = maxval

            counter += 1
            dane.append([counter, round(sum(gain_rem),2),  round(sum(loss_rem),2),  round(sum(gain_rem)-sum(loss_rem),2), len(TL), wypisz(solution, ch_types)])
            print(counter)
            if counter >= max_iter:
                stop_iter = True

        self.pb.setValue(max_iter)

        # plt.plot(limsta)
        # plt.title('Wykres wartości funkcji celu')
        # plt.show()

        self.c.plotting(limsta)
        self.c.setVisible(True)

        # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

        self.c5.plot_main(gain_rem, loss_rem)
        self.c5.setVisible(True)

        self.c6.plot_bar(gain_rem, loss_rem)
        self.c6.setVisible(True)

        self.c7.plot_bar2(gain_rem, loss_rem, bs_solution.shape[0])
        self.c7.setVisible(True)

        self.t.setRowCount(len(dane))
        self.t.setColumnCount(len(dane[0]))
        self.t.setHorizontalHeaderLabels(["Iteracja", "zysk", "strata","bilans","Aktualna długość TL","Opis"])

        for k in range(len(dane)):
            for i in range(len(dane[0])):
                self.t.setItem(k, i, QTableWidgetItem(str(dane[k][i])))
        self.t.resizeColumnsToContents()
        self.t.resizeRowsToContents()

        return bs_solution

    def acctab(self):
        upper = []
        lower = []
        for row in range(self.tab.rowCount()):
            for column in range(self.tab.columnCount()):
                _item = self.tab.item(row, column)
                if _item:
                    item = int(self.tab.item(row, column).text())
                else:
                    item = 0

                if column == 0:
                    upper.append(item)
                elif column == 1:
                    upper[row] *= item
                else:
                    lower.append(item)
        if upper[0] != 0 and lower[0] != 0 and self.flaga.isChecked():
            upper = [upper[0]] * self.tab.rowCount()
            lower = [lower[0]] * self.tab.rowCount()

        self.h, self.l = upper, lower
        print(self.h)
        print(self.l)

app = QApplication([])
window = UI()
window.show()
app.exec()