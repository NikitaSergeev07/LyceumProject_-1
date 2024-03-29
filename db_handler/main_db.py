import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler.check_db import *
from db_handler.Design_DB import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Импортировали все необходимое

class Interface(QtWidgets.QWidget):
    """"Создаем конструктор класса Interface"""

    def __init__(self, parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Design_DB.py
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Подключаем кнопки к методам
        self.ui.pushButton.clicked.connect(self.reg)  # Кнопка регистрации пользователя
        self.ui.pushButton_2.clicked.connect(self.auth)  # Кнопка авторизации пользователя
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]  # Кнопки ввода пароля и ника пользователя

        # Делаем различные подключения
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    # Проверка правильности ввода(декоратор)
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    # Если ввод правильный, то авторизуем пользователя
    def auth(self):
        try:
            name = self.ui.lineEdit.text()
            passw = self.ui.lineEdit_2.text()
            self.check_db.thr_login(name, passw)
        except Exception:
            print("Что-то пошло не так!")

    @check_input
    # Если ввод правильный, то регистрируем пользователя
    def reg(self):
        try:
            name = self.ui.lineEdit.text()
            passw = self.ui.lineEdit_2.text()
            self.check_db.thr_register(name, passw)
        except Exception:
            print("Что-то пошло не так!")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
