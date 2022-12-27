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

        # loading the ui file with uic module
        self.clicked = None
        uic.loadUi("Projekt/app.ui", self)
        self.setWindowIcon(QtGui.QIcon("Projekt/2836932.png"))
        self.epsilon = 0.1
        self.max_iter = 50


        self.st = self.findChild(QStackedWidget, "stackedWidget")
        self.st2 = self.findChild(QStackedWidget, "stackedWidget_2")

        # Zaczynamy od Menu
        self.st.setCurrentIndex(1)
        self.st2.setCurrentIndex(1)

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


        self.input = self.findChild(QDoubleSpinBox, "eps")
        self.input2 = self.findChild(QSpinBox, "iter")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.get)
        self.button.clicked.connect(self.grape_type_choice)

        # Wykresior
        self.c = self.findChild(QWidget, 'widget')
        print(self.c)

        self.button3 = self.findChild(QPushButton, "start")
        self.button3.clicked.connect(self.start_tabu)

        # Czyszczenie
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button2.clicked.connect(lambda: self.input.setValue(0.10))
        self.button2.clicked.connect(lambda: self.input2.setValue(50))


        #Odczyt typów wina
        #####
        self.v1 = self.findChild(QCheckBox, 'Barbera')
        self.v2 = self.findChild(QCheckBox, 'Chardonnay')
        self.v3 = self.findChild(QCheckBox, 'Nebbiolo')
        self.v4 = self.findChild(QCheckBox, 'Arneis')
        self.v5 = self.findChild(QCheckBox, 'Dolcetto')
        self.v6 = self.findChild(QCheckBox, 'Cortese')
        self.v7 = self.findChild(QCheckBox, 'Grignolino')
        self.v8 = self.findChild(QCheckBox, 'Erbaluce')
        ##########

        self.ch1 = self.findChild(QCheckBox, "checkBox")
        self.ch1.toggled.connect(self.showDetails)

        # wykres
        self.gv = self.findChild(QGraphicsView, 'graphWidget')

        L = [1, 2, 3, 4, 5]
        G = [22,33,44,55,2]

        self.gv.addLegend()
        self.plot(L, G, "Sensor1", 'r')
        self.plot(G, L, "Sensor2", 'b')
        self.gv.setTitle("Your Title Here", color="k", size="20pt")

        styles = {'color': 'k', 'font-size': '16px'}
        self.gv.setLabel('left', 'Temperature (°C)', **styles)
        self.gv.setLabel('bottom', 'Hour (H)', **styles)

        self.gv.showGrid(x=True, y=True)


        self.pb = self.findChild(QProgressBar,"pb")
        self.pb.setTextVisible(False)

        # DO tabeli w ust
        self.tab = self.findChild(QTableWidget,"tableWidget")
        self.nr_field = self.findChild(QSpinBox,"fieldnum")
        self.rt = self.findChild(QPushButton,"refreshtab")

        self.rt.clicked.connect(lambda: self.refrtab())

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color, width=2)
        self.gv.plot(x, y, name=plotname, pen=pen, symbol='o', symbolSize=4, symbolBrush=(color))

        # self.button2.clicked.connect(self.input2.clear)

    def showDetails(self):
        print("Selected: ", self.ch1.isChecked(),
              "  Name: ", self.ch1.text())
        # self.sender() gives ref to widget that emitted signal

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
        self.epsilon = float(self.input.text())
        self.max_iter = int(self.input2.text())

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
                    10, self.max_iter, self.epsilon)
        self.pb.setValue(0)
        self.pb.setTextVisible(False)
        self.c.destroyer()

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

        sol_present_yourself(gain, loss, beg_sol, ch_types)

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

        plt.plot(limsta)
        plt.title('Wykres wartości funkcji celu')
        plt.show()

        sol_present_yourself(gain_rem, loss_rem, bs_solution, ch_types)

        return bs_solution

    def refrtab(self):
        print(int(self.nr_field.text()))
        self.tab.setRowCount(int(self.nr_field.text()))


app = QApplication([])
window = UI()
window.show()
app.exec()