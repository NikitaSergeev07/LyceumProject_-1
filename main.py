import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets  # Импортируем все необходимое для работы с PyQt5
from PyQt5.QtWidgets import QMainWindow  # Импортируем все необходимое для работы с PyQt5
from Models.Design_MainWindow import Ui_MainWindow  # Это наш конвертированный файл дизайна MainWindow
from Models.Design_MP3Player import Ui_MP3PlayerWindow  # Это наш конвертированный файл дизайна MP3Player
from Presenters.Func_For_MP3Player import MP3_MainWindow  # Импортируем функции нашего MP3Player
from Models.Design_PhotoProcessing import \
    Ui_PhotoProcessingWindow  # Это наш конвертированный файл дизайна PhotoProcessing
from db_handler.main_db import Interface  # Импортируем работу с бд


class Window_of_Main(QMainWindow, Ui_MainWindow):  # Главное меню
    """"Создаем конструктор класса Window_of_Main"""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Design_MainWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_MP3Player.clicked.connect(self.openMP3Player)  # Привязываем кнопку к методу
        self.btn_PhotoProcessing.clicked.connect(self.openPhotoProcessing)  # Привязываем кнопку к методу

    """"Создаем метод для открытия MP3Player"""

    def openMP3Player(self):
        self.MP3Player = MP3_MainWindow()  # Создаем экземпляр нашего класса с MP3Player
        self.MP3Player.show()  # Выводим пользователю приложение на экран

    """"Создаем метод для открытия PhotoProcessing"""

    def openPhotoProcessing(self):
        self.PhotoProcessing = Window_of_PhotoProcessing()  # Создаем экземпляр нашего класса с PhotoProcessing
        self.PhotoProcessing.show()  # Выводим пользователю приложение на экран


class Window_of_MP3Player(QMainWindow, Ui_MP3PlayerWindow):  # MP3Player
    """"Создаем конструктор класса Window_of_MP3Player"""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


class Window_of_PhotoProcessing(QMainWindow, Ui_PhotoProcessingWindow):
    """"Создаем конструктор класса Window_of_PhotoProcessing"""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    mainMenu_window = Window_of_Main()  # Создаём объект класса ExampleApp
    mainMenu_window.show()  # Показываем окно

    """"Пытаемся открыть окно авторизации пользователя"""

    try:
        db_window = Interface()
        db_window.show()
    except Exception:
        pass

    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
