import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from Models.Design_PhotoProcessing import Ui_PhotoProcessingWindow  # Импортируем наш дизайн
from PIL import Image
import sqlite3


def check_ext(path):
    _, ext = os.path.splitext(path)
    if ext not in (".png", ".jpg", ".jpeg"):  # Проверяем расширения mp3, mp4, mov
        raise ValueError()


# Импортировали все необходимое


class PhotoProcessing_Window(QMainWindow, Ui_PhotoProcessingWindow):  # PhotoProcessing меню
    """"Создаем конструктор класса PhotoProcessing_Window"""

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Design_MainWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.newimg = 'newimg'
        self.actionOpen.triggered.connect(self.initUI)
        self.initUI()
        self.actionNew.triggered.connect(self.newFile)

    # def load_image(self, file_name):
    #     pixmap = QPixmap(file_name)
    #
    #     self.label = QLabel(self)
    #     self.label.setPixmap(pixmap)
    #     self.label.resize(pixmap.width(), pixmap.height())
    #
    #     self.resize(pixmap.width(), pixmap.height())
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("butcher.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(100, 200)
        self.width()
        self.height()
        self.show()

        # self.extention = self.current.split('.')[-1]  # Парсим расширение файла
        # self.file = os.path.basename(self.current)  # Парсим имя файла без расширения
        # self.name = self.file[0:self.file.rfind('.')]  # Парсим имя файла без расширения
        # self.db_img = self.name + "." + self.extention
        # print(self.db_img)
        # self.newimg = self.newimg + "." + self.extention
        # print(self.newimg)
        # try:
        #     check_ext(self.current)
        #     # Подключаемся к нашей бд и создаем курсор
        #     con = sqlite3.connect('photo.db')
        #     cur = con.cursor()
        #     cur.execute(
        #         """INSERT INTO photo(name, path, extention) VALUES(?, ?, ?)"""), (
        #         self.name, self.current, self.extention).fetchall()
        #     # Закрываем соединение и курсор
        #     con.commit()
        #     con.close()
        # except ValueError:
        #     print("Что-то пошло не так")

    def newFile(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PhotoProcessing_Window()
    ex.show()
    sys.exit(app.exec_())
