# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 736)
        self.mainwindowtitle = QWidget(MainWindow)
        self.mainwindowtitle.setObjectName(u"mainwindowtitle")
        self.verticalLayout = QVBoxLayout(self.mainwindowtitle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleframe = QFrame(self.mainwindowtitle)
        self.titleframe.setObjectName(u"titleframe")
        self.titleframe.setMaximumSize(QSize(16777215, 100))
        self.titleframe.setStyleSheet(u"background-color: rgb(0, 159, 238);")
        self.titleframe.setFrameShape(QFrame.Shape.Box)
        self.titleframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.titleframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.titleframe)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"font: 600 40pt \"Barlow Condensed SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)


        self.verticalLayout.addWidget(self.titleframe)

        self.bgframe = QFrame(self.mainwindowtitle)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.bgframe.setFrameShape(QFrame.Shape.Box)
        self.bgframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftframe = QFrame(self.bgframe)
        self.leftframe.setObjectName(u"leftframe")
        self.leftframe.setMaximumSize(QSize(400, 16777215))
        self.leftframe.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.leftframe.setFrameShape(QFrame.Shape.Box)
        self.leftframe.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.leftframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonframe = QFrame(self.leftframe)
        self.buttonframe.setObjectName(u"buttonframe")
        self.buttonframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.buttonframe.setFrameShape(QFrame.Shape.Box)
        self.buttonframe.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.buttonframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.startbutton = QPushButton(self.buttonframe)
        self.startbutton.setObjectName(u"startbutton")
        self.startbutton.setStyleSheet(u"background-color: rgb(0, 159, 238);\n"
"color: rgb(255, 255, 255);\n"
"font: 600 30pt \"Barlow SemiBold\";")

        self.verticalLayout_4.addWidget(self.startbutton)

        self.stopbutton = QPushButton(self.buttonframe)
        self.stopbutton.setObjectName(u"stopbutton")
        self.stopbutton.setStyleSheet(u"background-color: rgb(0, 159, 238);\n"
"color: rgb(255, 255, 255);\n"
"font: 600 30pt \"Barlow SemiBold\";")

        self.verticalLayout_4.addWidget(self.stopbutton)

        self.stopalarmbutton = QPushButton(self.buttonframe)
        self.stopalarmbutton.setObjectName(u"stopalarmbutton")
        self.stopalarmbutton.setStyleSheet(u"background-color: rgb(0, 159, 238);\n"
"color: rgb(255, 255, 255);\n"
"font: 600 30pt \"Barlow SemiBold\";")

        self.verticalLayout_4.addWidget(self.stopalarmbutton)

        self.resetbutton = QPushButton(self.buttonframe)
        self.resetbutton.setObjectName(u"resetbutton")
        self.resetbutton.setStyleSheet(u"background-color: rgb(0, 159, 238);\n"
"color: rgb(255, 255, 255);\n"
"font: 600 30pt \"Barlow SemiBold\";")

        self.verticalLayout_4.addWidget(self.resetbutton)


        self.verticalLayout_3.addWidget(self.buttonframe)

        self.alarmframe = QFrame(self.leftframe)
        self.alarmframe.setObjectName(u"alarmframe")
        self.alarmframe.setMaximumSize(QSize(16777215, 300))
        self.alarmframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.alarmframe.setFrameShape(QFrame.Shape.Box)
        self.alarmframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.alarmframe)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.horizontalLayout_2.addLayout(self.verticalLayout_14)


        self.verticalLayout_3.addWidget(self.alarmframe)

        self.frame_17 = QFrame(self.leftframe)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 70))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.horizontalLayout.addWidget(self.leftframe)

        self.leftframe_2 = QFrame(self.bgframe)
        self.leftframe_2.setObjectName(u"leftframe_2")
        self.leftframe_2.setFrameShape(QFrame.Shape.NoFrame)
        self.leftframe_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.leftframe_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.bluemainframe = QFrame(self.leftframe_2)
        self.bluemainframe.setObjectName(u"bluemainframe")
        self.bluemainframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bluemainframe.setFrameShape(QFrame.Shape.Box)
        self.bluemainframe.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.bluemainframe)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.bluenameframe = QFrame(self.bluemainframe)
        self.bluenameframe.setObjectName(u"bluenameframe")
        self.bluenameframe.setMaximumSize(QSize(16777215, 70))
        self.bluenameframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.bluenameframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.bluenameframe)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bluename = QLabel(self.bluenameframe)
        self.bluename.setObjectName(u"bluename")
        self.bluename.setStyleSheet(u"font: 600 26pt \"Barlow SemiBold\";")
        self.bluename.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.bluename)


        self.verticalLayout_9.addWidget(self.bluenameframe)

        self.bluegraph = QFrame(self.bluemainframe)
        self.bluegraph.setObjectName(u"bluegraph")
        self.bluegraph.setFrameShape(QFrame.Shape.StyledPanel)
        self.bluegraph.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.bluegraph)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_15.addLayout(self.verticalLayout_19)


        self.verticalLayout_9.addWidget(self.bluegraph)


        self.gridLayout.addWidget(self.bluemainframe, 0, 0, 1, 1)

        self.irmainframe = QFrame(self.leftframe_2)
        self.irmainframe.setObjectName(u"irmainframe")
        self.irmainframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.irmainframe.setFrameShape(QFrame.Shape.Box)
        self.irmainframe.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_10 = QVBoxLayout(self.irmainframe)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.irnameframe = QFrame(self.irmainframe)
        self.irnameframe.setObjectName(u"irnameframe")
        self.irnameframe.setMaximumSize(QSize(16777215, 70))
        self.irnameframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.irnameframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.irnameframe)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.irname = QLabel(self.irnameframe)
        self.irname.setObjectName(u"irname")
        self.irname.setStyleSheet(u"font: 600 26pt \"Barlow SemiBold\";")
        self.irname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.irname)


        self.verticalLayout_10.addWidget(self.irnameframe)

        self.irgraph = QFrame(self.irmainframe)
        self.irgraph.setObjectName(u"irgraph")
        self.irgraph.setFrameShape(QFrame.Shape.StyledPanel)
        self.irgraph.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.irgraph)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.verticalLayout_21.addLayout(self.verticalLayout_20)


        self.verticalLayout_10.addWidget(self.irgraph)


        self.gridLayout.addWidget(self.irmainframe, 0, 1, 1, 1)

        self.tempmainframe = QFrame(self.leftframe_2)
        self.tempmainframe.setObjectName(u"tempmainframe")
        self.tempmainframe.setMaximumSize(QSize(16777215, 200))
        self.tempmainframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tempmainframe.setFrameShape(QFrame.Shape.Box)
        self.tempmainframe.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.tempmainframe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.temp = QFrame(self.tempmainframe)
        self.temp.setObjectName(u"temp")
        self.temp.setFrameShape(QFrame.Shape.Box)
        self.temp.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.temp)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")

        self.horizontalLayout_4.addLayout(self.verticalLayout_16)


        self.verticalLayout_5.addWidget(self.temp)

        self.tempnameframe = QFrame(self.tempmainframe)
        self.tempnameframe.setObjectName(u"tempnameframe")
        self.tempnameframe.setMaximumSize(QSize(16777215, 50))
        self.tempnameframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.tempnameframe.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.tempnameframe)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tempname = QLabel(self.tempnameframe)
        self.tempname.setObjectName(u"tempname")
        self.tempname.setStyleSheet(u"font: 600 26pt \"Barlow SemiBold\";")
        self.tempname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.tempname)


        self.verticalLayout_5.addWidget(self.tempnameframe)


        self.gridLayout.addWidget(self.tempmainframe, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.leftframe_2)


        self.verticalLayout.addWidget(self.bgframe)

        MainWindow.setCentralWidget(self.mainwindowtitle)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1068, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"CN0583 - SMART SMOKE DETECTION SYSTEM", None))
        self.startbutton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopbutton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.stopalarmbutton.setText(QCoreApplication.translate("MainWindow", u"Stop Alarm", None))
        self.resetbutton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_7.setText("")
        self.bluename.setText(QCoreApplication.translate("MainWindow", u"BLUE LIGHT INTENSITY", None))
        self.irname.setText(QCoreApplication.translate("MainWindow", u"IR LIGHT INTENSITY", None))
        self.tempname.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE", None))
    # retranslateUi

