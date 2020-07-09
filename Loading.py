import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
TTTT_PROGRESS_STYLE = """
QLabel { 
    background-color: white;
    }

"""

class UIWindow0(QObject):
    def setupUI(self, MainWindow):
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.label = QLabel("label", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        pixmap = QtGui.QPixmap('image/메인화면.png')
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet(TTTT_PROGRESS_STYLE)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.raise_()
        self.test = QLabel('', self.centralwidget)
        m_gif = QtGui.QMovie('image/메인화면로딩.gif', QByteArray())
        m_gif.setScaledSize(QtCore.QSize(70, 70))
        self.test.setMovie(m_gif)
        self.test.setGeometry(QtCore.QRect(738, 595, 500, 500))
        m_gif.setCacheMode(QtGui.QMovie.CacheAll)
        m_gif.setSpeed(95)
        m_gif.start()
        self.test.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.timer0 = QTimer(self)
        self.timer0.setInterval(30000)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.startUIWindow0()

    def startUIWindow0(self):
        self.UItab0 = UIWindow0()
        self.UItab0.setupUI(self)
        self.show()
        self.timer0.start()
        self.timer0.timeout.connect(lambda: sys.exit())

def Loading_start():
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
