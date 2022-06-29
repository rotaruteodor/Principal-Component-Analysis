import numpy as np
import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtCore import *


def populateListWidget(listWidget, items):
    listWidget.clear()
    for each in items:
        item = QListWidgetItem(each)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        listWidget.addItem(item)


def populateComboBox(combo, items):
    combo.clear()
    combo.addItems(items)
    combo.setCurrentIndex(0)


def citire_fisier(listWidget=None, comboBoxVarIndex=None, comboBoxAxa1=None, comboBoxAxa2=None):
    dialog = QFileDialog(directory=".")
    dialog.setNameFilter("CSV Files (*.csv)")
    dialog.exec_()

    files = dialog.selectedFiles()

    if len(files) > 0:
        dataTable = pd.read_csv(files[0])
        dataTableHead = list(dataTable)

        if listWidget is not None:
            populateListWidget(listWidget, dataTableHead)

        if comboBoxVarIndex is not None:
            populateComboBox(comboBoxVarIndex, dataTableHead)
            print(type(dataTableHead))

        listOfConsecutiveNumbers = [str(x) for x in list(np.arange(1, len(dataTableHead)+1))]

        if comboBoxAxa1 is not None:
            populateComboBox(comboBoxAxa1, listOfConsecutiveNumbers)
            print(listOfConsecutiveNumbers)

        if comboBoxAxa2 is not None:
            populateComboBox(comboBoxAxa2, listOfConsecutiveNumbers)
            comboBoxAxa2.setCurrentIndex(1)

        return dataTable, files[0]
