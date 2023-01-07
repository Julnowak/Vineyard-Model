import numpy as np
from PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QUrl
from Command_files import *
from Generators import *
from canvas import *
import pandas as pd
import xlsxwriter
import os
cur = os.path.abspath(os.getcwd())
import re

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
        self.text7 = self.findChild(QLabel, 'text_7')
        self.text8 = self.findChild(QLabel, 'text_8')
        self.text9 = self.findChild(QLabel, 'text_9')
        self.text10 = self.findChild(QLabel, 'text_10')
        self.text11 = self.findChild(QLabel, 'text_11')
        self.text12 = self.findChild(QLabel, 'text_12')

        self.mn = self.findChild(QPushButton, "mn")
        self.mn.clicked.connect(lambda: self.st4.setCurrentIndex(1))

        self.mn2 = self.findChild(QPushButton, "mn_2")
        self.mn2.clicked.connect(lambda: self.st4.setCurrentIndex(0))

        # self.mn3 = self.findChild(QPushButton, "mn_3")
        # self.mn3.clicked.connect(lambda: self.st4.setCurrentIndex(2))

        ## TABELE
        self.lik = self.findChild(QLabel, 'p_1')
        path = cur + r'\Wyniki\Tabele\ceny_wina.csv'
        url = bytearray(QUrl.fromLocalFile(path).toEncoded()).decode()
        self.lik.setText(f'<a href="{url}" style="color: white;">Ceny win</a>' )
        self.lik.setOpenExternalLinks(True)

        self.lik2 = self.findChild(QLabel, 'p_2')
        path2 = cur + r'\Wyniki\Tabele\ceny_sadzenia.csv'
        url2 = bytearray(QUrl.fromLocalFile(path2).toEncoded()).decode()
        self.lik2.setText(f'<a href="{url2}" style="color: white;">Koszty odsadzenia pól</a>')
        self.lik2.setOpenExternalLinks(True)

        self.lik3 = self.findChild(QLabel, 'p_3')
        path3 = cur + r'\Wyniki\Tabele\jakosc_gleby.xlsx'
        url3 = bytearray(QUrl.fromLocalFile(path3).toEncoded()).decode()
        self.lik3.setText(f'<a href="{url3}" style="color: white;">Jakość gleby</a>')
        self.lik3.setOpenExternalLinks(True)

        self.lik4 = self.findChild(QLabel, 'p_4')
        path4 = cur + r'\Wyniki\Tabele\rozwiazanie_pocz.xlsx'
        url4 = bytearray(QUrl.fromLocalFile(path4).toEncoded()).decode()
        self.lik4.setText(f'<a href="{url4}" style="color: white;">Rozwiązanie początkowe</a>')
        self.lik4.setOpenExternalLinks(True)

        self.lik7 = self.findChild(QLabel, 'p_7')
        path7 = cur + r'\Do_trybu_testowego\beg_sol.txt'
        url7 = bytearray(QUrl.fromLocalFile(path7).toEncoded()).decode()
        self.lik7.setText(f'<a href="{url7}" style="color: white;">Rozwiązanie początkowe</a>')
        self.lik7.setOpenExternalLinks(True)

        self.lik8 = self.findChild(QLabel, 'p_8')
        path8 = cur + r'\Do_trybu_testowego\vineprice.txt'
        url8 = bytearray(QUrl.fromLocalFile(path8).toEncoded()).decode()
        self.lik8.setText(f'<a href="{url8}" style="color: white;">Ceny wina</a>')
        self.lik8.setOpenExternalLinks(True)

        self.lik9 = self.findChild(QLabel, 'p_9')
        path9 = cur + r'\Do_trybu_testowego\soil_quality.txt'
        url9 = bytearray(QUrl.fromLocalFile(path9).toEncoded()).decode()
        self.lik9.setText(f'<a href="{url9}" style="color: white;">Jakość gleby</a>')
        self.lik9.setOpenExternalLinks(True)

        self.lik10 = self.findChild(QLabel, 'p_10')
        path10 = cur + r'\Do_trybu_testowego\planting_cost.txt'
        url10 = bytearray(QUrl.fromLocalFile(path10).toEncoded()).decode()
        self.lik10.setText(f'<a href="{url10}" style="color: white;">Koszt obsadzenia</a>')
        self.lik10.setOpenExternalLinks(True)

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
        self.rt.clicked.connect(lambda: self.refresh_fieldnum())

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
            lambda: self.refresh_storeneed_tab())

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

        # TL średnio i długo - wartości
        self.tl_med = self.findChild(QSpinBox, "TL_2")
        self.tabu_med_thresh = int(self.tl_med.text())

        self.tl_long = self.findChild(QSpinBox, "TL_3")
        self.tabu_long_num = int(self.tl_long.text())

        # Typy TL
        self.smol = self.findChild(QCheckBox, "smol")
        self.tabulist = self.smol.isChecked()

        self.med = self.findChild(QCheckBox, "med")
        self.MidTermMem = self.med.isChecked()

        self.lon = self.findChild(QCheckBox, "lon")
        self.LongTermMem = self.lon.isChecked()

        # Typy sąsiedztwa
        self.sasiad = self.findChild(QRadioButton, "sasiedztwo")
        self.sasiad2 = self.findChild(QRadioButton, "sasiedztwo_2")
        self.rand = self.sasiad2.isChecked()

        self.staly = self.findChild(QSpinBox, "staly")
        self.constval = int(self.staly.text())

        self.minlos = self.findChild(QSpinBox, "minlos")
        self.minrand = int(self.minlos.text())

        self.maxlos = self.findChild(QSpinBox, "maxlos")
        self.maxrand = int(self.maxlos.text())

        # część sąsiedztwa
        self.som = self.findChild(QDoubleSpinBox, "som")
        self.SolutionSpaceCoverage = float(self.som.text())

        # Typy rozwiązania początkowego
        self.typ = self.findChild(QRadioButton, "typ")
        self.typ2 = self.findChild(QRadioButton, "typ_2")
        self.typ3 = self.findChild(QRadioButton, "typ_3")
        self.typ4 = self.findChild(QRadioButton, "typ_4")

        self.ch_typ_list = [self.typ.isChecked(),self.typ2.isChecked(),
                            self.typ3.isChecked(),self.typ4.isChecked()]

        # Kryterium aspiracji - tak/nie
        self.aspik= self.findChild(QCheckBox, "aspi")
        self.aspicheck = self.aspik.isChecked()

        # Długość do kryterium aspiracji
        self.aspinum = self.findChild(QSpinBox, "aspi_2")
        self.aspithresh = int(self.aspinum.text())

        ## Ustawienia przyciski

        # zatwierdź
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.get)

        # Czyszczenie
        self.button2 = self.findChild(QPushButton, "pushButton_2")

        # TODO: Dopisać wartości podstawowe dla reszty przycisków
        self.button2.clicked.connect(lambda: self.input.setValue(0.10))
        self.button2.clicked.connect(lambda: self.input2.setValue(50))

        ### DO STATYSTYK
        # Kryteria stopu
        self.stop_iter = False
        self.stop_eps = False

        # Wyświetlanie
        self.stat = self.findChild(QLabel, "stat")
        self.stat2 = self.findChild(QLabel, "stat_2")
        self.stat3 = self.findChild(QLabel, "stat_3")
        self.stat4 = self.findChild(QLabel, "stat_4")
        self.stat5 = self.findChild(QLabel, "stat_5")
        self.stat6 = self.findChild(QLabel, "stat_6")
        self.stat7 = self.findChild(QLabel, "stat_7")
        self.stat8 = self.findChild(QLabel, "stat_8")
        self.stat9 = self.findChild(QLabel, "stat_9")
        self.stat10 = self.findChild(QLabel, "stat_10")
        self.stat11 = self.findChild(QLabel, "stat_11")
        self.stat12 = self.findChild(QLabel, "stat_12")
        self.stat122 = self.findChild(QLabel, "stat_122")
        self.stat13 = self.findChild(QLabel, "stat_13")
        self.stat132 = self.findChild(QLabel, "stat_132")
        self.stat14 = self.findChild(QLabel, "stat_14")
        self.stat142 = self.findChild(QLabel, "stat_142")
        self.stat15 = self.findChild(QLabel, "stat_15")
        self.stat152 = self.findChild(QLabel, "stat_152")

        self.stat16 = self.findChild(QLabel, "stat_16") # średnioterm w porównaniach

        self.stat17 = self.findChild(QLabel, "stat_17")
        self.stat18 = self.findChild(QLabel, "stat_18")
        self.stat19 = self.findChild(QLabel, "stat_19")



        ### WARNINGI
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

        ### TRYB TESTOWY - WAŻNE
        self.tryb = self.findChild(QRadioButton, 'tryb')
        self.tryb2 = self.findChild(QRadioButton, 'tryb_2')
        self.repeat_test = self.findChild(QSpinBox, 'repeat_test')
        self.test_icon = self.findChild(QLabel, 'test_icon')
        self.test_icon2 = self.findChild(QLabel, 'test_icon_2')
        self.test_icon3 = self.findChild(QLabel, 'test_icon_3')
        self.lineedit = self.findChild(QLineEdit, 'lineEdit')
        self.lineedit.setText('Sheet1')
        self.excelnum=2

        self.oldFiles = self.findChild(QRadioButton, 'oldfiles')
        self.genFldFiles = self.findChild(QRadioButton, 'oldfiles_3')
        self.readFromFile = self.findChild(QRadioButton, 'oldfiles_2')

        self.read_from_line = self.findChild(QLineEdit, 'lineEdit2')

        ### PARAMSY
        self.upper = [800, 800, 800]
        self.lower = [100, 100, 100]
        self.helpik = self.findChild(QLabel, 'helpik')
        self.helpik.setVisible(False)
        self.show_yourself()
        self.set()

        self.writer33 = pd.ExcelWriter('Wyniki/porównanie_zbiorcze.xlsx')

        self.zapisz = self.findChild(QPushButton, 'zapisz_pliki')
        self.zapisz.clicked.connect(lambda: (self.writer33.close(),self.zapisz.setVisible(False)))

    def refresh_storeneed_tab(self):
        self.grape_type_choice()
        self.zap.setRowCount(len(self.ch_types) + 1)
        self.zap.setVerticalHeaderLabels(list(self.ch_types.values()) + [''])

    def refresh_fieldnum(self):
        self.fields = int(self.nr_field.text())
        self.tab.setRowCount(self.fields)

    def set(self):
        self.text.setText(str(self.num_of_years))
        self.text2.setText(str(self.fields))
        self.text3.setText(str(self.max_iter))
        self.text4.setText(str(self.epsilon))
        self.text5.setText(str(self.tabu_length))
        self.text6.setText(str(self.magazine_capacity))
        self.text7.setText(str(self.aspicheck))
        self.text8.setText(str(self.aspithresh))
        self.text9.setText(str(self.SolutionSpaceCoverage))
        self.fields = int(self.nr_field.text())

        if self.rand:
            self.text10.setText(f'Losowy\n{self.minrand}-{self.maxrand}')
        else:
            self.text10.setText(f'Stały\n{self.constval}')

        if self.rand:
            self.text10.setText(f'Losowy\n{self.minrand}-{self.maxrand}')
        else:
            self.text10.setText(f'Stały\n{self.constval}')

        if self.ch_typ_list[0]:
            txt = 'I typ'
        elif self.ch_typ_list[1]:
            txt = 'II typ'
        elif self.ch_typ_list[2]:
            txt = 'III typ'
        else:
            txt = 'IV typ'

        self.text11.setText(txt)
        self.text12.setText(str(len(self.ch_types)))
        self.repeats = int(self.repeat_test.text())
        self.tabu_med_thresh = int(self.tl_med.text())
        self.tabu_long_num = int(self.tl_long.text())

        if self.tryb.isChecked():
            self.tryb_programu = 'symulacja'
            self.test_icon.setVisible(False)
            self.takak.setVisible(False)
        else:
            try:
                self.tryb_programu = 'testowanie'
                self.test_icon.setVisible(True)
                self.takak.setVisible(True)
                if self.genFldFiles.isChecked():
                    if self.ch_typ_list[0]:
                        sol_flag = 1
                    elif self.ch_typ_list[1]:
                        sol_flag = 2
                    elif self.ch_typ_list[2]:
                        sol_flag = 3
                    else:
                        sol_flag = 4


                    # Fragment, gdyby pliki nie istniały - NIE USUWAĆ
                    sol = generate_solution(self.magazine_capacity, self.upper, self.lower, self.num_of_years,
                                            len(self.ch_types), self.store_need, sol_flag,self.fields)

                    with open('Do_trybu_testowego/beg_sol.txt', 'w') as my_file:
                        c = 0
                        for i in sol:
                            if c%12 in [2,6,10]:
                                np.savetxt(my_file, i,fmt='%.d',header=f'Miesiac {c+1} - tu sadzimy',footer='\n',comments='')
                            else:
                                np.savetxt(my_file, i, fmt='%.d', header=f'Miesiac {c + 1}',footer='\n',comments='')
                            c+=1

                    planting_cost = plant_price_generator(self.ch_types)
                    with open('Do_trybu_testowego/planting_cost.txt', 'w') as my_file:
                        planting_cost = planting_cost.reshape((1,len(planting_cost)))
                        for i in planting_cost:
                            np.savetxt(my_file, i, fmt='%.2f',header='Rodzaje - '+', '.join(list(self.ch_types.values())),comments='')

                    soil_quality = soil_quality_generator(self.fields, self.num_of_years, self.ch_types, self.trojka)
                    with open('Do_trybu_testowego/soil_quality.txt', 'w') as my_file:
                        c = 0
                        for i in soil_quality:
                            if c % 12 in [2, 6, 10]:
                                np.savetxt(my_file, i, fmt='%.2f', header=f'Miesiac {c + 1} - tu sadzimy',footer='\n',comments='')
                            else:
                                np.savetxt(my_file, i, fmt='%.2f', header=f'Miesiac {c + 1}',footer='\n',comments='')
                            c += 1

                    vineprice = vine_price_generator(self.ch_types, self.num_of_years)

                    with open('Do_trybu_testowego/vineprice.txt', 'w') as my_file:
                        c=0
                        for i in vineprice:
                            np.savetxt(my_file, i,fmt='%.2f', header=f'{list(self.ch_types.values())[c]}',footer='\n',comments='')
                            c+=1

            except:
                print('TESTOWANIE')


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
            self.fields = int(self.nr_field.text())
            self.tab.setRowCount(self.fields)
            self.zap.setRowCount(len(self.ch_types) + 1)
            self.zap.setVerticalHeaderLabels(list(self.ch_types.values()) + [''])
            self.tabu_length = int(self.tl.text())


            self.tabulist = self.smol.isChecked()
            self.MidTermMem = self.med.isChecked()
            self.LongTermMem = self.lon.isChecked()

            self.SolutionSpaceCoverage = float(self.som.text())
            self.aspicheck = self.aspik.isChecked()
            self.aspithresh = int(self.aspinum.text())
            self.ch_typ_list = [self.typ.isChecked(), self.typ2.isChecked(),
                                self.typ3.isChecked(), self.typ4.isChecked()]

            if self.nawoz.currentText() == 'Standardowy (+5%) - 2zł/szt':
                self.fertilizer_bonus = 0.05
                self.fertilizer_cost = 2.00
            elif self.nawoz.currentText() == 'Wyższej jakości (+10%) - 4zł/szt':
                self.fertilizer_bonus = 0.10
                self.fertilizer_cost = 4.00
            else:
                self.fertilizer_bonus = 0.17
                self.fertilizer_cost = 7.00

            self.rand = self.sasiad2.isChecked()
            if self.rand is True:
                self.minrand = int(self.minlos.text())
                self.maxrand = int(self.maxlos.text())
            else:
                self.constval = int(self.staly.text())

        self.set()
        self.helpik.setVisible(False)


    def start_tabu(self):
        self.get()
        self.set()
        try:
            print('k')
            self.warn2.setVisible(False)
            self.show_yourself()

            if self.tryb_programu == 'symulacja':
                self.helpik.setVisible(False)

                if self.ch_typ_list[0]:
                    sol_flag = 1
                elif self.ch_typ_list[1]:
                    sol_flag = 2
                elif self.ch_typ_list[2]:
                    sol_flag = 3
                else:
                    sol_flag = 4

                sol = generate_solution(self.magazine_capacity, self.upper, self.lower, self.num_of_years,
                                        len(self.ch_types), self.store_need, sol_flag)

                writer = pd.ExcelWriter('Wyniki/Tabele/rozwiazanie_pocz.xlsx', engine='xlsxwriter')
                for i in range(self.num_of_years * 12):
                    df0 = pd.DataFrame(data=sol[i, :, :].astype(int))
                    df0.insert(loc=0, column='Pole', value=list(range(1, self.fields+1)))
                    df0.to_excel(writer, sheet_name=f'Miesiac {i + 1}',
                                 header=['Pole'] + list(self.ch_types.values()), index=False)
                writer.close()


                planting_cost = plant_price_generator(self.ch_types)
                df1 = pd.DataFrame(data={'Typ':list(self.ch_types.values()), 'Cena': planting_cost.astype(float)})
                df1.to_csv('Wyniki/Tabele/ceny_sadzenia.csv', sep=',', header=None, float_format='%.2f', index=False)

                soil_quality = soil_quality_generator(self.fields, self.num_of_years, self.ch_types, self.trojka)
                writer = pd.ExcelWriter('Wyniki/Tabele/jakosc_gleby.xlsx', engine='xlsxwriter')
                for i in range(self.num_of_years * 12):
                    df2 = pd.DataFrame(data=soil_quality[i, :, :].astype(float))
                    df2.insert(loc=0, column='Pole', value=list(range(1, self.fields+1)))
                    df2.to_excel(writer, sheet_name=f'Miesiac {i + 1}',
                                 header=['Pole'] + list(self.ch_types.values()), index=False)
                writer.close()

                vineprice = vine_price_generator(self.ch_types, self.num_of_years)
                df3 = pd.DataFrame(data=vineprice.astype(float),columns=list('m'+str(i) for i in range(1,self.num_of_years*12+1)))
                df3.insert(loc=0,column='Typ',value=list(self.ch_types.values()))
                df3.to_csv('Wyniki/Tabele/ceny_wina.csv', sep=',', index=False)

                self.c1.plot_vineprice(self.ch_types, self.num_of_years, vineprice)
                self.c1.setVisible(True)


                # Tabu search wbudowany
                self.tabu_search(sol, planting_cost,
                                 self.IsFertilized, soil_quality,
                                 self.fertilizer_bonus, self.fertilizer_cost,
                                 self.harvest_cost, self.bottling_cost,
                                 self.plants_per_bottle, self.transport_cost,
                                 vineprice, self.magazine_cost, self.magazine_capacity, self.store_need, self.ch_types,
                                 self.tabu_length, self.max_iter, self.epsilon,self.upper, self.lower)
                self.pb.setValue(0)
                self.pb.setTextVisible(False)

            elif self.tryb_programu == 'testowanie':
                self.helpik.setVisible(True)

                if self.oldFiles.isChecked():

                    with open('Do_trybu_testowego/beg_sol.txt', 'r') as f:
                        l = [[int(num) for num in line.split(' ')] for line in f if (line != '\n' and not re.match('Miesiac',line))]
                        sol = np.zeros((self.num_of_years*12,self.fields,len(self.ch_types)))
                        l = np.array(np.array(l))
                        a = 0
                        b= self.fields
                        for i in range(self.num_of_years*12):
                            sol[i,:,:] = l[a:b,:]
                            a+=self.fields
                            b += self.fields

                    print(sol)

                    with open('Do_trybu_testowego/planting_cost.txt', 'r') as f:
                        l = [[float(num[:len(num) - 1]) for num in line.split(' ')] for line in f if
                             (line != '\n' and not re.match('Rodzaj', line))]

                        planting_cost = [i[0] for i in l]

                    print(planting_cost)
                    with open('Do_trybu_testowego/soil_quality.txt', 'r') as f:
                        l = [[float(num) for num in line.split(' ')] for line in f if
                             (line != '\n' and not re.match('Miesiac', line))]
                        soil_quality = np.zeros((self.num_of_years*12,self.fields,len(self.ch_types)))
                        l = np.array(np.array(l))
                        a = 0
                        b = self.fields
                        for i in range(self.num_of_years*12):
                            soil_quality[i, :, :] = l[a:b, :]
                            a += self.fields
                            b += self.fields

                    print(soil_quality)

                    with open('Do_trybu_testowego/vineprice.txt', 'r') as f:
                        l = [[float(num[:len(num) - 1]) for num in line.split(' ')] for line in f if
                             (line != '\n' and not line in list( i+'\n' for i in list(self.ch_types.values())))]
                        vineprice = np.zeros((len(self.ch_types),self.num_of_years*12))
                        l = np.array(np.array(l))

                        c = 0
                        for i in range(len(self.ch_types)):
                            for x in range(self.num_of_years*12):
                                vineprice[i][x] = l[c]
                                c += 1
                    print(vineprice)
                elif self.readFromFile.isChecked():
                    pass

                if self.repeats != 1:
                    count_iter_stops = 0
                    count_eps_stops = 0
                    besties = []
                    actualies = []
                    aspiracje = 0
                    for x in range(self.repeats):
                        # Na razie dla najlepszego
                        try:
                            best, actual, stop_type, aspiracje = self.testowy_tabu_search(sol, planting_cost,
                                             self.IsFertilized, soil_quality,
                                             self.fertilizer_bonus, self.fertilizer_cost,
                                             self.harvest_cost, self.bottling_cost,
                                             self.plants_per_bottle, self.transport_cost,
                                             vineprice, self.magazine_cost, self.magazine_capacity, self.store_need, self.ch_types,
                                             self.tabu_length, self.max_iter, self.epsilon, self.upper, self.lower)

                            besties.append(best)
                            actualies.append(actual)
                            if stop_type:
                                count_iter_stops+= 1
                            else:
                                count_eps_stops+=1
                        except:
                            best, actual, stop_type, aspiracje = self.testowy_tabu_search(sol, planting_cost,
                                                                                          self.IsFertilized,
                                                                                          soil_quality,
                                                                                          self.fertilizer_bonus,
                                                                                          self.fertilizer_cost,
                                                                                          self.harvest_cost,
                                                                                          self.bottling_cost,
                                                                                          self.plants_per_bottle,
                                                                                          self.transport_cost,
                                                                                          vineprice, self.magazine_cost,
                                                                                          self.magazine_capacity,
                                                                                          self.store_need,
                                                                                          self.ch_types,
                                                                                          self.tabu_length,
                                                                                          self.max_iter, self.epsilon,
                                                                                          self.upper, self.lower)

                            besties.append(best)
                            actualies.append(actual)
                            if stop_type:
                                count_iter_stops += 1
                            else:
                                count_eps_stops += 1
                        self.helpik.setText(f'x{x+1}')

                    df = pd.DataFrame(list(zip(besties, actualies)),
                                      columns=['Najlepsze', 'Aktualne'])

                    text = str(self.lineedit.text())
                    print('--------------------tuuuu')
                    print(str(self.lineedit.text()))

                    if text == 'Sheet1':
                        text = 'Sheet1'
                    elif text == f'Sheet{self.excelnum}':
                        text = f'Sheet{self.excelnum}'
                        self.excelnum += 1
                    self.lineedit.setText(f'Sheet{self.excelnum}')

                    # NAPRAW

                    df.to_excel(self.writer33, sheet_name=f'{text}')


                    # print('najlepsze\n')
                    # print(besties)
                    # print()
                    # print('actualne\n')
                    # print(actualies)
                    self.pb.setValue(0)
                    self.pb.setTextVisible(False)
                    self.stat11.setText(str(self.repeats))

                    self.stat12.setText(str(max(besties)))
                    self.stat13.setText(str(min(besties)))
                    self.stat14.setText(str(sum(besties)/len(besties)))
                    self.stat15.setText(str(np.std(besties)))

                    self.stat122.setText(str(max(actualies)))
                    self.stat132.setText(str(min(actualies)))
                    self.stat142.setText(str(sum(actualies)/len(actualies)))
                    self.stat152.setText(str(np.std(actualies)))

                    self.stat17.setText(str(count_iter_stops))
                    self.stat18.setText(str(count_eps_stops))
                    self.stat19.setText(str(aspiracje))
                else:
                    self.c1.plot_vineprice(self.ch_types, self.num_of_years, vineprice)
                    self.c1.setVisible(True)

                    # Tabu search wbudowany
                    self.tabu_search(sol, planting_cost,
                                     self.IsFertilized, soil_quality,
                                     self.fertilizer_bonus, self.fertilizer_cost,
                                     self.harvest_cost, self.bottling_cost,
                                     self.plants_per_bottle, self.transport_cost,
                                     vineprice, self.magazine_cost, self.magazine_capacity, self.store_need,
                                     self.ch_types,
                                     self.tabu_length, self.max_iter, self.epsilon, self.upper, self.lower)
                    self.pb.setValue(0)
                    self.helpik.setText(f'x{1}')
                    self.pb.setTextVisible(False)

        except:
            print('Coś poszło nie tak!')
            self.warn2.setVisible(True)
            self.warn2.setText(u"\u26A0" + ' Coś poszło nie tak! Sprawdź ustawienia.')

    def tabu_search(self, beg_sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    tabu_length=10, max_iter=50, epsilon=0.1,upper=[800,800,800],lower=[100,100,100]):

        #dane do gui

        licz_asp=0
        licz_mid=0

        gain, loss = ocena(beg_sol, planting_cost,
                           IsFertilized, soil_quality,
                           fertilizer_bonus, fertilizer_cost,
                           harvest_cost, bottling_cost,
                           plants_per_bottle, transport_cost,
                           vineprice, magazine_cost, magazine_capacity, store_needs, upper,lower )

        beg = round(sum(gain) - sum(loss),2)
        self.stat.setText(str(beg))

        self.c2.plot_main(gain, loss,'beginning_main_linear_plot')
        self.c2.setVisible(True)

        self.c3.plot_bar(gain, loss,'beginning_bar_plot')
        self.c3.setVisible(True)

        self.c4.plot_bar2(gain, loss, beg_sol.shape[0],'beginning_detailed_bar_plot')
        self.c4.setVisible(True)

        self.t.setVisible(True)

        TL = []
        avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[2]))  # pamiec srednioteminowa zlicza rozwiazania dane

        streak = 0 # Do kryterium aspiracji

        aspiMinstreak=5
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

        self.stop_iter = False
        self.stop_eps = False
        counter = 0

        self.pb.setTextVisible(True)
        self.pb.setMaximum(max_iter)
        aspiStreak = 0
        minieps = np.inf
        # DANE
        dane = [[counter, round(sum(gain), 2), round(sum(loss), 2), round(sum(gain) - sum(loss), 2), len(TL),
                 wypisz(beg_sol, ch_types)]]

        limsta = []
        sollist=[]
        # print(solution)
        print('----------------------------------------------------')
        while not (self.stop_iter or self.stop_eps):
            if counter == 0:
                past_sol = 0

            self.pb.setValue(counter)
            mapa = generateAllsolutions(solution,upper,self.SolutionSpaceCoverage,self.rand,self.minrand,self.maxrand,self.constval)
            neigh = [k for k, _ in mapa.items()]

            n_rem = None
            maxi = -np.inf
            maxval = -np.inf
            
            for n in neigh:
                if n in TL:
                    continue
                gain, loss = ocena(mapa[n], planting_cost,
                                   IsFertilized, soil_quality,
                                   fertilizer_bonus, fertilizer_cost,
                                   harvest_cost, bottling_cost,
                                   plants_per_bottle, transport_cost,
                                   vineprice, magazine_cost, magazine_capacity, store_needs, upper,lower )


                value = sum(gain) - sum(loss)
                if (n not in TL and value - avgMemory[n] * self.tabu_long_num> maxi):
                    maxi = value - avgMemory[n] * self.tabu_long_num  # no jak było wybierane to mniej
                    maxval = value
                    gain_rem = gain
                    loss_rem = loss
                    n_rem = n

            if self.aspicheck and aspiStreak>=aspiMinstreak :
                ASPmapa=generateAllsolutionsFromAspi(solution, upper, TL, self.rand, self.minrand, self.maxrand,
                                     self.constval)
                ASPneigh = [k for k, _ in ASPmapa.items()]

                ASPn_rem = None
                ASPmaxi = -np.inf
                ASPmaxval = -np.inf
                for ASPn in ASPneigh:
                    ASPgain, ASPloss = ocena(ASPmapa[ASPn], planting_cost,
                                       IsFertilized, soil_quality,
                                       fertilizer_bonus, fertilizer_cost,
                                       harvest_cost, bottling_cost,
                                       plants_per_bottle, transport_cost,
                                       vineprice, magazine_cost, magazine_capacity, store_needs, upper, lower)

                    ASPvalue = sum(ASPgain) - sum(ASPloss)
                    if  value - avgMemory[n] * self.tabu_long_num > maxi:
                        ASPmaxi = ASPvalue - avgMemory[n] * self.tabu_long_num  # no jak było wybierane to mniej
                        ASPmaxval = ASPvalue
                        ASPgain_rem = ASPgain
                        ASPloss_rem = ASPloss
                        ASPn_rem = ASPn

                if ASPmaxi-maxi>self.aspithresh:
                    maxi = ASPmaxi
                    mapa=ASPmapa
                    maxval = ASPmaxval
                    gain_rem = ASPgain_rem
                    loss_rem = ASPloss_rem
                    n_rem = ASPn_rem
                    licz_asp = licz_asp + 1  # to nam mówi ile razy wybraliśmy rozwiązanie z tabu lsity z kryterium aspiracji
                    aspiStreak = 0
                    TL = TL[len(TL)//2:]
                    # print("uzyto apiracji ", counter)


            if maxval <= past_sol and self.MidTermMem:#jak mamy midterm zliczamy spadki
                streak += 1
            if maxval <= past_sol and self.aspicheck:  # jak mamy midterm zliczamy spadki
                aspiStreak += 1
                # print(maxval-past_sol)

            # print(TL)
            if streak >= self.tabu_med_thresh:#jak spadki duże robimy reset
                randnum=random.randint(len(sollist)//3, len(sollist)- len(sollist)//3)
                buff=sollist[randnum]
                solbuff=buff[0]
                TL=TL[0:len(TL)//2]
                avgMemory=avgMemory//2
                licz_mid += 1
                limsta.append(buff[1])
                streak = 0

                maxval=buff[1]
                print("uzyto medium ", counter)
            else:
                solbuff=mapa[n_rem].copy()

                limsta.append(maxval)

                if self.LongTermMem:
                    avgMemory[n_rem] = avgMemory[n_rem] + 1
                if maxval >= bs:
                    streak=0
                    aspiStreak = 0

                    bs_solution = mapa[n_rem].copy()
                    bs_gain_rem = gain_rem
                    bs_loss_rem = loss_rem
                    bs = maxval
                    bs_counter_rem = counter + 1
                if (self.tabulist):
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
            # Obecne rozwiązanie
            solution = solbuff
            sollist.append((solbuff.copy(),maxval))

            if abs(past_sol - maxval) <= epsilon:
                self.stop_eps = True

            counter += 1

            if abs(past_sol - maxval) <= minieps:
                minieps = round(abs(past_sol - maxval), len(str(self.epsilon)))
                self.stat6.setText(str(minieps)+'/ it: '+str(counter))

            dane.append(
                [counter, round(sum(gain_rem), 2), round(sum(loss_rem), 2), round(sum(gain_rem) - sum(loss_rem), 2),
                 len(TL), wypisz(solution, ch_types)])

            print(counter)
            if counter >= max_iter:
                self.stop_iter = True

            past_sol = maxval

        if self.stop_eps and self.stop_iter:
            self.stat9.setText('Kryterium dokładności i maksymalnej liczby iteracji')
        elif self.stop_eps:
            self.stat9.setText('Kryterium dokładności')
        elif self.stop_iter:
            self.stat9.setText('Kryterium maksymalnej liczby iteracji')
        else:
            print("WARNING!")

        # print(avgMemory)
        self.stat5.setText(str(counter)+'/'+str(max_iter))

        ac = limsta[0]
        better_counter = 0
        worse_counter = 0

        for i in limsta[1:]:
            if i < ac:
                worse_counter +=1
            elif i > ac:
                better_counter += 1
            ac = i

        self.stat7.setText(str(better_counter))
        self.stat8.setText(str(worse_counter))

        self.pb.setValue(max_iter)

        self.c.plotting(limsta)
        self.c.setVisible(True)

        self.stat3.setText(str(round(limsta[-1],2)) + f'/ it: {counter}')
        self.stat2.setText(str(round(sum(bs_gain_rem)-sum(bs_loss_rem),2)) + f'/ it: {bs_counter_rem}')
        self.stat10.setText(wypisz(bs_solution,self.ch_types))

        self.stat4.setText(str(licz_asp))
        self.stat16.setText(str(licz_mid))

        self.c5.plot_main(bs_gain_rem, bs_loss_rem,'ending_main_linear_plot')
        self.c5.setVisible(True)

        self.c6.plot_bar(bs_gain_rem, bs_loss_rem,'ending_bar_plot')
        self.c6.setVisible(True)

        self.c7.plot_bar2(bs_gain_rem, bs_loss_rem, bs_solution.shape[0],'ending_detailed_bar_plot')
        self.c7.setVisible(True)

        self.t.setRowCount(len(dane))
        self.t.setColumnCount(len(dane[0]))
        self.t.setHorizontalHeaderLabels(["Iteracja", "zysk", "strata", "bilans", "Aktualna długość TL", "Opis"])

        for k in range(len(dane)):
            for i in range(len(dane[0])):
                self.t.setItem(k, i, QTableWidgetItem(str(dane[k][i])))
        self.t.resizeColumnsToContents()
        self.t.resizeRowsToContents()

        return bs_solution

    # Okrojona wersja do testów (Bez wizualizacji, inne przeliczniki)
    def testowy_tabu_search(self, beg_sol, planting_cost,
                    IsFertilized, soil_quality,
                    fertilizer_bonus, fertilizer_cost,
                    harvest_cost, bottling_cost,
                    plants_per_bottle, transport_cost,
                    vineprice, magazine_cost, magazine_capacity, store_needs, ch_types,
                    tabu_length=10, max_iter=50, epsilon=0.1, upper=[800, 800, 800], lower=[100, 100, 100]):


        stop_type = True # To wtedy iteracje
        # flagi

        licz_asp = 0
        licz_mid = 0

        gain, loss = ocena(beg_sol, planting_cost,
                           IsFertilized, soil_quality,
                           fertilizer_bonus, fertilizer_cost,
                           harvest_cost, bottling_cost,
                           plants_per_bottle, transport_cost,
                           vineprice, magazine_cost, magazine_capacity, store_needs, upper, lower)

        TL = []
        avgMemory = np.zeros((2 * beg_sol.shape[0] * beg_sol.shape[1] * beg_sol.shape[
            2]))  # pamiec srednioteminowa zlicza rozwiazania dane

        streak = 0  # Do kryterium aspiracji

        aspiMinstreak = 5
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

        self.stop_iter = False
        self.stop_eps = False
        counter = 0

        self.pb.setTextVisible(True)
        self.pb.setMaximum(max_iter)
        aspiStreak = 0
        minieps = np.inf
        # DANE
        dane = [[counter, round(sum(gain), 2), round(sum(loss), 2), round(sum(gain) - sum(loss), 2), len(TL),
                 wypisz(beg_sol, ch_types)]]

        limsta = []
        sollist = []
        # print(solution)
        print('----------------------------------------------------')
        while not (self.stop_iter or self.stop_eps):
            if counter == 0:
                past_sol = 0

            self.pb.setValue(counter)
            mapa = generateAllsolutions(solution, upper, self.SolutionSpaceCoverage, self.rand, self.minrand,
                                        self.maxrand, self.constval)
            neigh = [k for k, _ in mapa.items()]

            n_rem = None
            maxi = -np.inf
            maxval = -np.inf

            for n in neigh:
                if n in TL:
                    continue
                gain, loss = ocena(mapa[n], planting_cost,
                                   IsFertilized, soil_quality,
                                   fertilizer_bonus, fertilizer_cost,
                                   harvest_cost, bottling_cost,
                                   plants_per_bottle, transport_cost,
                                   vineprice, magazine_cost, magazine_capacity, store_needs, upper, lower)

                value = sum(gain) - sum(loss)
                if (n not in TL and value - avgMemory[n] * self.tabu_long_num > maxi):
                    maxi = value - avgMemory[n] * self.tabu_long_num  # no jak było wybierane to mniej
                    maxval = value
                    gain_rem = gain
                    loss_rem = loss
                    n_rem = n

            if self.aspicheck and aspiStreak >= aspiMinstreak:
                ASPmapa = generateAllsolutionsFromAspi(solution, upper, TL, self.rand, self.minrand, self.maxrand,
                                                       self.constval)
                ASPneigh = [k for k, _ in ASPmapa.items()]

                ASPn_rem = None
                ASPmaxi = -np.inf
                ASPmaxval = -np.inf
                for ASPn in ASPneigh:
                    ASPgain, ASPloss = ocena(ASPmapa[ASPn], planting_cost,
                                             IsFertilized, soil_quality,
                                             fertilizer_bonus, fertilizer_cost,
                                             harvest_cost, bottling_cost,
                                             plants_per_bottle, transport_cost,
                                             vineprice, magazine_cost, magazine_capacity, store_needs, upper, lower)

                    ASPvalue = sum(ASPgain) - sum(ASPloss)
                    if value - avgMemory[n] * self.tabu_long_num > maxi:
                        ASPmaxi = ASPvalue - avgMemory[n] * self.tabu_long_num  # no jak było wybierane to mniej
                        ASPmaxval = ASPvalue
                        ASPgain_rem = ASPgain
                        ASPloss_rem = ASPloss
                        ASPn_rem = ASPn

                if ASPmaxi - maxi > self.aspithresh:
                    maxi = ASPmaxi
                    mapa = ASPmapa
                    maxval = ASPmaxval
                    gain_rem = ASPgain_rem
                    loss_rem = ASPloss_rem
                    n_rem = ASPn_rem
                    licz_asp = licz_asp + 1  # to nam mówi ile razy wybraliśmy rozwiązanie z tabu lsity z kryterium aspiracji
                    aspiStreak = 0
                    TL = TL[len(TL) // 2:]
                    # print("uzyto apiracji ", counter)

            if maxval <= past_sol and self.MidTermMem:  # jak mamy midterm zliczamy spadki
                streak += 1
            if maxval <= past_sol and self.aspicheck:  # jak mamy midterm zliczamy spadki
                aspiStreak += 1
                # print(maxval-past_sol)

            # print(TL)
            if streak >= self.tabu_med_thresh:  # jak spadki duże robimy reset
                randnum = random.randint(0, len(sollist) // 2)
                buff = sollist[randnum]
                solbuff = buff[0]
                TL = TL[0:len(TL) // 2]
                avgMemory = avgMemory // 2
                licz_mid+=1
                limsta.append(buff[1])
                streak = 0
                self.stat16.setText(str(licz_mid))
                maxval = buff[1]
                # print("uzyto medium ", counter)
            else:
                solbuff = mapa[n_rem].copy()

                limsta.append(maxval)

                if self.LongTermMem:
                    avgMemory[n_rem] = avgMemory[n_rem] + 1
                if maxval >= bs:
                    streak = 0
                    aspiStreak = 0

                    bs_solution = mapa[n_rem].copy()
                    bs_gain_rem = gain_rem
                    bs_loss_rem = loss_rem
                    bs = maxval
                    bs_counter_rem = counter + 1
                if (self.tabulist):
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
            # Obecne rozwiązanie
            solution = solbuff
            sollist.append((solbuff.copy(), maxval))

            if abs(past_sol - maxval) <= epsilon:
                self.stop_eps = True

            counter += 1

            if abs(past_sol - maxval) <= minieps:
                minieps = round(abs(past_sol - maxval), len(str(self.epsilon)))

            print(counter)
            if counter >= max_iter:
                self.stop_iter = True

            past_sol = maxval

        self.pb.setValue(max_iter)

        # Licznik kryteriów aspiracji
        # Licznik zakończeń na iteracji
        # Licznik zakończeń na epsilon

        return round(sum(bs_gain_rem)-sum(bs_loss_rem),2),round(sum(gain_rem)-sum(loss_rem),2), stop_type, licz_asp


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
