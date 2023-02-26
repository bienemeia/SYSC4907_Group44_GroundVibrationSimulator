from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.uic import loadUi
import sys
import images_rc


class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        
        loadUi('C:\\Users\zeyad\\Desktop\\UNI\\4th Year Project\\UI Code\\settings\\settingspage.ui', self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUi()
    ui.show()
    app.exec()