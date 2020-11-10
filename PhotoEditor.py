import io
import sys
from PIL import Image, ImageOps, Image
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('supadesign.ui', self)
        self.Slider.setVisible(False)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.newFile)
        self.actionJust_Red.triggered.connect(self.justRed)

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
        self.freeimg = self.filename
        self.pixmap = QPixmap(self.filename)
        self.image.setPixmap(self.pixmap)

    def newFile(self):
        self.filename = 'newFile.png'
        self.pixmap = QPixmap(self.filename)
        self.image.setPixmap(self.pixmap)

    def justRed(self):
        img = QImage(self.filename)
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_img = Image.open(io.BytesIO(buffer.data()))
        pixels = pil_img.load()
        x, y = pil_img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        img.save(self.freeimg)
        self.pixmap = QPixmap(self.freeimg)
        self.image.setPixmap(self.pixmap)

    def justGreen(self):
        img = QImage(self.filename)
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_img = Image.open(io.BytesIO(buffer.data()))
        pixels = pil_img.load()
        x, y = pil_img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img.save(self.freeimg)
        self.pixmap = QPixmap(self.freeimg)
        self.image.setPixmap(self.pixmap)

    def justBlue(self):
        img = QImage(self.filename)
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_img = Image.open(io.BytesIO(buffer.data()))
        pixels = pil_img.load()
        x, y = pil_img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        img.save(self.filename)
        self.pixmap = QPixmap(self.filename)
        self.image.setPixmap(QtGui.QPixmap(self.filename))

    def Negative(self):
        img = QImage(self.filename)
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_img = Image.open(io.BytesIO(buffer.data()))
        pil_img = PIL.ImageOps.invert(pil_img)
        self.pixmap = QPixmap(self.pil_img)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
