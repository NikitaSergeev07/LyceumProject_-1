
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from Models.Design_MainWindow import Ui_MainWindow  # Это наш конвертированный файл дизайна MainWindow
from Models.Design_MP3Player import Ui_MP3PlayerWindow  # Это наш конвертированный файл дизайна MP3Player


class Window_Of_Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Design_MainWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_MP3Player.clicked.connect(self.OpenMP3Player)  # Привязываем кнопку к методу

    def OpenMP3Player(self):
        self.MP3Player = Window_of_MP3Player()
        self.MP3Player.show()


class Window_of_MP3Player(QMainWindow, Ui_MP3PlayerWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Window_Of_Main()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
