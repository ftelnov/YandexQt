# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'write.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(489, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Task-Manager.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(10, 50, 471, 231))
        self.description.setObjectName("description")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 461, 31))
        self.label.setMinimumSize(QtCore.QSize(461, 31))
        self.label.setMaximumSize(QtCore.QSize(461, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.over = QtWidgets.QPushButton(Dialog)
        self.over.setGeometry(QtCore.QRect(180, 290, 121, 31))
        self.over.setObjectName("over")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Введите описание события"))
        self.label.setText(_translate("Dialog", "Пожалуйста, введите описание!"))
        self.over.setText(_translate("Dialog", "Я закончил!"))

