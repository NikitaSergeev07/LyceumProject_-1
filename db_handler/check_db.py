from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler.db_handler import *
import db_handler.main_db

# Импортируем все необходимое


""""Создаем класс для управления потоками"""


class CheckThread(QtCore.QThread):  # Создаем класс для управления потоками
    mysignal = QtCore.pyqtSignal(str)  # Создаем сигнал

    """"Метод для отслеживания сигнала авторизации пользователя"""

    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    """"Метод для отслеживания сигнала регистрации пользователя"""

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)
