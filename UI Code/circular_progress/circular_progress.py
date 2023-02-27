from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        super().__init__()

        self.value = 0
        self.width = 150
        self.height = 150
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x8A00C2
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "°"
        self.text_color = 0x8A00C2

        self.resize(self.width, self.height)

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        #Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        # TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value}{self.suffix}")


        paint.end()

    def set_value(self, value):
        self.value = value
        self.repaint()

    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,0,0,150))
            self.setGraphicsEffect(self.shadow)
