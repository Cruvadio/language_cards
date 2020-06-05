from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

class MainWindow (QWidget):

    def __init__(self, icon_name, width=640, height=480):
        super().__init__()

        self.initUI(icon_name, width, height)


    def initUI(self, icon_name, width, height):
        self.resize(width, height)
        self.center()
        self.setWindowTitle('Language repeater')
        self.setWindowIcon(QIcon(icon_name))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
