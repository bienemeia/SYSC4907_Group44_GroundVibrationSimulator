# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'homepage.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QTimer, QThread)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                         QFont, QFontDatabase, QGradient, QIcon,
                         QImage, QKeySequence, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                             QLabel, QMainWindow, QPushButton, QSizePolicy,
                             QSpacerItem, QVBoxLayout, QWidget, QLineEdit, QDial, QMessageBox)

from circular_progress import CircularProgress
import images_rc
import time
from database import *
from I2CLib import *
from I2C_Communication import *


# Sets up all the widgets and objects in the HOMEPAGE. this is where they get added and edited to match our preference.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1117, 668)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"#mainContainer{\n"
                                         "background-color: rgb(44, 44, 44)\n"
                                         "}")
        self.gridLayout_2 = QGridLayout(self.mainContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.motorStatus = QLabel(self.mainContainer)
        self.motorStatus.setObjectName(u"motorStatus")
        self.motorStatus.setStyleSheet(u"#motorStatus{\n"
                                       "color: \"white\"\n"
                                       "}\n"
                                       "")

        self.gridLayout_2.addWidget(self.motorStatus, 2, 2, 1, 1)

        self.blank = QLabel(self.mainContainer)
        self.blank.setObjectName(u"blank")

        self.gridLayout_2.addWidget(self.blank, 0, 0, 1, 1)

        self.elapsedTime = QLabel(self.mainContainer)
        self.elapsedTime.setObjectName(u"elapsedTime")
        self.elapsedTime.setStyleSheet(u"#elapsedTime{\n"
                                       "color: \"white\"\n"
                                       "}\n"
                                       "")

        self.gridLayout_2.addWidget(self.elapsedTime, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.mainContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/pause.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x-octagon.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1, Qt.AlignRight)

        self.vibFreq = QLabel(self.mainContainer)
        self.vibFreq.setObjectName(u"vibFreq")
        self.vibFreq.setStyleSheet(u"#vibFreq{\n"
                                   "color: \"white\"\n"
                                   "}\n"
                                   "")

        self.gridLayout_2.addWidget(self.vibFreq, 2, 0, 1, 1)

        self.subContainer = QFrame(self.mainContainer)
        self.subContainer.setObjectName(u"subContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.subContainer.sizePolicy().hasHeightForWidth())
        self.subContainer.setSizePolicy(sizePolicy)
        self.subContainer.setMinimumSize(QSize(1039, 549))
        self.subContainer.setMaximumSize(QSize(1039, 549))
        self.subContainer.setFocusPolicy(Qt.NoFocus)
        self.subContainer.setStyleSheet(u"#subContainer{\n"
                                        "border: 4px solid white;\n"
                                        "border-radius: 15px;\n"
                                        "}")
        self.horizontalLayout_2 = QHBoxLayout(self.subContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftSide = QWidget(self.subContainer)
        self.leftSide.setObjectName(u"leftSide")
        self.leftSide.setMinimumSize(QSize(350, 0))
        self.leftSide.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.leftSide)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.turtle = QLabel(self.leftSide)
        self.turtle.setObjectName(u"turtle")

        self.horizontalLayout_3.addWidget(self.turtle, 0, Qt.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.leftSide, 0, Qt.AlignHCenter)

        self.rightSide = QWidget(self.subContainer)
        self.rightSide.setObjectName(u"rightSide")
        self.rightSide.setMinimumSize(QSize(600, 0))
        self.verticalLayout_2 = QVBoxLayout(self.rightSide)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.rightSide)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(582, 254))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"#frame{\n"
                                 "border: 4px solid white;\n"
                                 "border-radius: 15px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sensorArea = QWidget(self.frame)
        self.sensorArea.setObjectName(u"sensorArea")
        self.verticalLayout_3 = QVBoxLayout(self.sensorArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dialNames = QFrame(self.sensorArea)
        self.dialNames.setObjectName(u"dialNames")
        self.dialNames.setFrameShape(QFrame.StyledPanel)
        self.dialNames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.dialNames)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(
            15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.Temperature = QLabel(self.dialNames)
        self.Temperature.setObjectName(u"Temperature")
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(12)
        self.Temperature.setFont(font)
        self.Temperature.setStyleSheet(u"#Temperature{\n"
                                       "color: \"white\"\n"
                                       "}\n"
                                       "")

        self.horizontalLayout_6.addWidget(self.Temperature)

        self.Pressure = QLabel(self.dialNames)
        self.Pressure.setObjectName(u"Pressure")
        self.Pressure.setFont(font)
        self.Pressure.setStyleSheet(u"#Pressure{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")

        self.horizontalLayout_6.addWidget(self.Pressure)

        self.Humidity = QLabel(self.dialNames)
        self.Humidity.setObjectName(u"Humidity")
        self.Humidity.setFont(font)
        self.Humidity.setStyleSheet(u"#Humidity{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")

        self.horizontalLayout_6.addWidget(self.Humidity)

        self.horizontalSpacer_2 = QSpacerItem(
            5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addWidget(self.dialNames)

        self.dials = QFrame(self.sensorArea)
        self.dials.setObjectName(u"dials")
        self.horizontalLayout_5 = QHBoxLayout(self.dials)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tempBar = CircularProgress()
        self.tempBar.value = 25
        self.tempBar.font_size = 13
        self.tempBar.add_shadow(True)
        self.tempBar.setMinimumSize(self.tempBar.width, self.tempBar.height)
        self.tempBar.setObjectName(u"tempBar")

        self.dials.setLayout(self.horizontalLayout_5)
        self.horizontalLayout_5.addWidget(
            self.tempBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        self.pressureBar = CircularProgress()
        self.pressureBar.value = 50
        self.pressureBar.font_size = 13
        self.pressureBar.suffix = " kPa"
        self.pressureBar.add_shadow(True)
        self.pressureBar.setMinimumSize(
            self.tempBar.width, self.tempBar.height)
        self.pressureBar.setObjectName(u"pressureBar")

        self.horizontalLayout_5.addWidget(
            self.pressureBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        self.humidityBar = CircularProgress()
        self.humidityBar.value = 100
        self.humidityBar.font_size = 13
        self.humidityBar.suffix = "%"
        self.humidityBar.add_shadow(True)
        self.humidityBar.setMinimumSize(
            self.tempBar.width, self.tempBar.height)
        self.humidityBar.setObjectName(u"humidityBar")

        self.horizontalLayout_5.addWidget(
            self.humidityBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.dials)

        self.horizontalLayout_4.addWidget(self.sensorArea)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.displacementGraph = QFrame(self.rightSide)
        self.displacementGraph.setObjectName(u"displacementGraph")
        self.displacementGraph.setMinimumSize(QSize(582, 253))
        self.displacementGraph.setMaximumSize(QSize(16777215, 16777215))
        self.displacementGraph.setStyleSheet(u"#displacementGraph{\n"
                                             "border: 4px solid white;\n"
                                             "border-radius: 15px;\n"
                                             "}")
        self.displacementGraph.setFrameShape(QFrame.StyledPanel)
        self.displacementGraph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.displacementGraph)

        self.horizontalLayout_2.addWidget(self.rightSide)

        self.gridLayout_2.addWidget(
            self.subContainer, 1, 0, 1, 3, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(
            20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.clickHandler)
        self.pushButton_2.clicked.connect(self.stopHandler)
        self.pushButton_4.clicked.connect(self.pauseHandler)
        self.stop = False
        self.counter = 0
        self.started = 0

    # functions for the homepage's functionality, you can add as many as you like
    create_database()
    create_table()
    

    def stopHandler(self):
        if self.started == 0:
            return
        
        self.stop = True
        delete_table()
        self.started = 0
        

    def clickHandler(self):
        self.started = 1
        self.stop = False
        self.vibFreq.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vibration Frequency: 5 Hz</span></p></body></html>", None))
        self.motorStatus.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Motor Status: ON</span></p></body></html>", None))
        #self.updateTime()
        self.insert_loop(self.stop)
    
    def pauseHandler(self):
        self.stop = True
        self.insert_loop(self.stop)

    def insert_loop(self, stop):
        timer = QTime();
        timer.start()
        while not self.stop:
            app.processEvents()
            if timer.elapsed() >= 5000:
                 insert_values("1", "turtle", "111", "marwan@gmail")
                 timer.restart()   
            if stop:
                app.processEvents()
                return  
                

        """while not self.stop:
            app.processEvents()
            insert_values("1", "turtle", "111", "marwan@gmail")
            app.processEvents()
            if self.stop:
                break
            QThread.msleep(5000) """

    """def updateTime(self):
        while 1:
            self.counter += 1
            self.elapsedTime.setText(QCoreApplication.translate(
                "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Elapsed Time: --:%s</span></p></body></html>" % self.counter, None))
            app.processEvents()
            if self.stop:
                break
            QThread.msleep(1000) """

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.motorStatus.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Motor Status: -</span></p></body></html>", None))
        self.blank.setText("")
        self.elapsedTime.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Elapsed Time: --:-</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.vibFreq.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vibration Frequency: - Hz</span></p></body></html>", None))
# if QT_CONFIG(whatsthis)
        self.subContainer.setWhatsThis("")
# endif // QT_CONFIG(whatsthis)
        self.turtle.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/images/images/turtle.png\"/></p></body></html>", None))
        self.Temperature.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Temperature</span></p></body></html>", None))
        self.Pressure.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Pressure</span></p></body></html>", None))
        self.Humidity.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Humidity</span></p></body></html>", None))
    # retranslateUi

# Sets up all the widgets and objects in the SETTINGS. this is where they get added and edited to match our preference.


class Ui_SettingsWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"#mainContainer{\n"
                                         "background-color: rgb(44, 44, 44)\n"
                                         "}")
        self.gridLayout = QGridLayout(self.mainContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.mainContainer)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/back.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1, Qt.AlignLeft)

        self.subContainer = QFrame(self.mainContainer)
        self.subContainer.setObjectName(u"subContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.subContainer.sizePolicy().hasHeightForWidth())
        self.subContainer.setSizePolicy(sizePolicy)
        self.subContainer.setMinimumSize(QSize(1039, 549))
        self.subContainer.setMaximumSize(QSize(1039, 549))
        self.subContainer.setFocusPolicy(Qt.NoFocus)
        self.subContainer.setStyleSheet(u"#subContainer{\n"
                                        "border: 4px solid white;\n"
                                        "border-radius: 15px;\n"
                                        "}")
        self.horizontalLayout_2 = QHBoxLayout(self.subContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftSide = QFrame(self.subContainer)
        self.leftSide.setObjectName(u"leftSide")
        self.leftSide.setMinimumSize(QSize(504, 523))
        self.leftSide.setFrameShape(QFrame.StyledPanel)
        self.leftSide.setFrameShadow(QFrame.Raised)
        self.lineEdit_5 = QLineEdit(self.leftSide)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 427, 231, 22))
        self.lineEdit_5.setMinimumSize(QSize(231, 22))
        self.lineEdit_5.setMaximumSize(QSize(231, 22))
        self.lineEdit_5.setStyleSheet(u"#lineEdit_5{\n"
                                      "border: 3px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "}")
        self.lineEdit_6 = QLineEdit(self.leftSide)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 471, 231, 22))
        self.lineEdit_6.setMinimumSize(QSize(231, 22))
        self.lineEdit_6.setMaximumSize(QSize(231, 22))
        self.lineEdit_6.setStyleSheet(u"#lineEdit_6{\n"
                                      "border: 3px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "}")
        self.lineEdit_2 = QLineEdit(self.leftSide)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 209, 231, 22))
        self.lineEdit_2.setMinimumSize(QSize(231, 22))
        self.lineEdit_2.setMaximumSize(QSize(231, 22))
        self.lineEdit_2.setStyleSheet(u"#lineEdit_2{\n"
                                      "border: 3px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "}")
        self.lineEdit_4 = QLineEdit(self.leftSide)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 383, 231, 22))
        self.lineEdit_4.setMinimumSize(QSize(231, 22))
        self.lineEdit_4.setMaximumSize(QSize(231, 22))
        self.lineEdit_4.setStyleSheet(u"#lineEdit_4{\n"
                                      "border: 3px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "}")
        self.lineEdit = QLineEdit(self.leftSide)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 122, 231, 22))
        self.lineEdit.setMinimumSize(QSize(231, 22))
        self.lineEdit.setMaximumSize(QSize(231, 22))
        self.lineEdit.setStyleSheet(u"#lineEdit{\n"
                                    "border: 3px solid black;\n"
                                    "border-radius: 5px;\n"
                                    "}")
        self.label_2 = QLabel(self.leftSide)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 79, 201, 21))
        self.label_2.setMinimumSize(QSize(201, 21))
        self.label_2.setMaximumSize(QSize(231, 21))
        self.label_2.setStyleSheet(u"#label_2{\n"
                                   "color: \"white\"\n"
                                   "}\n"
                                   "")
        self.lineEdit_3 = QLineEdit(self.leftSide)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 296, 231, 22))
        self.lineEdit_3.setMinimumSize(QSize(231, 22))
        self.lineEdit_3.setMaximumSize(QSize(231, 22))
        self.lineEdit_3.setStyleSheet(u"#lineEdit_3{\n"
                                      "border: 3px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "}")
        self.label_7 = QLabel(self.leftSide)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 31, 31))
        self.label_7.setMinimumSize(QSize(31, 31))
        self.label_7.setMaximumSize(QSize(31, 31))
        self.label_7.setPixmap(QPixmap(u":/icons/icons/settings.svg"))
        self.label_3 = QLabel(self.leftSide)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 166, 201, 21))
        self.label_3.setMinimumSize(QSize(201, 21))
        self.label_3.setMaximumSize(QSize(231, 21))
        self.label_3.setStyleSheet(u"#label_3{\n"
                                   "color: \"white\"\n"
                                   "}\n"
                                   "")
        self.label_5 = QLabel(self.leftSide)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 340, 201, 21))
        self.label_5.setMinimumSize(QSize(201, 21))
        self.label_5.setMaximumSize(QSize(231, 21))
        self.label_5.setStyleSheet(u"#label_5{\n"
                                   "color: \"white\"\n"
                                   "}\n"
                                   "")
        self.label_4 = QLabel(self.leftSide)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 253, 201, 21))
        self.label_4.setMinimumSize(QSize(201, 21))
        self.label_4.setMaximumSize(QSize(231, 21))
        self.label_4.setStyleSheet(u"#label_4{\n"
                                   "color: \"white\"\n"
                                   "}\n"
                                   "")
        self.label = QLabel(self.leftSide)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 70, 21, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(21, 41))
        self.label_6 = QLabel(self.leftSide)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 160, 21, 41))
        sizePolicy1.setHeightForWidth(
            self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(21, 41))
        self.label_8 = QLabel(self.leftSide)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 245, 21, 41))
        sizePolicy1.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(21, 41))
        self.label_9 = QLabel(self.leftSide)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(215, 330, 30, 41))
        sizePolicy1.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMaximumSize(QSize(30, 41))
        self.pushButton_2 = QPushButton(self.leftSide)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 495, 41, 31))
        icon1 = QIcon()
        icon1.addFile(u"../UI Code/icons/plus-circle.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.leftSide)

        self.rightSide = QFrame(self.subContainer)
        self.rightSide.setObjectName(u"rightSide")
        self.rightSide.setMinimumSize(QSize(503, 523))
        self.rightSide.setStyleSheet(u"")
        self.rightSide.setFrameShape(QFrame.StyledPanel)
        self.rightSide.setFrameShadow(QFrame.Raised)
        self.dial = QDial(self.rightSide)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(310, 60, 131, 81))
        self.dial.setMaximum(1)
        self.dial.setPageStep(1)
        self.dial.setOrientation(Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setNotchesVisible(True)
        self.dial_2 = QDial(self.rightSide)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setGeometry(QRect(310, 230, 131, 81))
        self.dial_2.setMaximum(1)
        self.dial_2.setPageStep(1)
        self.dial_2.setNotchesVisible(True)
        self.label_13 = QLabel(self.rightSide)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 40, 201, 21))
        self.label_13.setMinimumSize(QSize(201, 21))
        self.label_13.setMaximumSize(QSize(231, 21))
        self.label_13.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.label_14 = QLabel(self.rightSide)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 80, 51, 51))
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))
        self.label_14.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.label_15 = QLabel(self.rightSide)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(412, 80, 51, 51))
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        self.label_15.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.label_16 = QLabel(self.rightSide)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(280, 210, 201, 21))
        self.label_16.setMinimumSize(QSize(201, 21))
        self.label_16.setMaximumSize(QSize(231, 21))
        self.label_16.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.label_17 = QLabel(self.rightSide)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(280, 250, 51, 51))
        self.label_17.setMinimumSize(QSize(0, 0))
        self.label_17.setMaximumSize(QSize(16777215, 16777215))
        self.label_17.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.label_18 = QLabel(self.rightSide)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(420, 250, 51, 51))
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        self.label_18.setStyleSheet(u"#label_13{\n"
                                    "color: \"white\"\n"
                                    "}\n"
                                    "")
        self.pushButton_3 = QPushButton(self.rightSide)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 380, 211, 61))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/export data.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(201, 71))
        self.pushButton_3.setFlat(True)
        self.pushButton_4 = QPushButton(self.rightSide)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(270, 450, 211, 61))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/save changes.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(201, 71))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_2.addWidget(self.rightSide)

        self.gridLayout.addWidget(self.subContainer, 1, 0, 1, 1)

        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_4.clicked.connect(self.savechange)
    # setupUi

    # functions for the settings page. add more here
    def savechange(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Changes Saved!")
        msgBox.setWindowTitle("Alert")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
# if QT_CONFIG(whatsthis)
        self.subContainer.setWhatsThis("")
# endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; font-style:italic;\">Experiment Name </span></p></body></html>", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; font-style:italic;\">Desired Frequency</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; font-style:italic;\">Email Addresses</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; font-style:italic;\">Desired Amplitude</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/name.png\"/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/freq.png\"/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/amp.png\"/></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/mail.png\"/></p></body></html>", None))
        self.pushButton_2.setText("")
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Temperature Unit</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">C</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">F</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#ffffff;\">Pressure Unit</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">psi</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700; color:#ffffff;\">Pa</span></p></body></html>", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.homewindow = Ui_MainWindow()
        self.settingswindow = Ui_SettingsWindow()
        self.starthomeWindow()

    def startSettings(self):
        self.settingswindow.setupUi(self)
        self.settingswindow.pushButton.clicked.connect(self.starthomeWindow)
        self.show()

    def starthomeWindow(self):
        self.homewindow.setupUi(self)
        self.homewindow.pushButton_3.clicked.connect(self.startSettings)
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
