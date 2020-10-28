from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
# Импортировали все нужное

from Models.Design_MP3Player import Ui_MP3PlayerWindow  # Импортируем наш дизайн


def hoursHours_minutesMinutes_secondsSeconds(milliseconds):  # Метод для преобразования времени в миллисекундах
    """"Используем divmod, который возвращает пару частное-остаток от деления аргументов для получения секунд"""
    # seconds = 1000
    # minutes = 60000
    # hours = 3600000
    seconds = round(milliseconds / 1000)  # Переводим миллисекунды в секунды
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return ("%d:%02d:%02d" % (hours, minutes, seconds)) if hours else ("%d:%02d" % (minutes, seconds))  # Подправить


class ViewerWindow(QMainWindow):  # Создаем класс для просмотра видео
    state = pyqtSignal(bool)

    """"Добавляем метод close Event для обновления кнопки переключения, 
    при этом отменяя ее поведение по умолчанию, которая
    закрывает окно, она не закроет его, а просто скроет"""

    def closeEvent(self, e):
        # Выводим состояние окна, чтобы обновить кнопку переключения средства просмотра.
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):  # Создаем класс модели плейлиста
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле Design_MP3Player.py
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    """"Метод d_data, который возвращает данные для определенной строки,
    в этом случае мы отображаем только имя файла"""

    def d_data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    """"Метод count_of_row для возврата общего количества строк в
    списке воспроизведения через mediaCount()"""

    def count_of_row(self, index):
        return self.playlist.mediaCount()
