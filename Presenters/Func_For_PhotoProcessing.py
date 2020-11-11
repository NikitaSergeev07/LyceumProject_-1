import sys

from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Models.Design_PhotoProcessing import Ui_PhotoProcessingWindow


class PhotoProcessing_Window(QMainWindow, Ui_PhotoProcessingWindow):
    def __init__(self):
        super().__init__()
        self.coefficient = 0
        self.setupUi(self)
        self.image.setPixmap(QPixmap('background.png'))
        self.actionOpen.triggered.connect(self.openFile)
        self.actionNew.triggered.connect(self.newFile)
        self.Redder.triggered.connect(self.justRed)
        self.Greener.triggered.connect(self.justGreen)
        self.Bluer.triggered.connect(self.justBlue)
        self.Negative.triggered.connect(self.nnegative)
        self.All.triggered.connect(self.all)
        self.actionCurvies.triggered.connect(self.Inbright)
        self.BnW.triggered.connect(self.blwh)
        self.Sepia.triggered.connect(self.sepiit)
        self.actionGray_Skale.triggered.connect(self.gray_scale)
        self.actionContrast.triggered.connect(self.contrast)
        self.actionSquare_2.triggered.connect(self.crop_square)

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
        self.mainimg = Image.open(self.filename)
        self.pic = self.mainimg.copy()
        self.x, self.y = self.mainimg.size
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def newFile(self):
        try:
            self.filename = 'newFile.png'
            self.mainimg = Image.open(self.filename)
            self.pic = self.mainimg.copy()
            self.x, self.y = self.mainimg.size
            self.pic.save('freeFile.png')
            self.image.setPixmap(QPixmap('freeFile.png'))
        except BaseException:
            print("Что-то пошло не так")

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

    def all(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def nnegative(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 256 - r, 256 - g, 256 - b
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def Inbright(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                pixels[i, j] = curve(pixels[i, j])

    def blwh(self):
        brightness, ok = QInputDialog.getInt(self, "Input Brightness", 'What brightness do you want to use?', 2, 1, 15,
                                             1)
        separator = 255 / brightness / 2 * 3
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                total = r + g + b
                if total > separator:
                    self.pic.putpixel((i, j), (255, 255, 255))
                else:
                    self.pic.putpixel((i, j), (0, 0, 0))
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def sepiit(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                red = int(r * 0.393 + g * 0.769 + b * 0.189)
                green = int(r * 0.349 + g * 0.686 + b * 0.168)
                blue = int(r * 0.272 + g * 0.534 + b * 0.131)
                self.pic.putpixel((i, j), (red, green, blue))
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def gray_scale(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                self.pic.putpixel((i, j), (gray, gray, gray))
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))

    def contrast(self, value):
        self.Slider.setVisible(True)
        self.Slider.valueChanged[int].connect(self.contrast2)
        if value:
            self.coefficient = int(value) % 10

    def contrast2(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()

        avg = 0
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= self.pic.size[0] * self.pic.size[1]

        palette = []
        for i in range(256):
            temp = int(avg + self.coefficient * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                self.pic.putpixel((i, j), (palette[r], palette[g], palette[b]))
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.Slider.setVisible(False)

    def crop_square(self):
        self.pic = self.mainimg.copy()
        self.pic = self.pic.crop((177, 882, 1179, 1707))
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))


def curve(pixel):
    r, g, b = pixel
    brightness = r + g + b
    if brightness < 60:
        k = 60 / (brightness + 1)
        return min(255, int(r * k ** 2)), \
               min(255, int(g * k ** 2)), \
               min(255, int(b * k ** 2))
    else:
        return r, g, b


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PhotoProcessing_Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
