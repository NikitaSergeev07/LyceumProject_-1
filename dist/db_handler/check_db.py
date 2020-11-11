from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler.db_handler import *

# Импортируем все необходимое
"""Смысл этого скрипта обрабатывать запросы к бд,
в отдельном потоке, чтобы основной интерфейс не зависал намертво"""

""""Создаем класс для управления потоками"""


class CheckThread(QtCore.QThread):  # Создаем класс для управления потоками
    mysignal = QtCore.pyqtSignal(str)  # Создаем сигнал

    """"Метод для отслеживания сигнала авторизации пользователя"""

    def thr_login(self, name, passw):
        login(name, passw, self.mysignal)

    """"Метод для отслеживания сигнала регистрации пользователя"""

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)
