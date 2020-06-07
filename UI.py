from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
import sys
from constants import LANGUAGES


class MainWindow(QWidget):

    def __init__(self, icon_name="", width=640, height=480):
        super().__init__()
        self.okButton = QPushButton("Ok")
        self.hBoxLayout = QHBoxLayout()
        self.vBoxLayout = QVBoxLayout()
        self.foreignCombobox = QComboBox()
        self.nativeCombobox = QComboBox()
        self.initUI(icon_name, width, height)


    def initUI(self, icon_name, width, height):
        self.resize(width, height)
        self.center()

        self.foreignCombobox.addItems(LANGUAGES)
        self.nativeCombobox.addItems(LANGUAGES)

        self.vBoxLayout.addWidget(QLabel("foreign:"))
        self.vBoxLayout.addWidget(self.foreignCombobox)
        self.vBoxLayout.addWidget(QLabel("native:"))
        self.vBoxLayout.addWidget(self.nativeCombobox)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addWidget(self.okButton)

        self.setLayout(self.hBoxLayout)

        self.setWindowTitle('Language repeater')
        # self.setWindowIcon(QIcon(icon_name))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow("sss")
    sys.exit(app.exec_())