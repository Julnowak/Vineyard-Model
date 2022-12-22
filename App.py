from main import *
from PyQt6.QtWidgets import *
from PyQt6 import uic
import pyqtgraph as pg

class UI(QMainWindow):

    def __init__(self):
        super().__init__()
        # loading the ui file with uic module
        self.clicked = None
        uic.loadUi("app.ui", self)
        self.epsilon = 0.1
        self.max_iter = 50

        self.ch1 = self.findChild(QCheckBox,"checkBox")
        self.ch1.toggled.connect(self.showDetails)

        # Odczyt typów wina
        ######
        self.v1 = self.findChild(QCheckBox, 'Barbera')
        self.v2 = self.findChild(QCheckBox, 'Chardonnay')
        self.v3 = self.findChild(QCheckBox, 'Nebbiolo')
        self.v4 = self.findChild(QCheckBox, 'Arneis')
        self.v5 = self.findChild(QCheckBox, 'Dolcetto')
        self.v6 = self.findChild(QCheckBox, 'Cortese')
        self.v7 = self.findChild(QCheckBox, 'Grignolino')
        self.v8 = self.findChild(QCheckBox, 'Erbaluce')
        ##########

        self.input = self.findChild(QDoubleSpinBox, "eps")
        self.input2 = self.findChild(QSpinBox, "iter")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.get)
        self.button.clicked.connect(self.grape_type_choice)

        self.button3 = self.findChild(QPushButton, "start")
        self.button3.clicked.connect(self.start_tabu)

        # Czyszczenie
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button2.clicked.connect(lambda: self.input.setValue(0.10))
        self.button2.clicked.connect(lambda: self.input2.setValue(50))


        self.st = self.findChild(QStackedWidget, "stackedWidget")
        
        # Zaczynamy od Menu
        self.st.setCurrentIndex(0)
        self.bset = self.findChild(QPushButton, "btn_set")
        self.bset.clicked.connect(self.go_to_set)

        self.b2 = self.findChild(QPushButton, "btn_page_1")
        self.b2.clicked.connect(self.go_to_menu)

        self.b3 = self.findChild(QPushButton, "btn_page_2")
        self.b3.clicked.connect(self.go_to_1)

        self.b4 = self.findChild(QPushButton, "btn_page_3")
        self.b4.clicked.connect(self.go_to_2)

        self.b4 = self.findChild(QPushButton, "btn_page4")
        self.b4.clicked.connect(self.go_to_3)

        self.b5 = self.findChild(QPushButton, "btn_info")
        self.b5.clicked.connect(self.go_to_info)

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

    # Wszystkie przyciski działają
    def go_to_set(self):
        self.st.setCurrentIndex(0)

    def go_to_menu(self):
        self.st.setCurrentIndex(1)

    def go_to_1(self):
        self.st.setCurrentIndex(2)

    def go_to_2(self):
        self.st.setCurrentIndex(3)

    def go_to_3(self):
        self.st.setCurrentIndex(4)

    def go_to_info(self):
        self.st.setCurrentIndex(5)

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

        tabu_search(sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    10, self.max_iter, self.epsilon)


app = QApplication([])
window = UI()
window.show()
app.exec()