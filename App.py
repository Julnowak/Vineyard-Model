from PyQt6.QtWidgets import *
from PyQt6 import uic,QtGui
import pyqtgraph as pg
from Command_files import *
from Generators import *
from Wykresy import *
import time
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
        # ceny wina
        self.w = self.findChild(QPushButton, "w_1")
        self.w.clicked.connect(lambda: self.st3.setCurrentIndex(1))

        # wykres początkowy
        self.w1 = self.findChild(QPushButton, "w_2")
        self.w1.clicked.connect(lambda: self.st3.setCurrentIndex(2))

        # słupki początkowe 1
        self.w2 = self.findChild(QPushButton, "w_3")
        self.w2.clicked.connect(lambda: self.st3.setCurrentIndex(3))

        # słupki początkowe 2
        self.w21 = self.findChild(QPushButton, "w_31")
        self.w21.clicked.connect(lambda: self.st3.setCurrentIndex(4))

        # tabu search
        self.w3 = self.findChild(QPushButton, "w_4")
        self.w3.clicked.connect(lambda: self.st3.setCurrentIndex(0))

        # wykres początkowy
        self.w4 = self.findChild(QPushButton, "w_5")
        self.w4.clicked.connect(lambda: self.st3.setCurrentIndex(5))

        # słupki początkowe 1
        self.w5 = self.findChild(QPushButton, "w_6")
        self.w5.clicked.connect(lambda: self.st3.setCurrentIndex(6))

        # słupki początkowe 2
        self.w51 = self.findChild(QPushButton, "w_61")
        self.w51.clicked.connect(lambda: self.st3.setCurrentIndex(7))

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

        # Liczba pól
        self.nr_field = self.findChild(QSpinBox,"fieldnum")


        # Liczba lat/miesięcy
        self.nr_time = self.findChild(QSpinBox, "timenum")

        # Odświeżanie tabeli
        self.rt = self.findChild(QPushButton,"refreshtab")
        self.rt.clicked.connect(lambda: self.tab.setRowCount(int(self.nr_field.text())))

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
        self.ch1.toggled.connect(self.showDetails)

        # Typ nawozu
        self.nawoz = self.findChild(QComboBox, "nawoz")
        print(self.nawoz.currentText())

        # Koszt zbioru
        self.zbior = self.findChild(QDoubleSpinBox, "zbior")


        ## Ustawienia - butelkowanie, magazynowanie, transport

        # Pojemność magazynu
        self.magcap = self.findChild(QSpinBox, "capacity")

        # Koszt magazynowania
        self.magcost = self.findChild(QDoubleSpinBox, "magcost")

        # Ilość jednostek winogron na butelkę
        self.jperbot = self.findChild(QSpinBox, "jperbot")

        # Koszt transportu
        self.transcost = self.findChild(QDoubleSpinBox, "transcost")

        # Koszt butelki
        self.botcost = self.findChild(QDoubleSpinBox, "botcost")


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


    def showDetails(self):
        print("Selected: ", self.ch1.isChecked(),
              "  Name: ", self.ch1.text())


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
        self.epsilon = float(self.eps.text())
        self.max_iter = int(self.iter.text())

        print(self.epsilon, self.max_iter)


    def start_tabu(self):
        ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}

        # example data and visualisation
        num_of_years = 2
        types_of_grapes = len(ch_types)

        m = 600
        l = [800, 800, 800]  # Ograniczenia górne
        h = [100, 100, 100]  # Ograniczenia dolne

        sol = generate_solution(m, l, h, num_of_years, types_of_grapes)

        planting_cost = plant_price_generator(ch_types)

        IsFertilized = 1
        soil_quality = soil_quality_generator(3, num_of_years, ch_types)
        fertilizer_bonus = 0.05
        fertilizer_cost = 2
        harvest_cost = 3
        bottling_cost = 4
        plants_per_bottle = 1
        transport_cost = 3
        vineprice = vine_price_generator(ch_types, num_of_years)
        print(vineprice)

        self.c1.plot_vineprice(ch_types, num_of_years,vineprice)
        self.c1.setVisible(True)

        magazine_cost = 2
        magazine_capacity = 600
        store_needs = [100, 100, 100]

        # Tabu search wbudowany
        self.tabu_search(sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    self.tabu_length, self.max_iter, self.epsilon)

        self.pb.setValue(0)
        self.pb.setTextVisible(False)

        self.c.setVisible(True)


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

            if counter > max_iter:
                stop_iter = True

            if abs(past_sol - maxval) <= epsilon:
                stop_eps = True

            past_sol = maxval

            counter += 1
            print(counter)
            if counter >= max_iter:
                stop_iter = True

        self.pb.setValue(max_iter)
        print(limsta)

        # plt.plot(limsta)
        # plt.title('Wykres wartości funkcji celu')
        # plt.show()

        self.c.plotting(limsta)

        # sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

        self.c5.plot_main(gain_rem, loss_rem)
        self.c5.setVisible(True)

        self.c6.plot_bar(gain_rem, loss_rem)
        self.c6.setVisible(True)

        self.c7.plot_bar2(gain_rem, loss_rem, bs_solution.shape[0])
        self.c7.setVisible(True)

        return bs_solution

    def acctab(self):
        for row in range(self.tab.rowCount()):
            for column in range(self.tab.columnCount()):
                _item = self.tab.item(row, column)
                if _item:
                    item = self.tab.item(row, column).text()
                    print(f'row: {row}, column: {column}, item={item}')
                else:
                    item = None
                    print(f'row: {row}, column: {column}, item={item}')

app = QApplication([])
window = UI()
window.show()
app.exec()