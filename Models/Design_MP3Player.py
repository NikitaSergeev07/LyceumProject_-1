# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_MP3Player.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MP3PlayerWindow(object):
    def setupUi(self, MP3PlayerWindow):
        MP3PlayerWindow.setObjectName("MP3PlayerWindow")
        MP3PlayerWindow.resize(484, 371)
        self.centralWidget = QtWidgets.QWidget(MP3PlayerWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout.addWidget(self.playlistView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeIcon = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeIcon.setMinimumSize(QtCore.QSize(80, 0))
        self.currentTimeIcon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTimeIcon.setObjectName("currentTimeIcon")
        self.horizontalLayout_4.addWidget(self.currentTimeIcon)
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)
        self.totalTimeIcon = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeIcon.setMinimumSize(QtCore.QSize(80, 0))
        self.totalTimeIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeIcon.setObjectName("totalTimeIcon")
        self.horizontalLayout_4.addWidget(self.totalTimeIcon)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/control-skip-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/control-stop-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/control-skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        self.viewButton = QtWidgets.QPushButton(self.centralWidget)
        self.viewButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/application-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(True)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)
        self.volumeicon = QtWidgets.QLabel(self.centralWidget)
        self.volumeicon.setText("")
        self.volumeicon.setPixmap(QtGui.QPixmap("../images/speaker-volume.png"))
        self.volumeicon.setObjectName("volumeicon")
        self.horizontalLayout_5.addWidget(self.volumeicon)
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MP3PlayerWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MP3PlayerWindow)
        self.statusBar.setObjectName("statusBar")
        MP3PlayerWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MP3PlayerWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 484, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        MP3PlayerWindow.setMenuBar(self.menuBar)
        self.open_file_action = QtWidgets.QAction(MP3PlayerWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.menuFIle.addAction(self.open_file_action)
        self.menuBar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MP3PlayerWindow)
        QtCore.QMetaObject.connectSlotsByName(MP3PlayerWindow)

    def retranslateUi(self, MP3PlayerWindow):
        _translate = QtCore.QCoreApplication.translate
        MP3PlayerWindow.setWindowTitle(_translate("MP3PlayerWindow", "MP3Player"))
        self.currentTimeIcon.setText(_translate("MP3PlayerWindow", "0:00"))
        self.totalTimeIcon.setText(_translate("MP3PlayerWindow", "0:00"))
        self.menuFIle.setTitle(_translate("MP3PlayerWindow", "FIle"))
        self.open_file_action.setText(_translate("MP3PlayerWindow", "Open file..."))
