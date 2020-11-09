# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_PhotoProcessing.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PhotoProcessingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen_File = QtWidgets.QMenu(self.menubar)
        self.menuOpen_File.setObjectName("menuOpen_File")
        self.menuFilters = QtWidgets.QMenu(self.menubar)
        self.menuFilters.setObjectName("menuFilters")
        self.menuJust_Blue = QtWidgets.QMenu(self.menuFilters)
        self.menuJust_Blue.setObjectName("menuJust_Blue")
        self.menuCurvies = QtWidgets.QMenu(self.menuFilters)
        self.menuCurvies.setObjectName("menuCurvies")
        self.menuCropper = QtWidgets.QMenu(self.menubar)
        self.menuCropper.setObjectName("menuCropper")
        self.menuShape = QtWidgets.QMenu(self.menuCropper)
        self.menuShape.setObjectName("menuShape")
        self.menuAspect_Ratio = QtWidgets.QMenu(self.menuCropper)
        self.menuAspect_Ratio.setObjectName("menuAspect_Ratio")
        self.menuFor_Social_Network = QtWidgets.QMenu(self.menuCropper)
        self.menuFor_Social_Network.setObjectName("menuFor_Social_Network")
        self.menuRotation = QtWidgets.QMenu(self.menubar)
        self.menuRotation.setObjectName("menuRotation")
        self.menuEffects = QtWidgets.QMenu(self.menubar)
        self.menuEffects.setObjectName("menuEffects")
        self.menuMasks = QtWidgets.QMenu(self.menubar)
        self.menuMasks.setObjectName("menuMasks")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSepia = QtWidgets.QAction(MainWindow)
        self.actionSepia.setObjectName("actionSepia")
        self.actionNegative = QtWidgets.QAction(MainWindow)
        self.actionNegative.setObjectName("actionNegative")
        self.actionJust_Green = QtWidgets.QAction(MainWindow)
        self.actionJust_Green.setObjectName("actionJust_Green")
        self.actionJust_Red = QtWidgets.QAction(MainWindow)
        self.actionJust_Red.setObjectName("actionJust_Red")
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionTriangle = QtWidgets.QAction(MainWindow)
        self.actionTriangle.setObjectName("actionTriangle")
        self.action16_9 = QtWidgets.QAction(MainWindow)
        self.action16_9.setObjectName("action16_9")
        self.action4_3 = QtWidgets.QAction(MainWindow)
        self.action4_3.setObjectName("action4_3")
        self.action9_16 = QtWidgets.QAction(MainWindow)
        self.action9_16.setObjectName("action9_16")
        self.actionSquare_2 = QtWidgets.QAction(MainWindow)
        self.actionSquare_2.setObjectName("actionSquare_2")
        self.actionTriangle_2 = QtWidgets.QAction(MainWindow)
        self.actionTriangle_2.setObjectName("actionTriangle_2")
        self.actionCircle = QtWidgets.QAction(MainWindow)
        self.actionCircle.setObjectName("actionCircle")
        self.action4_4 = QtWidgets.QAction(MainWindow)
        self.action4_4.setObjectName("action4_4")
        self.action16_10 = QtWidgets.QAction(MainWindow)
        self.action16_10.setObjectName("action16_10")
        self.action3_4 = QtWidgets.QAction(MainWindow)
        self.action3_4.setObjectName("action3_4")
        self.action9_17 = QtWidgets.QAction(MainWindow)
        self.action9_17.setObjectName("action9_17")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        self.action3_2.setObjectName("action3_2")
        self.actionInstagram_Stories = QtWidgets.QAction(MainWindow)
        self.actionInstagram_Stories.setObjectName("actionInstagram_Stories")
        self.actionInstagram_Stories_2 = QtWidgets.QAction(MainWindow)
        self.actionInstagram_Stories_2.setObjectName("actionInstagram_Stories_2")
        self.actionTwitter_Youtube_Header = QtWidgets.QAction(MainWindow)
        self.actionTwitter_Youtube_Header.setObjectName("actionTwitter_Youtube_Header")
        self.actionFree_Crop = QtWidgets.QAction(MainWindow)
        self.actionFree_Crop.setObjectName("actionFree_Crop")
        self.actionJust_Blue_2 = QtWidgets.QAction(MainWindow)
        self.actionJust_Blue_2.setObjectName("actionJust_Blue_2")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(MainWindow)
        self.actionRight.setObjectName("actionRight")
        self.actionFlip_from_right_to_left = QtWidgets.QAction(MainWindow)
        self.actionFlip_from_right_to_left.setObjectName("actionFlip_from_right_to_left")
        self.actionFlip_vertically = QtWidgets.QAction(MainWindow)
        self.actionFlip_vertically.setObjectName("actionFlip_vertically")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSTicker = QtWidgets.QAction(MainWindow)
        self.actionSTicker.setObjectName("actionSTicker")
        self.actionPhoto = QtWidgets.QAction(MainWindow)
        self.actionPhoto.setObjectName("actionPhoto")
        self.actionText = QtWidgets.QAction(MainWindow)
        self.actionText.setObjectName("actionText")
        self.menuOpen_File.addAction(self.actionOpen)
        self.menuOpen_File.addAction(self.actionNew)
        self.menuOpen_File.addSeparator()
        self.menuOpen_File.addAction(self.actionSave)
        self.menuOpen_File.addAction(self.actionSave_As)
        self.menuJust_Blue.addAction(self.actionJust_Red)
        self.menuJust_Blue.addAction(self.actionJust_Green)
        self.menuJust_Blue.addAction(self.actionJust_Blue_2)
        self.menuFilters.addAction(self.actionSepia)
        self.menuFilters.addAction(self.actionNegative)
        self.menuFilters.addSeparator()
        self.menuFilters.addAction(self.menuJust_Blue.menuAction())
        self.menuFilters.addAction(self.menuCurvies.menuAction())
        self.menuShape.addAction(self.actionSquare_2)
        self.menuShape.addAction(self.actionTriangle_2)
        self.menuShape.addAction(self.actionCircle)
        self.menuAspect_Ratio.addAction(self.action3_4)
        self.menuAspect_Ratio.addAction(self.action4_4)
        self.menuAspect_Ratio.addAction(self.action16_10)
        self.menuAspect_Ratio.addAction(self.action3_2)
        self.menuFor_Social_Network.addAction(self.actionInstagram_Stories_2)
        self.menuFor_Social_Network.addAction(self.actionTwitter_Youtube_Header)
        self.menuCropper.addAction(self.menuShape.menuAction())
        self.menuCropper.addAction(self.menuAspect_Ratio.menuAction())
        self.menuCropper.addAction(self.menuFor_Social_Network.menuAction())
        self.menuCropper.addSeparator()
        self.menuCropper.addAction(self.actionFree_Crop)
        self.menuRotation.addAction(self.actionLeft)
        self.menuRotation.addAction(self.actionRight)
        self.menuRotation.addAction(self.actionFlip_from_right_to_left)
        self.menuRotation.addAction(self.actionFlip_vertically)
        self.menuEffects.addAction(self.action_4)
        self.menuMasks.addAction(self.action_5)
        self.menuAdd.addAction(self.actionSTicker)
        self.menuAdd.addAction(self.actionPhoto)
        self.menuAdd.addAction(self.actionText)
        self.menubar.addAction(self.menuOpen_File.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuCropper.menuAction())
        self.menubar.addAction(self.menuRotation.menuAction())
        self.menubar.addAction(self.menuEffects.menuAction())
        self.menubar.addAction(self.menuMasks.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "File"))
        self.menuFilters.setTitle(_translate("MainWindow", "Filters"))
        self.menuJust_Blue.setTitle(_translate("MainWindow", "Colors"))
        self.menuCurvies.setTitle(_translate("MainWindow", "Curvies"))
        self.menuCropper.setTitle(_translate("MainWindow", "Cropper"))
        self.menuShape.setTitle(_translate("MainWindow", "Shape"))
        self.menuAspect_Ratio.setTitle(_translate("MainWindow", "Aspect Ratio"))
        self.menuFor_Social_Network.setTitle(_translate("MainWindow", "For Social Network"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation"))
        self.menuEffects.setTitle(_translate("MainWindow", "Effects"))
        self.menuMasks.setTitle(_translate("MainWindow", "Masks"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menu.setTitle(_translate("MainWindow", "/вероятно это не все/"))
        self.actionSepia.setText(_translate("MainWindow", "Sepia"))
        self.actionNegative.setText(_translate("MainWindow", "Negative"))
        self.actionJust_Green.setText(_translate("MainWindow", "Just Green"))
        self.actionJust_Red.setText(_translate("MainWindow", "Just Red"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionTriangle.setText(_translate("MainWindow", "Triangle"))
        self.action16_9.setText(_translate("MainWindow", "16:9"))
        self.action4_3.setText(_translate("MainWindow", "4:3"))
        self.action9_16.setText(_translate("MainWindow", "9:16"))
        self.actionSquare_2.setText(_translate("MainWindow", "Square"))
        self.actionTriangle_2.setText(_translate("MainWindow", "Triangle"))
        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.action4_4.setText(_translate("MainWindow", "4:3"))
        self.action16_10.setText(_translate("MainWindow", "16:9"))
        self.action3_4.setText(_translate("MainWindow", "3:4"))
        self.action9_17.setText(_translate("MainWindow", "9:16"))
        self.action3_2.setText(_translate("MainWindow", "3:2"))
        self.actionInstagram_Stories.setText(_translate("MainWindow", "Instagram Stories"))
        self.actionInstagram_Stories_2.setText(_translate("MainWindow", "Instagram Stories"))
        self.actionTwitter_Youtube_Header.setText(_translate("MainWindow", "Twitter/Youtube Header"))
        self.actionFree_Crop.setText(_translate("MainWindow", "Free Crop"))
        self.actionJust_Blue_2.setText(_translate("MainWindow", "Just Blue"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionFlip_from_right_to_left.setText(_translate("MainWindow", "Flip Horizontally"))
        self.actionFlip_vertically.setText(_translate("MainWindow", "Flip Vertically"))
        self.action_4.setText(_translate("MainWindow", "/буду дополнять и пополнять/"))
        self.action_5.setText(_translate("MainWindow", "/дополнять/"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSTicker.setText(_translate("MainWindow", "Sticker"))
        self.actionPhoto.setText(_translate("MainWindow", "Photo"))
        self.actionText.setText(_translate("MainWindow", "Text"))
