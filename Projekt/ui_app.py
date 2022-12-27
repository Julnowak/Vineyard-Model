# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)

from canvas import Canvas
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 657)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(177, 13, 120)")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(148, 23, 165);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bfff = QPushButton(self.frame_top_menus)
        self.bfff.setObjectName(u"bfff")
        self.bfff.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.bfff.setFont(font1)
        self.bfff.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.bfff)

        self.hhhh = QFrame(self.frame_top_menus)
        self.hhhh.setObjectName(u"hhhh")
        self.hhhh.setMaximumSize(QSize(70, 40))
        self.hhhh.setStyleSheet(u"background-color: rgb(177, 13, 120)")
        self.hhhh.setFrameShape(QFrame.StyledPanel)
        self.hhhh.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.hhhh)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.hhhh)

        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT Condensed"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setUnderline(False)
        self.btn_page_1.setFont(font2)
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setFont(font2)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setFont(font2)
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page4 = QPushButton(self.frame_top_menus)
        self.btn_page4.setObjectName(u"btn_page4")
        self.btn_page4.setMinimumSize(QSize(0, 40))
        self.btn_page4.setFont(font2)
        self.btn_page4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page4)

        self.hh = QFrame(self.frame_top_menus)
        self.hh.setObjectName(u"hh")
        self.hh.setMaximumSize(QSize(70, 40))
        self.hh.setStyleSheet(u"background-color: rgb(177, 13, 120)")
        self.hh.setFrameShape(QFrame.StyledPanel)
        self.hh.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.hh)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.hh)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.btn_info = QPushButton(self.frame_left_menu)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT Condensed"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setUnderline(False)
        self.btn_info.setFont(font3)
        self.btn_info.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_info)

        self.btn_set = QPushButton(self.frame_left_menu)
        self.btn_set.setObjectName(u"btn_set")
        self.btn_set.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT Condensed"])
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.btn_set.setFont(font4)
        self.btn_set.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 17, 180, 105);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_set)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setFocusPolicy(Qt.StrongFocus)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_7 = QGroupBox(self.page)
        self.groupBox_7.setObjectName(u"groupBox_7")
        font5 = QFont()
        font5.setFamilies([u"Tw Cen MT Condensed"])
        font5.setPointSize(14)
        self.groupBox_7.setFont(font5)
        self.groupBox_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 30, 101, 208))
        self.verticalLayout_25 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.verticalLayoutWidget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_32)

        self.radioButton = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font5)
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font5)
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_2.setChecked(True)

        self.verticalLayout_25.addWidget(self.radioButton_2)

        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label)

        self.spinBox = QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font5)
        self.spinBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setValue(1)

        self.verticalLayout_25.addWidget(self.spinBox)

        self.label_2 = QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font5)
        self.spinBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_2.setWrapping(False)
        self.spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setSingleStep(0)
        self.spinBox_2.setValue(3)

        self.verticalLayout_25.addWidget(self.spinBox_2)

        self.label_36 = QLabel(self.groupBox_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(190, 120, 181, 22))
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.groupBox_7, 1, 0, 5, 2)

        self.label_34 = QLabel(self.page)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_34, 6, 1, 1, 1)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font5)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 221, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Grignolino = QCheckBox(self.gridLayoutWidget)
        self.Grignolino.setObjectName(u"Grignolino")
        self.Grignolino.setFont(font5)
        self.Grignolino.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Grignolino, 4, 0, 1, 1)

        self.Barbera = QCheckBox(self.gridLayoutWidget)
        self.Barbera.setObjectName(u"Barbera")
        self.Barbera.setFont(font5)
        self.Barbera.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Barbera, 0, 0, 1, 1)

        self.Cortese = QCheckBox(self.gridLayoutWidget)
        self.Cortese.setObjectName(u"Cortese")
        self.Cortese.setFont(font5)
        self.Cortese.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Cortese, 3, 1, 1, 1)

        self.Erbaluce = QCheckBox(self.gridLayoutWidget)
        self.Erbaluce.setObjectName(u"Erbaluce")
        self.Erbaluce.setFont(font5)
        self.Erbaluce.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Erbaluce, 4, 1, 1, 1)

        self.Dolcetto = QCheckBox(self.gridLayoutWidget)
        self.Dolcetto.setObjectName(u"Dolcetto")
        self.Dolcetto.setFont(font5)
        self.Dolcetto.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Dolcetto, 3, 0, 1, 1)

        self.Chardonnay = QCheckBox(self.gridLayoutWidget)
        self.Chardonnay.setObjectName(u"Chardonnay")
        self.Chardonnay.setFont(font5)
        self.Chardonnay.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Chardonnay, 0, 1, 1, 1)

        self.Arneis = QCheckBox(self.gridLayoutWidget)
        self.Arneis.setObjectName(u"Arneis")
        self.Arneis.setFont(font5)
        self.Arneis.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Arneis, 1, 1, 1, 1)

        self.Nebbiolo = QCheckBox(self.gridLayoutWidget)
        self.Nebbiolo.setObjectName(u"Nebbiolo")
        self.Nebbiolo.setFont(font5)
        self.Nebbiolo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.Nebbiolo, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 2, 3, 1)

        self.groupBox_10 = QGroupBox(self.page)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font5)
        self.groupBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_10)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(20, 30, 193, 116))
        self.verticalLayout_28 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setFont(font5)
        self.spinBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_3.setWrapping(False)
        self.spinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_3.setMaximum(999999999)
        self.spinBox_3.setValue(600)

        self.verticalLayout_28.addWidget(self.spinBox_3)

        self.label_10 = QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_10)

        self.eps_5 = QDoubleSpinBox(self.verticalLayoutWidget_7)
        self.eps_5.setObjectName(u"eps_5")
        self.eps_5.setFont(font5)
        self.eps_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eps_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.eps_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.eps_5.setProperty("showGroupSeparator", False)
        self.eps_5.setDecimals(2)
        self.eps_5.setMaximum(9999999999999999455752309870428160.000000000000000)
        self.eps_5.setSingleStep(0.010000000000000)
        self.eps_5.setValue(2.000000000000000)

        self.verticalLayout_28.addWidget(self.eps_5)


        self.gridLayout_2.addWidget(self.groupBox_10, 1, 3, 3, 1)

        self.label_31 = QLabel(self.page)
        self.label_31.setObjectName(u"label_31")
        font6 = QFont()
        font6.setFamilies([u"Tw Cen MT Condensed"])
        font6.setPointSize(36)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setKerning(True)
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_31, 0, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.pushButton_2, 10, 0, 1, 1)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.pushButton, 9, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.page)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font5)
        self.groupBox_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_8 = QWidget(self.groupBox_12)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(20, 30, 191, 191))
        self.verticalLayout_29 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_4)

        self.spinBox_4 = QSpinBox(self.verticalLayoutWidget_8)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setFont(font5)
        self.spinBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_4.setWrapping(False)
        self.spinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setValue(1)

        self.verticalLayout_29.addWidget(self.spinBox_4)

        self.label_9 = QLabel(self.verticalLayoutWidget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_9)

        self.eps_4 = QDoubleSpinBox(self.verticalLayoutWidget_8)
        self.eps_4.setObjectName(u"eps_4")
        self.eps_4.setFont(font5)
        self.eps_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eps_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.eps_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.eps_4.setProperty("showGroupSeparator", False)
        self.eps_4.setDecimals(2)
        self.eps_4.setMaximum(9999999999999999455752309870428160.000000000000000)
        self.eps_4.setSingleStep(0.010000000000000)
        self.eps_4.setValue(3.000000000000000)

        self.verticalLayout_29.addWidget(self.eps_4)

        self.label_6 = QLabel(self.verticalLayoutWidget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_6)

        self.eps_6 = QDoubleSpinBox(self.verticalLayoutWidget_8)
        self.eps_6.setObjectName(u"eps_6")
        self.eps_6.setFont(font5)
        self.eps_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eps_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.eps_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.eps_6.setProperty("showGroupSeparator", False)
        self.eps_6.setDecimals(2)
        self.eps_6.setMaximum(9999999999999999455752309870428160.000000000000000)
        self.eps_6.setSingleStep(0.010000000000000)
        self.eps_6.setValue(3.000000000000000)

        self.verticalLayout_29.addWidget(self.eps_6)


        self.gridLayout_2.addWidget(self.groupBox_12, 4, 3, 4, 1)

        self.groupBox_8 = QGroupBox(self.page)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font5)
        self.groupBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_8)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 70, 211, 148))
        self.verticalLayout_26 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_7)

        self.comboBox = QComboBox(self.verticalLayoutWidget_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_26.addWidget(self.comboBox)

        self.label_8 = QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_8)

        self.eps_7 = QDoubleSpinBox(self.verticalLayoutWidget_5)
        self.eps_7.setObjectName(u"eps_7")
        self.eps_7.setFont(font5)
        self.eps_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eps_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.eps_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.eps_7.setProperty("showGroupSeparator", False)
        self.eps_7.setDecimals(2)
        self.eps_7.setMaximum(9999999999999999455752309870428160.000000000000000)
        self.eps_7.setSingleStep(0.010000000000000)
        self.eps_7.setValue(2.000000000000000)

        self.verticalLayout_26.addWidget(self.eps_7)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox_8)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 30, 160, 31))
        self.verticalLayout_27 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font5)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.checkBox.setChecked(True)

        self.verticalLayout_27.addWidget(self.checkBox)


        self.gridLayout_2.addWidget(self.groupBox_8, 4, 2, 4, 1)

        self.label_35 = QLabel(self.page)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_35, 7, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font5)
        self.groupBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 30, 451, 61))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.iteracje = QLabel(self.gridLayoutWidget_4)
        self.iteracje.setObjectName(u"iteracje")
        self.iteracje.setFont(font5)
        self.iteracje.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.iteracje.setTextFormat(Qt.AutoText)
        self.iteracje.setScaledContents(False)
        self.iteracje.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.iteracje, 0, 1, 1, 1)

        self.eps = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.eps.setObjectName(u"eps")
        self.eps.setFont(font5)
        self.eps.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.eps.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.eps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.eps.setProperty("showGroupSeparator", False)
        self.eps.setDecimals(4)
        self.eps.setMaximum(9999999999999999455752309870428160.000000000000000)
        self.eps.setSingleStep(0.010000000000000)
        self.eps.setValue(0.100000000000000)

        self.gridLayout_4.addWidget(self.eps, 1, 0, 1, 1)

        self.epsilon = QLabel(self.gridLayoutWidget_4)
        self.epsilon.setObjectName(u"epsilon")
        self.epsilon.setFont(font5)
        self.epsilon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.epsilon.setTextFormat(Qt.AutoText)
        self.epsilon.setScaledContents(False)
        self.epsilon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.epsilon, 0, 0, 1, 1)

        self.iter = QSpinBox(self.gridLayoutWidget_4)
        self.iter.setObjectName(u"iter")
        self.iter.setFont(font5)
        self.iter.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.iter.setWrapping(False)
        self.iter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iter.setMaximum(999999999)
        self.iter.setValue(50)

        self.gridLayout_4.addWidget(self.iter, 1, 1, 1, 1)

        self.iter_2 = QSpinBox(self.gridLayoutWidget_4)
        self.iter_2.setObjectName(u"iter_2")
        self.iter_2.setFont(font5)
        self.iter_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.iter_2.setWrapping(False)
        self.iter_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iter_2.setMaximum(999999999)
        self.iter_2.setValue(50)

        self.gridLayout_4.addWidget(self.iter_2, 1, 2, 1, 1)

        self.iteracje_2 = QLabel(self.gridLayoutWidget_4)
        self.iteracje_2.setObjectName(u"iteracje_2")
        self.iteracje_2.setFont(font5)
        self.iteracje_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.iteracje_2.setTextFormat(Qt.AutoText)
        self.iteracje_2.setScaledContents(False)
        self.iteracje_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.iteracje_2, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 8, 2, 3, 2)

        self.stackedWidget.addWidget(self.page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.start = QPushButton(self.page_7)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(260, 400, 391, 101))
        font7 = QFont()
        font7.setFamilies([u"Tw Cen MT Condensed"])
        font7.setPointSize(26)
        self.start.setFont(font7)
        self.start.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.stackedWidget.addWidget(self.page_7)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.graphWidget = PlotWidget(self.page_2)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(50, 0, 801, 571))
        self.graphWidget.setLineWidth(5)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        self.graphWidget.setBackgroundBrush(brush)
        self.graphWidget.setInteractive(True)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget = Canvas(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 911, 551))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.checkBox_4 = QCheckBox(self.page_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(400, 130, 70, 17))
        self.stackedWidget.addWidget(self.page_4)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.buttonBox = QDialogButtonBox(self.page_8)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(460, 200, 156, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.spinBox)
        self.label_2.setBuddy(self.spinBox_2)
        self.label_3.setBuddy(self.spinBox_3)
        self.iteracje.setBuddy(self.iter)
        self.epsilon.setBuddy(self.eps)
        self.iteracje_2.setBuddy(self.iter)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Model Winnicy", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"\ud83c\udf47", None))
        self.bfff.setText("")
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Wykres 1", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Wykres 2", None))
        self.btn_page4.setText(QCoreApplication.translate("MainWindow", u"Wykres 3", None))
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"\u24d8", None))
        self.btn_set.setText(QCoreApplication.translate("MainWindow", u"\u2699", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Podstawowe dane", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Jednostka czasu", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Miesi\u0105ce", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Lata", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Czas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Liczba p\u00f3l", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Tu tabela// ustawianie warto\u015bci", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Kryterium Aspiracji", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Rodzaje winogron", None))
        self.Grignolino.setText(QCoreApplication.translate("MainWindow", u"Grignolino", None))
        self.Barbera.setText(QCoreApplication.translate("MainWindow", u"Barbera", None))
        self.Cortese.setText(QCoreApplication.translate("MainWindow", u"Cortese", None))
        self.Erbaluce.setText(QCoreApplication.translate("MainWindow", u"Erbaluce", None))
        self.Dolcetto.setText(QCoreApplication.translate("MainWindow", u"Dolcetto", None))
        self.Chardonnay.setText(QCoreApplication.translate("MainWindow", u"Chardonnay", None))
        self.Arneis.setText(QCoreApplication.translate("MainWindow", u"Arneis", None))
        self.Nebbiolo.setText(QCoreApplication.translate("MainWindow", u"Nebbiolo", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Kwestie magazynowania", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pojemno\u015b\u0107 magazynu", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Koszt magazynowania (1 butelka)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"USTAWIENIA", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Zatwierd\u017a", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Produkcja i transport", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 jednostek winogron na butelk\u0119", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Koszt transportu (1 butelka)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Koszt butelki", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Piel\u0119gnacja pola", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Typ i koszt nawozu", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Standardowy (+5%) - 2z\u0142/szt", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Wy\u017cszej jako\u015bci (+10%) - 4z\u0142/szt", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Najwy\u017cszej jako\u015bci (_+17%) - 7z\u0142/szt", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Koszt zbioru 1 jednostki winogron", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Czy u\u017cyto nawozu?", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Typy Tabu List?", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Warunki STOP", None))
        self.iteracje.setText(QCoreApplication.translate("MainWindow", u"Iteracje", None))
        self.epsilon.setText(QCoreApplication.translate("MainWindow", u"Epsilon", None))
        self.iteracje_2.setText(QCoreApplication.translate("MainWindow", u"D\u0142ugo\u015b\u0107 Listy Tabu", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

