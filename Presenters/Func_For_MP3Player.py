import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *

from Models.Design_MP3Player import Ui_MP3PlayerWindow  # Импортируем наш дизайн


# Импортировали все модули из PyQt5


def hoursHours_minutesMinutes_secondsSeconds(milliseconds: int) -> int:  # Функция для преобразования времени в миллисекунды
    """"Используем divmod, который возвращает частное и остаток от деления аргументов для получения миллисекунд"""
    # Комментарии, для понимания сколько в секундах, минутах и часах содержится миллисекунд
    # seconds = 1000
    # minutes = 60000
    # hours = 3600000
    seconds = round(milliseconds / 1000)  # Переводим миллисекунды в секунды
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    # Возвращаем количество времени с начала воспроизведения композиции
    return ("%d:%02d:%02d" % (hours, minutes, seconds)) if hours else ("%d:%02d" % (minutes, seconds))


""""Создаем функцию для проверки расширения файла"""


def check_ext(path: str) -> bool:
    _, ext = os.path.splitext(path)
    if ext not in (".mp3", ".mp4", ".mov"):  # Проверяем расширения mp3, mp4, mov
        raise ValueError()


class ViewerWindow(QMainWindow):  # Создаем класс для просмотра видео
    state = pyqtSignal(bool)

    """"Добавляем метод close Event для обновления кнопки переключения, 
    при этом отменяя ее поведение по умолчанию, которая
    закрывает окно, она не закроет его, а просто скроет"""

    def closeEvent(self, e):
        # Выводим состояние окна, чтобы обновить кнопку переключения средства просмотра.
        self.state.emit(False)

    # Пытаемся подключить стили к нашему приложению
    try:
        app = QApplication([])
        # Имя окна просмотра видео
        app.setApplicationName("MP4Player")
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    # Навсякий случай, сделаем исключение для непредвиденных ошибок
    except BaseException:
        print("Что-то пошло не так!")


class PlaylistModel(QAbstractListModel):  # Создаем класс модели плейлиста
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле Func_For_MP3Player.py
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    """"Метод data, который возвращает данные для определенной строки,
    в этом случае мы отображаем только имя файла"""

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    """"Метод rowCount для возврата общего количества строк в
    списке воспроизведения через mediaCount()"""

    def rowCount(self, parent=None, *args, **kwargs):
        return self.playlist.mediaCount()


class MP3_MainWindow(QMainWindow, Ui_MP3PlayerWindow):  # Создаем класс главного окна MP3Player
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле Func_For_MP3Player.py
    def __init__(self, *args, **kwargs):
        super(MP3_MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.player = QMediaPlayer()

        self.player.error.connect(self.erroralert)  # Обработчик ошибок, подключенный к сигналу ошибки self.erroralert
        self.player.play()

        # Список воспроизведения может быть передан проигрывателю
        # Он может использовать его для автоматического выбора дорожки для воспроизведения
        # После завершения текущей.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        """"Добавляем просмотр видео, если не добавить это, то будет проигрываться только аудио, но не видео"""

        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))
        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        """"Все общие элементы управления медиаплеером
            могут быть подключены к проигрывателю напрямую,
            используя self.player"""

        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)

        """"self.volumeSlider для регулировки громкости
            и self.timeSlider для положения ползунка времени"""

        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        """"Включаем или квыключаем переключатели, чтобы user мог видеть или скрывать воспроизведение"""

        self.viewButton.toggled.connect(self.toggle_viewer)
        self.viewer.state.connect(self.viewButton.setChecked)

        """"Кнопки self.previousButton и self.nextButton подключены к методам воспроизведения
        и выполняют перезапуск возврат и переход на следующую композицию,
        Поскольку метод воспроизведения подключен к проигрывателю,
        это позволяет автоматически запускать плеер для воспроизведения композиции"""

        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)

        """"Это Модель плейлиста для получения данных из
         QMediaPlaylist и отображения их на представление
         Мы создаем экземпляр модели и передаем его нашему представлению."""

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        """"Подключаем методы отображения таймера к данному моменту воспроизведения,
        это позволяет нам автоматически обновлять отображение при изменении позиции воспроизведения"""

        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)

        """"Мы имеем файловую операцию, это 
        открытие файла, она добавляет файл в список произведений для воспроизведения,
        но также мы принимаем drag_and_drop(перетаскивание композиции)"""

        self.open_file_action.triggered.connect(self.open_file)
        self.setAcceptDrops(True)

        self.show()  # Воспроизводим GUI приложения на экран

    """"В методе dragEnterEvent проверяется,
    является ли объект,который мы перетащили файлом (по пути до файла)"""

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    """"Метод dropEvent перебирает URL-адреса в предоставленных данных
    и добавляет их в список воспроизведения,
    если мы не воспроизводим композицию, при удалении файла запускается автовоспроизведение только,
    что добавленного файла"""

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        # Если ничего не воспроизводится, то ищется первая композиция из вновь добавленных и проигрывается
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()

    """"Создаем метод для открытия файлов,
    который добавит его в текущий список воспроизведения"""

    def open_file(self):
        # Вытаскиваем путь до файла
        path, h = QFileDialog.getOpenFileName(self, "Open file", "",  # Определяем форматы, который поддерживает плеер
                                              "mp3 Audio (*.mp3);mp4 Video (*.mp4);Movie files (*.mov);All files (*.*)")
        try:  # Проверяем расширение файла
            check_ext(path)
            self.playlist.addMedia(QMediaContent
                                   (QUrl.fromLocalFile(path)
                                    )
                                   )

            # f = os.path.basename(path)
            # print(f[0:f.rfind('.')]) Имя песни без расширения
            # f = os.path.basename(i)
            # print(f[0:]) Имя песни с расширением

        except ValueError:
            self.log = Log()  # Если расширение не соотвествует стандарту нашей программы
            self.log.show()  # Выводим окно с поясняющим текстом

        self.model.layoutChanged.emit()

    """"Создаем метод для считывания, на каком моменте воспроизведения мы находимся,
    а также обновляем ползунок, когда например происходит переход к следующей композиции"""

    def update_duration(self, duration):
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(hoursHours_minutesMinutes_secondsSeconds(duration))

    """"Создаем метод для обновления положение ползунка,
    мы хотим обновлять ползунок по мере продвижения дорожки,
    однако обновление ползунка запускает обновление позиции, 
    чтобы пользователь мог перетащить на позицию на дорожке,
    это может вызвать бесконечный цикл, поэтому
    чтобы обойти это, мы блокируем сигналы, пока делаем обновление ползунка, и снова включаем после"""

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hoursHours_minutesMinutes_secondsSeconds(position))

        # Отключаем события, чтобы предотвратить запуск обновления события, ведь могут произойти непредвиденные ошибки
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    """"Создаем метод для обновления композиции в списке воспроизведений, которую выбрал user"""

    def playlist_selection_changed(self, ix):
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    """"Обновляем выделение в списке воспроизведения по мере движения композиции
    мы проверяем -1, так как это значение отправляется списком воспроизведения,
    когда композиций для воспроизведения больше нет, то либо мы находимся в конце списка воспроизведения,
    либо список воспроизведения пуст"""

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    """"Создаем метод для просмотра видео,
    если окно присутствует показываем его,
    в ином случае скрываем окно"""

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    """"Метод для обработки сигнала ошибки"""

    def erroralert(self, *args):
        print(args)


""""Создаем класс для диалогового окна, для неверного расширение файла"""


class Log(QDialog):
    # Это здесь нужно для доступа к переменным, методам
    # и т.д. в файле Func_For_MP3Player.py
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 300, 220, 50)  # Размеры окна и положение окна
        self.setWindowTitle('Extention Error')  # Заголовок окна

        """"Создаем label logtext, который выводит юзеру, что он выбрал не то расширение"""

        self.logtext = QLabel(self)
        self.logtext.move(10, 10)
        self.logtext.setText("Выбрано неверное расширение файла")
        self.logtext.setEnabled(False)


if __name__ == '__main__':
    app = QApplication([])
    # Имя окна просмотра видео
    app.setApplicationName("MP4Player")
    app.setStyle("Fusion")

    # Набросали пару стилей для дизайна приложения
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = MP3_MainWindow()
    app.exec_()
