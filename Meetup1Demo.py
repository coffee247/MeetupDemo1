#!/usr/bin/env python3


'''
MIT License 2020 Jim Stallings
'''

import random
import sys
import pymysql
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QAction, QMessageBox
import database as db
import setupUI
from PyQt5 import QtChart
from PyQt5.QtChart import QPieSeries, QPieSlice, QChartView, QChart
import cars

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        ''' Load the UI file from disk (UI file was created in QT Designer) '''
        uic.loadUi("mainwindow.ui", self)

        ''' Create an instance of the database class '''
        self.dbase = db.database()  # Create an instance of the database as self.dbase

        '''call the  Connect method on our new database object (Creates a database connection) '''
        self.dbase.Connect()
        self.conn = self.dbase.getConn()

        ''' Set up the menubar '''
        self.createMenus()

        self.carsModel = cars.carsModel()
        setupUI.doSetup(self)

        self.dbase.populateView(self, "select * from car order by make asc", self.carsModel)

        mySeries = QPieSeries()
        mySeries.append("jane", 2)
        mySeries.append("joe", 8)

        chart = QChart()
        chart.addSeries(mySeries)
        chart.setTitle("Simple piechart example")
        chart.legend().hide()

    # set up the application menuBar
    def createMenus(self):
        # Create the main menuBar menu items
        fileMenu = self.menuBar().addMenu("&File")

        # Populate File menu
        self.createAction("&Quit", fileMenu, self.close)

    # set up menuBar behavior
    def createAction(self, text, menu, slot):
        """ Helper function to save typing when populating menus
           with action.
        """
        action = QAction(text, self)
        menu.addAction(action)
        action.triggered.connect(slot)
        return action

    def doQuit(self):
        sys.exit()



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()


app.exec_()