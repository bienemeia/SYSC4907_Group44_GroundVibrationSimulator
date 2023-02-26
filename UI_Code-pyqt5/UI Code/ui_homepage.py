# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer, QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from circular_progress import CircularProgress
import images_rc
import time

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
        icon1.addFile(u":/icons/icons/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

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
        sizePolicy.setHeightForWidth(self.subContainer.sizePolicy().hasHeightForWidth())
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
        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

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

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

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
        self.horizontalLayout_5.addWidget(self.tempBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        self.pressureBar = CircularProgress()
        self.pressureBar.value = 50
        self.pressureBar.font_size = 13
        self.pressureBar.suffix = " kPa"
        self.pressureBar.add_shadow(True)
        self.pressureBar.setMinimumSize(self.tempBar.width, self.tempBar.height)
        self.pressureBar.setObjectName(u"pressureBar")
        

        self.horizontalLayout_5.addWidget(self.pressureBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)

        self.humidityBar = CircularProgress()
        self.humidityBar.value = 100
        self.humidityBar.font_size = 13
        self.humidityBar.suffix = "%"
        self.humidityBar.add_shadow(True)
        self.humidityBar.setMinimumSize(self.tempBar.width, self.tempBar.height)
        self.humidityBar.setObjectName(u"humidityBar")
        

        self.horizontalLayout_5.addWidget(self.humidityBar, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)


        self.verticalLayout_3.addWidget(self.dials)


        self.horizontalLayout_4.addWidget(self.sensorArea)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

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


        self.gridLayout_2.addWidget(self.subContainer, 1, 0, 1, 3, Qt.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.clickHandler)
        self.pushButton_2.clicked.connect(self.stopHandler)
        self.stop = False;
        self.counter = 0;


    def stopHandler(self):
        self.stop = True;

    def clickHandler(self):
        self.stop = False;
        index = 1;
        self.vibFreq.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vibration Frequency: 5 Hz</span></p></body></html>", None))
        self.motorStatus.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Motor Status: ON</span></p></body></html>", None))
        self.updateTime()
        
    def updateTime(self):
        while 1:
                self.counter += 1;
                self.elapsedTime.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Elapsed Time: --:%s</span></p></body></html>" %self.counter, None))
                app.processEvents()
                if self.stop:
                        break
                QThread.msleep(1000)






        
    
        

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.motorStatus.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Motor Status: -</span></p></body></html>", None))
        self.blank.setText("")
        self.elapsedTime.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Elapsed Time: --:-</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.vibFreq.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vibration Frequency: - Hz</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.subContainer.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.turtle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/turtle.png\"/></p></body></html>", None))
        self.Temperature.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Temperature</span></p></body></html>", None))
        self.Pressure.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Pressure</span></p></body></html>", None))
        self.Humidity.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Humidity</span></p></body></html>", None))
    # retranslateUi



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

