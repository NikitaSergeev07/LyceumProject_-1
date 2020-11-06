import sys
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

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
        self.pixmap = QPixmap(filename)
        self.image.setPixmap(self.pixmap)
        self.image = QLabel(self)
        self.image.move(0, 23)
        im = Image.open(str(self.filename))
        z, a = im.size
        self.image.resize(z, a)

    def newFile(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
