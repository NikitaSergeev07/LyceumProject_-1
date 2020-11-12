import sys
import sqlite3
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

from Models.Design_PhotoProcessing import Ui_PhotoProcessingWindow


class PhotoProcessing_Window(QMainWindow, Ui_PhotoProcessingWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 200)
        self.coefficient = 0
        self.setupUi(self)
        self.Slider.setVisible(False)
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
        self.Sepia.triggered.connect(self.sepi_it)
        self.gray_skale.triggered.connect(self.gray_scale)
        self.acontrast.triggered.connect(self.contrast)
        self.a11.triggered.connect(self.crop_square)
        self.a169.triggered.connect(self.crop_rect)
        self.a34.triggered.connect(self.crop_r34)
        self.a43.triggered.connect(self.crop_r43)
        self.a23.triggered.connect(self.crop_r23)
        self.a32.triggered.connect(self.crop_r32)
        self.actionLeft.triggered.connect(self.rotate_left)
        self.actionRight.triggered.connect(self.rotate_right)
        self.aFlipHor.triggered.connect(self.flip_hor)
        self.aFlipVert.triggered.connect(self.flip_vert)
        self.actionSave.triggered.connect(self.saver)

    def openFile(self):
        try:
            self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '')[0]
            # Импорт библиотеки

            # Подключение к БД
            self.con = sqlite3.connect("Presenters/photo.db")

            # Создание курсора
            self.cur = self.con.cursor()
            self.path = os.path.basename(self.filename)
            self.name = self.filename[0:self.filename.rfind('.')]
            self.full_name = self.filename[0:]
            self.result = self.cur.execute(
                f"INSERT INTO photo (name, full_name, path) VALUES ('{self.name}', '{self.full_name}', '{self.path}')").fetchall()
            self.con.commit()
            self.con.close()

        except BaseException:
            print("Выберите изображение!")
        self.mainimg = Image.open(self.filename)
        self.pic = self.mainimg.copy()
        self.x, self.y = self.mainimg.size
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(self.x, self.y)
        self.setGeometry(100, 100, self.x + 20, self.y + 20)
        self.saver()

    def newFile(self):
        try:
            self.filename = 'newFile.png'
            self.mainimg = Image.open(self.filename)
            self.pic = self.mainimg.copy()
            self.x, self.y = self.mainimg.size
            self.pic.save('freeFile.png')
            self.image.setPixmap(QPixmap('freeFile.png'))
            self.saver()
        except BaseException:
            print("Что-то пошло не так!")

    def justRed(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.saver()

    def justGreen(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.saver()

    def justBlue(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.saver()

    def all(self):
        try:
            self.pic = self.mainimg.copy()
            pixels = self.pic.load()
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = r, g, b
            self.pic.save('freeFile.png')
            self.image.setPixmap(QPixmap('freeFile.png'))
            self.saver()
        except Exception:
            print("Что-то пошло не так!")

    def nnegative(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 256 - r, 256 - g, 256 - b
        self.pic.save('freeFile.png')
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.saver()

    def Inbright(self):
        self.pic = self.mainimg.copy()
        pixels = self.pic.load()
        for i in range(self.x):
            for j in range(self.y):
                pixels[i, j] = curve(pixels[i, j])
        self.saver()

    def blwh(self):
        try:
            brightness, ok = QInputDialog.getInt(self, "Input Brightness", 'What brightness do you want to use?', 2, 1,
                                                 15,
                                                 1)
            if ok:
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
            self.saver()
        except Exception:
            print("Что-то пошло не так!")

    def sepi_it(self):
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
        self.saver()

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
        self.saver()

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
        self.saver()

    def crop_square(self):
        try:
            self.pic = self.mainimg.copy()
            if self.x / self.y > 1:
                x1 = int(self.x / 2 - self.y / 2)
                y1 = int(self.x / 2 + self.y / 2)
                pic2 = self.pic.crop((x1, 0, y1, self.y))
            elif self.x / self.y < 1:
                x1 = int(self.y / 2 - self.x / 2)
                y1 = int(self.y / 2 + self.x / 2)
                pic2 = self.pic.crop((0, x1, self.x, y1))
            else:
                pic2 = self.pic.copy()
            pic2.save('freeFile.png')
            x, y = pic2.size
            self.image.setPixmap(QPixmap('freeFile.png'))
            self.image.resize(x, y)
            self.saver()
        except Exception:
            print("Что-то пошло не так!")

    def crop_rect(self):
        try:
            self.pic = self.mainimg.copy()
            x1 = 0
            y1 = 0
            if self.x / self.y > 16 / 9:
                x1 = int(self.x / 2 - (8 * self.y / 9))
                y1 = int(self.x / 2 + (8 * self.y / 9))
            elif self.x / self.y < 16 / 9:
                x1 = int(self.y / 2 - (9 * self.x / 32))
                y1 = int(self.y / 2 + (9 * self.x / 32))
            new_size = (x1, y1)
            ratio = min(float(new_size[0]) / self.x, float(new_size[1]) / self.y)
            x2 = int(400 * self.x * ratio)
            y2 = int(400 * self.y * ratio)
            x = int(self.x / 2 - x2 / 2)
            xy = int(self.x / 2 + x2 / 2)
            yx = int(self.y / 2 - y2 / 2)
            y = int(self.y / 2 + y2 / 2)
            if x1 and y1:
                pic2 = self.pic.crop((x, yx, xy, y))
            else:
                pic2 = self.pic.copy()
            pic2.save('freeFile.png')
            x, y = pic2.size
            self.image.setPixmap(QPixmap('freeFile.png'))
            self.image.resize(x, y)
            self.saver()
        except BaseException:
            print('что-то пошло не так!')

    def crop_r34(self):
        try:
            self.pic = self.mainimg.copy()
            x1 = 0
            y1 = 0
            if self.x / self.y > 3 / 4:
                x1 = int(self.x / 2 - (3 * self.y / 8))
                y1 = int(self.x / 2 + (3 * self.y / 8))
            elif self.x / self.y < 3 / 4:
                x1 = int(self.y / 2 - (2 * self.x / 3))
                y1 = int(self.y / 2 + (2 * self.x / 3))
            new_size = (x1, y1)
            ratio = min(float(new_size[0]) / self.x, float(new_size[1]) / self.y)
            x2 = int(3 * self.x * ratio)
            y2 = int(3 * self.y * ratio)
            x = int(self.x / 2 - x2 / 2)
            xy = int(self.x / 2 + x2 / 2)
            yx = int(self.y / 2 - y2 / 2)
            y = int(self.y / 2 + y2 / 2)
            if x1 and y1:
                pic2 = self.pic.crop((x, yx, xy, y))
            else:
                pic2 = self.pic.copy()
            pic2.save('freeFile.png')
            x, y = pic2.size
            self.image.setPixmap(QPixmap('freeFile.png'))
            self.image.resize(x, y)
            self.saver()
        except Exception:
            print("Что-то пошло не так!")

    def crop_r43(self):
        self.pic = self.mainimg.copy()
        x1 = 0
        y1 = 0
        if self.x / self.y > 4 / 3:
            x1 = int(self.x / 2 - (2 * self.y / 3))
            y1 = int(self.x / 2 + (2 * self.y / 3))
        elif self.x / self.y < 4 / 3:
            x1 = int(self.y / 2 - (3 * self.x / 8))
            y1 = int(self.y / 2 + (3 * self.x / 8))
        new_size = (x1, y1)
        ratio = min(float(new_size[0]) / self.x, float(new_size[1]) / self.y)
        x2 = int(3 * self.x * ratio)
        y2 = int(3 * self.y * ratio)
        x = int(self.x / 2 - x2 / 2)
        xy = int(self.x / 2 + x2 / 2)
        yx = int(self.y / 2 - y2 / 2)
        y = int(self.y / 2 + y2 / 2)
        if x1 and y1:
            pic2 = self.pic.crop((x, yx, xy, y))
        else:
            pic2 = self.pic.copy()
        pic2.save('freeFile.png')
        x, y = pic2.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def crop_r23(self):
        self.pic = self.mainimg.copy()
        x1 = 0
        y1 = 0
        if self.x / self.y > 2 / 3:
            x1 = int(self.x / 2 - (self.y / 3))
            y1 = int(self.x / 2 + (self.y / 3))
        elif self.x / self.y < 2 / 3:
            x1 = int(self.y / 2 - (3 * self.x / 4))
            y1 = int(self.y / 2 + (3 * self.x / 4))
        new_size = (x1, y1)
        ratio = min(float(new_size[0]) / self.x, float(new_size[1]) / self.y)
        x2 = int(3 * self.x * ratio)
        y2 = int(3 * self.y * ratio)
        x = int(self.x / 2 - x2 / 2)
        xy = int(self.x / 2 + x2 / 2)
        yx = int(self.y / 2 - y2 / 2)
        y = int(self.y / 2 + y2 / 2)
        if x1 and y1:
            pic2 = self.pic.crop((x, yx, xy, y))
        else:
            pic2 = self.pic.copy()
        pic2.save('freeFile.png')
        x, y = pic2.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def crop_r32(self):
        self.pic = self.mainimg.copy()
        x1 = 0
        y1 = 0
        if self.x / self.y > 2 / 3:
            x1 = int(self.x / 2 - (3 * self.y / 4))
            y1 = int(self.x / 2 + (3 * self.y / 4))
        elif self.x / self.y < 2 / 3:
            x1 = int(self.y / 2 - (self.x / 3))
            y1 = int(self.y / 2 + (self.x / 3))
        new_size = (x1, y1)
        ratio = min(float(new_size[0]) / self.x, float(new_size[1]) / self.y)
        x2 = int(7 * self.x * ratio)
        y2 = int(7 * self.y * ratio)
        x = int(self.x / 2 - x2 / 2)
        xy = int(self.x / 2 + x2 / 2)
        yx = int(self.y / 2 - y2 / 2)
        y = int(self.y / 2 + y2 / 2)
        if x1 and y1:
            pic2 = self.pic.crop((x, yx, xy, y))
        else:
            pic2 = self.pic.copy()
        pic2.save('freeFile.png')
        x, y = pic2.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def rotate_left(self):
        self.pic = self.mainimg.copy()
        self.pic = self.pic.transpose(Image.ROTATE_90)
        self.pic.save('freeFile.png')
        x, y = self.pic.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def rotate_right(self):
        self.pic = self.mainimg.copy()
        self.pic = self.pic.transpose(Image.ROTATE_270)
        self.pic.save('freeFile.png')
        x, y = self.pic.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def flip_vert(self):
        self.pic = self.mainimg.copy()
        self.pic = self.pic.transpose(Image.FLIP_LEFT_RIGHT)
        self.pic.save('freeFile.png')
        x, y = self.pic.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def flip_hor(self):
        self.pic = self.mainimg.copy()
        self.pic = self.pic.transpose(Image.FLIP_TOP_BOTTOM)
        self.pic.save('freeFile.png')
        x, y = self.pic.size
        self.image.setPixmap(QPixmap('freeFile.png'))
        self.image.resize(x, y)
        self.saver()

    def saver(self):
        self.mainimg = self.pic.copy()


def curve(pixel):
    try:
        r, g, b = pixel
        brightness = r + g + b
        if brightness < 60:
            k = 60 / (brightness + 1)
            return min(255, int(r * k ** 2)), \
                   min(255, int(g * k ** 2)), \
                   min(255, int(b * k ** 2))
        else:
            return r, g, b
    except BaseException:
        print("Что-то пошло не так!")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PhotoProcessing_Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
