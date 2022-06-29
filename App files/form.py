import numpy as np
from PySide6.QtWidgets import QMessageBox
from gui import *
import controller
from acp import acp
from utils import nan_replace, getDataFrame, corelograma, plot_corelatii, plot_componente, show
from tkinter import filedialog
from pathlib import Path


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dataTable = None
        self.model_creat = False

        self.btnCitireDate.clicked.connect(self.citireFisierCSV)
        self.btnSelecteazaToateVariabilele.clicked.connect(lambda: self.selecteazaToateVariabileleDinCheckBox(self.listWidgetVariabile))
        self.btnExpTabelVarianta.clicked.connect(self.exportaTabelVarianta)
        self.btnPlotVarianta.clicked.connect(self.plotVarianta)
        self.btnExpCorelatiiFactoriale.clicked.connect(self.exportaCorelatiiFactoriale)
        self.btnPlotCorelatiiFactoriale.clicked.connect(self.plotCorelatiiFactoriale)
        self.btnPlotCorelatii.clicked.connect(self.plotCorelatii)
        self.btnExpComponentePrincipale.clicked.connect(self.exportaComponentePrincipale)
        self.btnPlotComponente.clicked.connect(self.plotComponente)
        self.btnExportaCosinusuri.clicked.connect(self.exportaCosinusuri)
        self.btnExpComunalitati.clicked.connect(self.exportaComunalitati)
        self.btnPlotComunalitati.clicked.connect(self.plotComunalitati)


    def invalidare_model(self):
        self.model_creat = False


    def showDialogForCsvFileSave(self, path):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Fisierul CSV a fost salvat in " + path + " !")
        msg.setWindowTitle("Succes!")
        msg.exec_()


    def citireFisierCSV(self):
        dataTable, selectedDataFile = controller.citire_fisier(self.listWidgetVariabile, self.comboBoxVariabilaIndex, self.comboBoxAxa1, self.comboBoxAxa2)
        if dataTable is not None and selectedDataFile is not None:
            self.dataTable = nan_replace(dataTable)
            self.lineEditCaleFisie.setText(selectedDataFile)
        self.invalidare_model()


    def selecteazaToateVariabileleDinCheckBox(self, listWidget):
        for i in range(listWidget.count()):
            listWidget.item(i).setCheckState(Qt.Checked)


    def exportaTabelVarianta(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()
            tabel_varianta = model.tabelare_varianta()

            pathForSaving = filedialog.askdirectory(title='Pick a folder', initialdir=str(Path.home()))
            if len(pathForSaving) > 0:
                tabel_varianta.to_csv(pathForSaving + '/Tabel Varianta' + '.csv')
                self.showDialogForCsvFileSave(pathForSaving)


    def plotVarianta(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()
            model.plot_varianta()
            show()


    def exportaCorelatiiFactoriale(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            r_x_c = model.r_x_c
            r_x_c_t = getDataFrame(r_x_c, variabile_observate, model.etichete_componente)

            pathForSaving = filedialog.askdirectory(title='Pick a folder', initialdir=str(Path.home()))
            if len(pathForSaving) > 0:
                r_x_c_t.to_csv(pathForSaving + '/Tabel Corelatii Factoriale' + '.csv')
                self.showDialogForCsvFileSave(pathForSaving)


    def plotCorelatiiFactoriale(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            r_x_c = model.r_x_c
            r_x_c_t = getDataFrame(r_x_c, variabile_observate, model.etichete_componente)
            corelograma(r_x_c_t)
            show()


    def plotCorelatii(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            r_x_c = model.r_x_c
            r_x_c_t = getDataFrame(r_x_c, variabile_observate, model.etichete_componente)

            plot_corelatii(r_x_c_t, "Comp" + self.comboBoxAxa1.currentText(), "Comp" + self.comboBoxAxa2.currentText())
            show()


    def exportaComponentePrincipale(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            componente = model.c
            componente_t = getDataFrame(componente, self.dataTable[self.comboBoxVariabilaIndex.currentText()], model.etichete_componente)

            pathForSaving = filedialog.askdirectory(title='Pick a folder', initialdir=str(Path.home()))
            if len(pathForSaving) > 0:
                componente_t.to_csv(pathForSaving + '/Tabel Componente Principale' + '.csv')
                self.showDialogForCsvFileSave(pathForSaving)


    def plotComponente(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            componente = model.c
            componente_t = getDataFrame(componente, self.dataTable[self.comboBoxVariabilaIndex.currentText()], model.etichete_componente)

            plot_componente(componente_t, "Comp" + self.comboBoxAxa1.currentText(), "Comp" + self.comboBoxAxa2.currentText(), aspect=1)
            show()


    def exportaCosinusuri(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            componente = model.c
            c_patrat = componente * componente
            cosin = np.transpose(c_patrat.T / np.sum(c_patrat, axis=1))
            cosin_t = getDataFrame(cosin, self.dataTable[self.comboBoxVariabilaIndex.currentText()], model.etichete_componente)

            pathForSaving = filedialog.askdirectory(title='Pick a folder', initialdir=str(Path.home()))
            if len(pathForSaving) > 0:
                cosin_t.to_csv(pathForSaving + '/Tabel Cosinusuri' + '.csv')
                self.showDialogForCsvFileSave(pathForSaving)


    def exportaComunalitati(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            r_x_c = model.r_x_c
            r_x_c_patrat = r_x_c * r_x_c
            comunalitati = np.cumsum(r_x_c_patrat, axis=1)
            comunalitati_t = getDataFrame(comunalitati, variabile_observate, model.etichete_componente)

            pathForSaving = filedialog.askdirectory(title='Pick a folder', initialdir=str(Path.home()))
            if len(pathForSaving) > 0:
                comunalitati_t.to_csv(pathForSaving + '/Tabel Comunalitati' + '.csv')
                self.showDialogForCsvFileSave(pathForSaving)


    def plotComunalitati(self):
        if self.dataTable is not None:
            variabileSelectateInComboBox = []

            for index in range(self.listWidgetVariabile.count()):
                if self.listWidgetVariabile.item(index).checkState() == Qt.Checked:
                    variabileSelectateInComboBox.append(self.listWidgetVariabile.item(index).text())

            variabile_observate = list(variabileSelectateInComboBox)
            model = acp(self.dataTable, variabile_observate)
            model.creare_model()

            r_x_c = model.r_x_c
            r_x_c_patrat = r_x_c * r_x_c
            comunalitati = np.cumsum(r_x_c_patrat, axis=1)
            comunalitati_t = getDataFrame(comunalitati, variabile_observate, model.etichete_componente)

            corelograma(comunalitati_t, titlu="Comunalitati")
            show()
