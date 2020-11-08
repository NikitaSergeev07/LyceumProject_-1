import sys
import io
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PIL import Image



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('supadesign.ui', self)
        self.current = 'newFile.png'
        self.pixmap = QPixmap(self.current)
        self.image = QLabel(self)
        self.image.move(0, 23)
        img = Image.open(self.current)
        x, y = img.size
        self.image.resize(x, y)
        self.image.setPixmap(self.pixmap)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.newFile)
        self.actionJust_Red.triggered.connect(self.justRed)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
        self.pixmap = QPixmap(filename)
        self.image.setPixmap(self.pixmap)
        self.image = QLabel(self)
        self.image.move(0, 23)

    def newFile(self):
        pass

    def justRed(self):
        img = Image.open(self.filename)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.image.setPixmap(self.pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
