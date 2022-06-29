# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_Rotaru.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1247, 715)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBoxCitireDate = QGroupBox(self.centralwidget)
        self.groupBoxCitireDate.setObjectName(u"groupBoxCitireDate")
        self.groupBoxCitireDate.setGeometry(QRect(10, 10, 571, 661))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.groupBoxCitireDate.setFont(font)
        self.btnCitireDate = QPushButton(self.groupBoxCitireDate)
        self.btnCitireDate.setObjectName(u"btnCitireDate")
        self.btnCitireDate.setGeometry(QRect(20, 30, 531, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.btnCitireDate.setFont(font1)
        self.lineEditCaleFisie = QLineEdit(self.groupBoxCitireDate)
        self.lineEditCaleFisie.setObjectName(u"lineEditCaleFisie")
        self.lineEditCaleFisie.setGeometry(QRect(20, 70, 531, 31))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.lineEditCaleFisie.setFont(font2)
        self.listWidgetVariabile = QListWidget(self.groupBoxCitireDate)
        self.listWidgetVariabile.setObjectName(u"listWidgetVariabile")
        self.listWidgetVariabile.setGeometry(QRect(20, 200, 531, 401))
        self.labelCheckBoxVariabile = QLabel(self.groupBoxCitireDate)
        self.labelCheckBoxVariabile.setObjectName(u"labelCheckBoxVariabile")
        self.labelCheckBoxVariabile.setGeometry(QRect(20, 180, 191, 16))
        self.btnSelecteazaToateVariabilele = QPushButton(self.groupBoxCitireDate)
        self.btnSelecteazaToateVariabilele.setObjectName(u"btnSelecteazaToateVariabilele")
        self.btnSelecteazaToateVariabilele.setGeometry(QRect(454, 610, 91, 24))
        self.comboBoxVariabilaIndex = QComboBox(self.groupBoxCitireDate)
        self.comboBoxVariabilaIndex.setObjectName(u"comboBoxVariabilaIndex")
        self.comboBoxVariabilaIndex.setGeometry(QRect(20, 140, 531, 22))
        self.labelVariabilaIndex = QLabel(self.groupBoxCitireDate)
        self.labelVariabilaIndex.setObjectName(u"labelVariabilaIndex")
        self.labelVariabilaIndex.setGeometry(QRect(20, 120, 131, 16))
        self.labelVariabilaIndex.setWordWrap(False)
        self.groupBoxAnalizaComponente = QGroupBox(self.centralwidget)
        self.groupBoxAnalizaComponente.setObjectName(u"groupBoxAnalizaComponente")
        self.groupBoxAnalizaComponente.setGeometry(QRect(620, 10, 591, 661))
        font3 = QFont()
        font3.setBold(True)
        self.groupBoxAnalizaComponente.setFont(font3)
        self.btnExpTabelVarianta = QPushButton(self.groupBoxAnalizaComponente)
        self.btnExpTabelVarianta.setObjectName(u"btnExpTabelVarianta")
        self.btnExpTabelVarianta.setGeometry(QRect(20, 40, 201, 24))
        self.btnPlotVarianta = QPushButton(self.groupBoxAnalizaComponente)
        self.btnPlotVarianta.setObjectName(u"btnPlotVarianta")
        self.btnPlotVarianta.setGeometry(QRect(360, 40, 141, 24))
        self.btnExpCorelatiiFactoriale = QPushButton(self.groupBoxAnalizaComponente)
        self.btnExpCorelatiiFactoriale.setObjectName(u"btnExpCorelatiiFactoriale")
        self.btnExpCorelatiiFactoriale.setGeometry(QRect(20, 100, 201, 24))
        self.btnPlotCorelatiiFactoriale = QPushButton(self.groupBoxAnalizaComponente)
        self.btnPlotCorelatiiFactoriale.setObjectName(u"btnPlotCorelatiiFactoriale")
        self.btnPlotCorelatiiFactoriale.setGeometry(QRect(360, 110, 141, 24))
        self.btnPlotCorelatii = QPushButton(self.groupBoxAnalizaComponente)
        self.btnPlotCorelatii.setObjectName(u"btnPlotCorelatii")
        self.btnPlotCorelatii.setGeometry(QRect(360, 180, 141, 24))
        self.btnExpComponentePrincipale = QPushButton(self.groupBoxAnalizaComponente)
        self.btnExpComponentePrincipale.setObjectName(u"btnExpComponentePrincipale")
        self.btnExpComponentePrincipale.setGeometry(QRect(10, 270, 221, 24))
        self.btnPlotComponente = QPushButton(self.groupBoxAnalizaComponente)
        self.btnPlotComponente.setObjectName(u"btnPlotComponente")
        self.btnPlotComponente.setGeometry(QRect(360, 270, 141, 24))
        self.btnExportaCosinusuri = QPushButton(self.groupBoxAnalizaComponente)
        self.btnExportaCosinusuri.setObjectName(u"btnExportaCosinusuri")
        self.btnExportaCosinusuri.setGeometry(QRect(30, 470, 201, 24))
        self.btnExpComunalitati = QPushButton(self.groupBoxAnalizaComponente)
        self.btnExpComunalitati.setObjectName(u"btnExpComunalitati")
        self.btnExpComunalitati.setGeometry(QRect(30, 380, 201, 24))
        self.btnPlotComunalitati = QPushButton(self.groupBoxAnalizaComponente)
        self.btnPlotComunalitati.setObjectName(u"btnPlotComunalitati")
        self.btnPlotComunalitati.setGeometry(QRect(360, 380, 141, 24))
        self.comboBoxAxa1 = QComboBox(self.groupBoxAnalizaComponente)
        self.comboBoxAxa1.setObjectName(u"comboBoxAxa1")
        self.comboBoxAxa1.setGeometry(QRect(120, 180, 51, 22))
        self.comboBoxAxa2 = QComboBox(self.groupBoxAnalizaComponente)
        self.comboBoxAxa2.setObjectName(u"comboBoxAxa2")
        self.comboBoxAxa2.setGeometry(QRect(180, 180, 51, 22))
        self.label = QLabel(self.groupBoxAnalizaComponente)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 180, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1247, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxCitireDate.setTitle(QCoreApplication.translate("MainWindow", u"Citire Date", None))
        self.btnCitireDate.setText(QCoreApplication.translate("MainWindow", u"Selecteaza fisier", None))
        self.labelCheckBoxVariabile.setText(QCoreApplication.translate("MainWindow", u"Selectati variabilele pentru analiza:", None))
        self.btnSelecteazaToateVariabilele.setText(QCoreApplication.translate("MainWindow", u"Selecteaza tot", None))
        self.labelVariabilaIndex.setText(QCoreApplication.translate("MainWindow", u"Selectati variabila index", None))
        self.groupBoxAnalizaComponente.setTitle(QCoreApplication.translate("MainWindow", u"Analiza in componente principale", None))
        self.btnExpTabelVarianta.setText(QCoreApplication.translate("MainWindow", u"Exporta CSV tabel varianta", None))
        self.btnPlotVarianta.setText(QCoreApplication.translate("MainWindow", u"Plot varianta", None))
        self.btnExpCorelatiiFactoriale.setText(QCoreApplication.translate("MainWindow", u"Exporta CSV corelatii factoriale", None))
        self.btnPlotCorelatiiFactoriale.setText(QCoreApplication.translate("MainWindow", u"Plot corelatii factoriale", None))
        self.btnPlotCorelatii.setText(QCoreApplication.translate("MainWindow", u"Plot corelatii", None))
        self.btnExpComponentePrincipale.setText(QCoreApplication.translate("MainWindow", u"Exporta CSV componente principale", None))
        self.btnPlotComponente.setText(QCoreApplication.translate("MainWindow", u"Plot componente", None))
        self.btnExportaCosinusuri.setText(QCoreApplication.translate("MainWindow", u"Exporta CSV cosinus-uri", None))
        self.btnExpComunalitati.setText(QCoreApplication.translate("MainWindow", u"Exporta CSV comunalitati", None))
        self.btnPlotComunalitati.setText(QCoreApplication.translate("MainWindow", u"Plot comunalitati", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selectati axele:", None))
    # retranslateUi

