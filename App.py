from Generators import *
from main import *
from PyQt6.QtWidgets import QApplication, QMainWindow,QCheckBox,QLineEdit,QPushButton,QProgressBar,QSpinBox,QDoubleSpinBox
from PyQt6 import uic


class UI(QMainWindow):
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    num_of_years = 2
    types_of_grapes = len(ch_types)
    num_of_fields = 3

    m = 600
    l = [800, 800, 800]  # Ograniczenia górne
    h = [100, 100, 100]  # Ograniczenia dolne

    sol = generate_solution(m, l, h, num_of_years, types_of_grapes)

    planting_cost = plant_price_generator(ch_types)
    epsilon = 0.01
    max_iter = 50
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

    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("app.ui", self)

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
        self.progress = self.findChild(QProgressBar, "progressBar")

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

        print(d)
        return d

    def get(self):
        epsilon = self.input.text()
        max_iter = self.input2.text()
        print(epsilon, max_iter)

    def show_progress(self):
        pass

    def start_tabu(self):
        tabu_search(self.sol, self.planting_cost,
                self.IsFertilized, self.soil_quality,
                self.fertilizer_bonus, self.fertilizer_cost,
                self.harvest_cost, self.bottling_cost,
                self.plants_per_bottle, self.transport_cost,self.ch_types,
                self.vineprice, self.magazine_cost, self.magazine_capacity, self.store_needs
                )

app = QApplication([])
window = UI()
window.show()
app.exec()