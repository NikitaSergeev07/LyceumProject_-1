# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e;\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 801, 301))
        self.Header.setStyleSheet("background-color: #fb5b5d;\n"
                                  "")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.Tittle_MainWindow = QtWidgets.QLabel(self.Header)
        self.Tittle_MainWindow.setGeometry(QtCore.QRect(170, 20, 451, 58))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Tittle_MainWindow.setFont(font)
        self.Tittle_MainWindow.setStyleSheet("color: white;\n"
                                             "")
        self.Tittle_MainWindow.setObjectName("Tittle_MainWindow")
        self.Image_MainWindow = QtWidgets.QLabel(self.Header)
        self.Image_MainWindow.setGeometry(QtCore.QRect(100, 90, 621, 201))
        self.Image_MainWindow.setText("")
        self.Image_MainWindow.setPixmap(QtGui.QPixmap("images/MusicalNote.jpg"))
        self.Image_MainWindow.setObjectName("Image_MainWindow")
        self.btn_MP3Player = QtWidgets.QPushButton(self.centralwidget)
        self.btn_MP3Player.setGeometry(QtCore.QRect(90, 380, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setPointSize(14)
        font.setItalic(False)
        self.btn_MP3Player.setFont(font)
        self.btn_MP3Player.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_MP3Player.setStyleSheet("QPushButton {\n"
                                         "    background-color: #fb5b5d;\n"
                                         "    border-radius: 8px;    \n"
                                         "    border: 2px solid #960631;\n"
                                         "    color: white\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: #fa4244\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         " \n"
                                         "")
        self.btn_MP3Player.setObjectName("btn_MP3Player")
        self.btn_PhotoProcessing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_PhotoProcessing.setGeometry(QtCore.QRect(310, 380, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setPointSize(14)
        font.setItalic(False)
        self.btn_PhotoProcessing.setFont(font)
        self.btn_PhotoProcessing.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_PhotoProcessing.setStyleSheet("QPushButton {\n"
                                               "    background-color: #fb5b5d;\n"
                                               "    border-radius: 8px;    \n"
                                               "    border: 2px solid #960631;\n"
                                               "    color: white\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed{\n"
                                               "    background-color: #fa4244\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               " \n"
                                               "")
        self.btn_PhotoProcessing.setObjectName("btn_PhotoProcessing")
        self.btn_AudioAndVideoProcessing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_AudioAndVideoProcessing.setGeometry(QtCore.QRect(530, 380, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Humnst777 BlkCn BT")
        font.setPointSize(14)
        font.setItalic(False)
        self.btn_AudioAndVideoProcessing.setFont(font)
        self.btn_AudioAndVideoProcessing.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_AudioAndVideoProcessing.setStyleSheet("QPushButton {\n"
                                                       "    background-color: #fb5b5d;\n"
                                                       "    border-radius: 8px;    \n"
                                                       "    border: 2px solid #960631;\n"
                                                       "    color: white\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:pressed{\n"
                                                       "    background-color: #fa4244\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       " \n"
                                                       "")
        self.btn_AudioAndVideoProcessing.setObjectName("btn_AudioAndVideoProcessing")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tittle_MainWindow.setText(_translate("MainWindow", "The Future Programm"))
        self.btn_MP3Player.setText(_translate("MainWindow", "MP3Player"))
        self.btn_PhotoProcessing.setText(_translate("MainWindow", "PhotoProcessing"))
        self.btn_AudioAndVideoProcessing.setText(_translate("MainWindow", "AudioAndVideoProcessing"))