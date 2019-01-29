import csv
import datetime
from sys import argv

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import *

import createEvent
import mainwindow
import name
import write


# функция логгирования
def logging(exception):
    try:
        with open('log.txt', 'a') as file:
            file.write(exception)
    except Exception:
        pass


# Класс окна

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.description = '-'  # описание события
        self.time = '-'  # время события
        self.name = '-'  # имя события
        self.date = '-'  # текущее время
        self.initUi()  # инициализируем интерфейс

    def initUi(self):
        self.load()  # подгружаем данные из csv файла
        self.addEvent.clicked.connect(self.add)  # подключаем ответную функцию на клик к кнопке Добавить событие
        self.clearEvent.clicked.connect(
            self.clearEvents)  # подключаем ответную функцию на клик к кнопке Очистить таблицу
        self.saveToFile.clicked.connect(self.save)  # подключаем ответную функцию на клик к кнопке Сохранить в файл

    # функция сохранения в файл
    def save(self):
        try:
            with open('data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in range(0, self.events.rowCount()):
                    writer.writerow(
                        [self.events.item(i, 0).text(), self.events.item(i, 1).text(), self.events.item(i, 2).text(),
                         self.events.item(i, 3).text()])
        except Exception as exc:
            logging(exc)

    # функция загрузки из файла
    def load(self):
        try:
            with open('data.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in reader:
                    self.events.insertRow(self.events.rowCount())
                    for j in range(4):
                        self.events.setItem(self.events.rowCount() - 1, j, QTableWidgetItem(row[j]))
        except Exception as exc:
            logging(exc)

    # функция добавления события
    def add(self):
        try:
            # диалог добавления события
            self.dialogEvent = QDialog()
            self.dialogEvent.ui = createEvent.Ui_Dialog()
            self.dialogEvent.ui.setupUi(self.dialogEvent)
            self.dialogEvent.ui.setData.setMinimumDate(QDate.currentDate())
            self.dialogEvent.ui.setDescription.clicked.connect(self.addDescription)
            self.dialogEvent.ui.setName.clicked.connect(self.setName)
            self.dialogEvent.ui.over.clicked.connect(self.overEvent)
            self.dialogEvent.exec_()
            #
            self.events.insertRow(self.events.rowCount())
            self.events.setItem(self.events.rowCount() - 1, 0, QTableWidgetItem(str(self.name)))
            self.events.setItem(self.events.rowCount() - 1, 1, QTableWidgetItem(str(self.time)))
            self.events.setItem(self.events.rowCount() - 1, 2, QTableWidgetItem(str(self.date)))
            self.events.setItem(self.events.rowCount() - 1, 3, QTableWidgetItem(str(self.description)))
        except Exception as exc:
            logging(exc)

    # установить имя событию
    def setName(self):
        self.dialogName = QDialog()
        self.dialogName.ui = name.Ui_Dialog()
        self.dialogName.ui.setupUi(self.dialogName)
        self.dialogName.ui.pushButton.clicked.connect(self.overName)
        self.dialogName.exec_()

    # получить имя из диалога установки имени
    def overName(self):
        self.name = self.dialogName.ui.lineEdit.text()
        self.dialogName.close()

    # функция, запускающая диалог добавления описания к событию
    def addDescription(self):
        self.dialogDescription = QDialog()
        self.dialogDescription.ui = write.Ui_Dialog()
        self.dialogDescription.ui.setupUi(self.dialogDescription)
        self.dialogDescription.ui.over.clicked.connect(self.overDescript)
        self.dialogDescription.exec_()

    # получить описание из диалога добавления описания
    def overDescript(self):
        self.description = self.dialogDescription.ui.description.toPlainText()
        self.dialogDescription.close()

    # получить дату и время из диалога добавления события
    def overEvent(self):
        self.time = self.dialogEvent.ui.setTime.time().toString(Qt.DefaultLocaleLongDate)
        self.date = self.dialogEvent.ui.setData.selectedDate().toString(Qt.DefaultLocaleLongDate)
        self.dialogEvent.close()

    # функция очистки таблицы
    def clearEvents(self):
        for i in range(self.events.rowCount(), -1, -1):
            self.events.removeRow(i)
        try:
            with open('data.csv', 'w') as file:
                file.write('')
        except Exception as exc:
            logging(exc)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
