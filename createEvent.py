# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createEvent.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 451)
        Dialog.setMinimumSize(QtCore.QSize(639, 451))
        Dialog.setMaximumSize(QtCore.QSize(639, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Task-Manager.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 0, 251, 51))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 441, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setData = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget)
        self.setData.setObjectName("setData")
        self.horizontalLayout.addWidget(self.setData)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 70, 171, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setTime = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.setTime.setObjectName("setTime")
        self.verticalLayout.addWidget(self.setTime)
        self.setName = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setName.setObjectName("setName")
        self.verticalLayout.addWidget(self.setName)
        self.setDescription = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setDescription.setObjectName("setDescription")
        self.verticalLayout.addWidget(self.setDescription)
        self.over = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.over.setObjectName("over")
        self.verticalLayout.addWidget(self.over)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить событие"))
        self.label.setText(_translate("Dialog", "Выберите дату:"))
        self.label_2.setText(_translate("Dialog", "Выберите время:"))
        self.setName.setText(_translate("Dialog", "Ввести имя"))
        self.setDescription.setText(_translate("Dialog", "Ввести описание"))
        self.over.setText(_translate("Dialog", "Закончить"))

