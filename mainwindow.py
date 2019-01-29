# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 554)
        MainWindow.setMinimumSize(QtCore.QSize(697, 554))
        MainWindow.setMaximumSize(QtCore.QSize(697, 554))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Task-Manager.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 2, 681, 81))
        self.label.setStyleSheet("font: 25pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.events = QtWidgets.QTableWidget(self.centralwidget)
        self.events.setGeometry(QtCore.QRect(10, 130, 681, 391))
        self.events.setObjectName("events")
        self.events.setColumnCount(4)
        self.events.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.events.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.events.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.events.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.events.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 60, 511, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addEvent = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addEvent.setObjectName("addEvent")
        self.horizontalLayout.addWidget(self.addEvent)
        self.clearEvent = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearEvent.setObjectName("clearEvent")
        self.horizontalLayout.addWidget(self.clearEvent)
        self.saveToFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveToFile.setObjectName("saveToFile")
        self.horizontalLayout.addWidget(self.saveToFile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TaskManager"))
        self.label.setText(_translate("MainWindow", "TaskManager"))
        item = self.events.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.events.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время"))
        item = self.events.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.events.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Описание"))
        self.addEvent.setText(_translate("MainWindow", "Добавить задачу"))
        self.clearEvent.setText(_translate("MainWindow", "Очистить таблицу"))
        self.saveToFile.setText(_translate("MainWindow", "Сохранить в файл"))

