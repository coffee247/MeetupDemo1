from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtChart import QChartView, QChart

''' method to wire-up all the UI components '''
def doSetup(self): # self is a reference to the object from which this method was called.

    # create a local reference to the cars_TableView object defined in the UI
    self.carsView = self.findChild(QtWidgets.QTableView, 'cars_TableView')
    self.chartView = self.findChild(QChartView, 'carsCharView')
    a = 1

    # set up carsView
    self.carsView.setModel(self.carsModel)


    carsHeader = self.carsView.horizontalHeader()

    carsHeader.setSectionResizeMode(1, QHeaderView.Stretch)
    carsHeader.setSectionResizeMode(2, QHeaderView.Stretch)
    carsHeader.setDefaultSectionSize(20)

