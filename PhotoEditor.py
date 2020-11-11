import sys

from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Design_PhotoProcessing import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image.setPixmap(QPixmap('background.png'))
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.newFile)
        self.Redder.triggered.connect(self.justRed)
        self.Greener.triggered.connect(self.justGreen)
        self.Bluer.triggered.connect(self.justBlue)
        self.Negative.triggered.connect(self.nnegative)

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
        self.mainimg = Image.open(self.filename)
        self.pic = self.mainimg.copy()
        self.x, self.y = self.mainimg.size
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def newFile(self):
        self.filename = 'newFile.png'
        self.mainimg = Image.open(self.filename)
        self.pic = self.mainimg.copy()
        self.x, self.y = self.mainimg.size
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def justRed(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def justGreen(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def justBlue(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def nnegative(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
