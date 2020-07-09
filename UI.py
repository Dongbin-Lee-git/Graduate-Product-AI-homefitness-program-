import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5075
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def objectinfo(run_data):
    sock.sendto((run_data).encode(), (UDP_IP, UDP_PORT))


# up code : udp
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# down code : UI

UIFlag = 0
a_a = 0
score = 0
cnt = 0
b_b = ""


class UIWindow1(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 1
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)
        self.pushButton2 = QPushButton("pushButton", self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 300, 151, 70))
        self.pushButton2.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton2)
        opacity_effect.setOpacity(0.0)
        self.pushButton2.setGraphicsEffect(opacity_effect)

        # 버튼이미지
        self.label = QLabel("label", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 151, 70))
        self.label.setText("")
        pixmap = QtGui.QPixmap('image/음쓰.png')
        pixmap = pixmap.scaled(140, 75)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.pushButton2.resize(pixmap.width(), pixmap.height())
        self.label.raise_()

        self.laman = QLabel("laman", self.centralwidget)
        self.laman.setGeometry(QtCore.QRect(260, 70, 700, 1000))
        self.laman.setText("")
        pixmap7 = QtGui.QPixmap('image/사람틀2.png')
        pixmap7 = pixmap7.scaledToHeight(770)
        self.laman.setPixmap(pixmap7)
        self.laman.raise_()

        eff = QGraphicsDropShadowEffect()
        eff.setOffset(2, 1)
        eff.setBlurRadius(15)
        eff.setColor(Qt.red)
        self.Slabel3 = QLabel('', self.centralwidget)
        self.Slabel3.setText('화면에 보이는 테두리안에\n몸을 맞춰 서주세요!')
        self.Slabel3.setGeometry(205, 0, 490, 300)
        self.Slabel3.setStyleSheet("color: rgba(255, 255, 255, 1);"
                                   "line-height:1.6;"
                                   "font: 15pt \"배달의민족 도현\";\n"
                                   "border-style: solid;"
                                   "border-width: 0px;"
                                   "border-color: rgba(255, 255, 255, 1);"
                                   "border-radius: 8px")
        self.Slabel3.setGraphicsEffect(eff)
        self.Slabel3.setAlignment(Qt.AlignCenter)
        self.Slabel3.raise_()

        self.pushButton2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)


class UIWindow2(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 2
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)

        self.pushButton4 = QPushButton("뒤로가기", self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.pushButton4.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton4)
        opacity_effect.setOpacity(0.0)
        self.pushButton4.setGraphicsEffect(opacity_effect)

        self.pushButton1 = QPushButton("스쿼트", self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(10, 220, 151, 51))
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet("")
        opacity_effect = QGraphicsOpacityEffect(self.pushButton1)
        opacity_effect.setOpacity(0.0)
        self.pushButton1.setGraphicsEffect(opacity_effect)

        self.pushButton2 = QPushButton("프론트레이즈", self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet("")
        opacity_effect = QGraphicsOpacityEffect(self.pushButton2)
        opacity_effect.setOpacity(0.0)
        self.pushButton2.setGraphicsEffect(opacity_effect)

        # 좌우 버튼
        self.pushButton6 = QPushButton("leftbutton", self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(610, 310, 50, 20))
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("")
        self.pushButton6.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton6)
        opacity_effect.setOpacity(0.0)
        self.pushButton6.setGraphicsEffect(opacity_effect)

        self.pushButton7 = QPushButton("rightbutton", self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(762, 310, 70, 5))
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("")
        self.pushButton7.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton7)
        opacity_effect.setOpacity(0.0)
        self.pushButton7.setGraphicsEffect(opacity_effect)

        MainWindow.setCentralWidget(self.centralwidget)

        self.label2_1 = QLabel("label2_1", self.centralwidget)
        self.label2_1.setGeometry(QtCore.QRect(10, 220, 151, 51))
        self.label2_1.setText("")
        pixmap = QtGui.QPixmap('image/스쿼트.png')
        pixmap = pixmap.scaled(140, 75)
        self.label2_1.setPixmap(pixmap)
        self.label2_1.resize(pixmap.width(), pixmap.height())
        self.pushButton1.resize(pixmap.width(), pixmap.height())
        self.label2_1.raise_()

        self.label2_2 = QLabel("label2_2", self.centralwidget)
        self.label2_2.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.label2_2.setText("")
        pixmap = QtGui.QPixmap('image/프론트레이즈.png')
        pixmap = pixmap.scaled(140, 75)
        self.label2_2.setPixmap(pixmap)
        self.label2_2.resize(pixmap.width(), pixmap.height())
        self.pushButton2.resize(pixmap.width(), pixmap.height())
        self.label2_2.raise_()

        self.label2_4 = QLabel("label2_4", self.centralwidget)
        self.label2_4.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.label2_4.setText("")
        pixmap = QtGui.QPixmap('image/뒤로가기.png')
        pixmap = pixmap.scaled(140, 75)
        self.label2_4.setPixmap(pixmap)
        self.label2_4.resize(pixmap.width(), pixmap.height())
        self.pushButton4.resize(pixmap.width(), pixmap.height())
        self.label2_4.raise_()

        # 좌우 버튼이미지
        self.labe6 = QLabel("labe6", self.centralwidget)
        self.labe6.setGeometry(QtCore.QRect(600, 300, 151, 51))
        self.labe6.setText("")
        pixmap6 = QtGui.QPixmap('image/흰빨왼쪽.png')
        self.labe6.setPixmap(pixmap6)
        self.labe6.resize(pixmap6.width(), pixmap6.height())
        self.pushButton6.resize(pixmap6.width(), pixmap6.height())
        self.labe6.raise_()

        self.labe7 = QLabel("labe7", self.centralwidget)
        self.labe7.setGeometry(QtCore.QRect(750, 300, 151, 51))
        self.labe7.setText("")
        pixmap7 = QtGui.QPixmap('image/빨빨오른쪽.png')
        self.labe7.setPixmap(pixmap7)
        self.labe7.resize(pixmap7.width(), pixmap7.height())
        self.pushButton7.resize(pixmap7.width(), pixmap7.height())
        self.labe7.raise_()

        self.labe8 = QLabel("labe8", self.centralwidget)
        self.labe8.setGeometry(QtCore.QRect(550, 180, 151, 51))
        self.labe8.setText("")
        pixmap8 = QtGui.QPixmap('image/boxx.png')
        self.labe8.setPixmap(pixmap8)
        self.labe8.resize(pixmap8.width(), pixmap8.height())
        self.labe8.raise_()

        self.pushButton6.raise_()
        self.pushButton7.raise_()
        self.pushButton1.raise_()
        self.pushButton2.raise_()
        self.pushButton4.raise_()

        b_b = ""
        # b_b 는 운동종류 1=스쿼트, 2=프론트레이즈

    def clickMethod4(self):
        global b_b
        b_b = "Squat"
        objectinfo("Squat_100")

    def clickMethod5(self):
        global b_b
        b_b = "FrontRaise"
        objectinfo("FrontRaise_100")


class UIWindow3(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 3
        global a_a
        a_a = 0
        # a_a 는 운동횟수 정하는 변수
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)

        if b_b == "Squat":
            self.labe9 = QLabel("labe9", self.centralwidget)
            self.labe9.setGeometry(QtCore.QRect(620, 25, 151, 51))
            self.labe9.setText("")
            pixmap9 = QtGui.QPixmap('image/스쿼트안내.png')
            self.labe9.setPixmap(pixmap9)
            self.labe9.resize(pixmap9.width(), pixmap9.height())
            self.labe9.raise_()

        if b_b == "FrontRaise":
            self.labe9 = QLabel("labe9", self.centralwidget)
            self.labe9.setGeometry(QtCore.QRect(620, 25, 151, 51))
            self.labe9.setText("")
            pixmap9 = QtGui.QPixmap('image/프론트안내.png')
            self.labe9.setPixmap(pixmap9)
            self.labe9.resize(pixmap9.width(), pixmap9.height())
            self.labe9.raise_()

        self.pushButton4 = QPushButton("운동시작", self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(10, 460, 151, 51))
        self.pushButton4.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton4)
        opacity_effect.setOpacity(0.0)
        self.pushButton4.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton4.raise_()

        self.startlabel = QLabel("startlabel", self.centralwidget)
        self.startlabel.setGeometry(QtCore.QRect(10, 460, 151, 51))
        self.startlabel.setText("")
        pixmap = QtGui.QPixmap('image/음쓰.png')
        pixmap = pixmap.scaled(140, 75)
        self.startlabel.setPixmap(pixmap)
        self.startlabel.resize(pixmap.width(), pixmap.height())
        self.pushButton4.resize(pixmap.width(), pixmap.height())
        self.startlabel.raise_()

        self.pushButton5 = QPushButton("뒤로가기", self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.pushButton5.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton5)
        opacity_effect.setOpacity(0.0)
        self.pushButton5.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton5.raise_()

        self.labelCPS = QLabel("labelCPS", self.centralwidget)
        self.labelCPS.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.labelCPS.setText("")
        pixmap = QtGui.QPixmap('image/뒤로가기.png')
        pixmap = pixmap.scaled(140, 75)
        self.labelCPS.setPixmap(pixmap)
        self.labelCPS.resize(pixmap.width(), pixmap.height())
        self.pushButton5.resize(pixmap.width(), pixmap.height())
        self.labelCPS.raise_()

        # 좌우 버튼
        self.pushButton6 = QPushButton("leftbutton", self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(610, 310, 50, 20))
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("")
        self.pushButton6.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton6)
        opacity_effect.setOpacity(0.0)
        self.pushButton6.setGraphicsEffect(opacity_effect)

        self.pushButton7 = QPushButton("rightbutton", self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(762, 310, 70, 5))
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("")
        self.pushButton7.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton7)
        opacity_effect.setOpacity(0.0)
        self.pushButton7.setGraphicsEffect(opacity_effect)

        self.labe6 = QLabel("labe6", self.centralwidget)
        self.labe6.setGeometry(QtCore.QRect(600, 300, 151, 51))
        self.labe6.setText("")
        pixmap6 = QtGui.QPixmap('image/흰빨왼쪽.png')
        self.labe6.setPixmap(pixmap6)
        self.labe6.resize(pixmap6.width(), pixmap6.height())
        self.pushButton6.resize(pixmap6.width(), pixmap6.height())
        self.labe6.raise_()

        self.labe7 = QLabel("labe7", self.centralwidget)
        self.labe7.setGeometry(QtCore.QRect(750, 300, 151, 51))
        self.labe7.setText("")
        pixmap7 = QtGui.QPixmap('image/빨빨오른쪽.png')
        self.labe7.setPixmap(pixmap7)
        self.labe7.resize(pixmap7.width(), pixmap7.height())
        self.pushButton7.resize(pixmap7.width(), pixmap7.height())
        self.labe7.raise_()

        self.labe8 = QLabel("labe8", self.centralwidget)
        self.labe8.setGeometry(QtCore.QRect(550, 180, 151, 51))
        self.labe8.setText("")
        pixmap8 = QtGui.QPixmap('image/boxx.png')
        self.labe8.setPixmap(pixmap8)
        self.labe8.resize(pixmap8.width(), pixmap8.height())
        self.pushButton7.resize(pixmap8.width(), pixmap8.height())
        self.labe8.raise_()

        # 횟수 설정 버튼
        self.pushButton1 = QPushButton("5회", self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(10, 220, 151, 51))
        self.pushButton1.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton1)
        opacity_effect.setOpacity(0.0)
        self.pushButton1.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton1.raise_()

        self.count5label = QLabel("count5label", self.centralwidget)
        self.count5label.setGeometry(QtCore.QRect(10, 220, 151, 51))
        self.count5label.setText("")
        pixmap5 = QtGui.QPixmap('image/5회.png')
        pixmap5 = pixmap5.scaled(140, 75)
        self.count5label.setPixmap(pixmap5)
        self.count5label.resize(pixmap5.width(), pixmap5.height())
        self.pushButton1.resize(pixmap5.width(), pixmap5.height())
        self.count5label.raise_()

        self.pushButton2 = QPushButton("10회", self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.pushButton2.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton2)
        opacity_effect.setOpacity(0.0)
        self.pushButton2.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton2.raise_()

        self.count10label = QLabel("count5label", self.centralwidget)
        self.count10label.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.count10label.setText("")
        pixmap = QtGui.QPixmap('image/10회.png')
        pixmap = pixmap.scaled(140, 75)
        self.count10label.setPixmap(pixmap)
        self.count10label.resize(pixmap.width(), pixmap.height())
        self.pushButton2.resize(pixmap.width(), pixmap.height())
        self.count10label.raise_()

        self.pushButton3 = QPushButton("15회", self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(10, 380, 151, 51))
        self.pushButton3.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton3)
        opacity_effect.setOpacity(0.0)
        self.pushButton3.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton3.raise_()

        self.count15label = QLabel("count5label", self.centralwidget)
        self.count15label.setGeometry(QtCore.QRect(10, 380, 151, 71))
        self.count15label.setText("")
        pixmap = QtGui.QPixmap('image/15회.png')
        pixmap = pixmap.scaled(140, 75)
        self.count15label.setPixmap(pixmap)
        self.count15label.resize(pixmap.width(), pixmap.height())
        self.count15label.resize(pixmap.width(), pixmap.height())
        self.count15label.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton1.raise_()
        self.pushButton2.raise_()
        self.pushButton3.raise_()
        self.pushButton4.raise_()
        self.pushButton5.raise_()
        self.pushButton6.raise_()
        self.pushButton7.raise_()

        self.label = QLabel("label", self.centralwidget)
        self.labell = QLabel("labell", self.centralwidget)

        eff = QGraphicsDropShadowEffect()
        eff.setOffset(2, 1)
        eff.setBlurRadius(20)
        eff.setColor(Qt.red)
        self.Slabel2 = QLabel('', self.centralwidget)
        self.Slabel2.setText('운동횟수를 지정해주세요!')
        self.Slabel2.setGeometry(220, 60, 400, 200)
        self.Slabel2.setStyleSheet("color: rgba(255, 255, 255, 1);"
                                   "line-height:1.5px;"
                                   "font: 20pt \"배달의민족 도현\";\n"
                                   "border-style: solid;"
                                   "border-width: 0px;"
                                   "border-color: rgba(255, 255, 255, 1);"
                                   "border-radius: 8px")
        self.Slabel2.setGraphicsEffect(eff)
        self.Slabel2.setAlignment(Qt.AlignCenter)
        self.Slabel2.raise_()
        self.Slabel2.setVisible(False)

    def clickMethod1(self):
        global a_a
        a_a = 5
        self.Slabel2.setVisible(False)

        eff5 = QGraphicsDropShadowEffect()
        eff5.setOffset(2, 1)
        eff5.setBlurRadius(20)
        eff5.setColor(Qt.red)
        self.Slabel2.setText('지정횟수 : {}회'.format(a_a))
        self.Slabel2.setVisible(True)

        self.labell.setGeometry(QtCore.QRect(150, 230, 151, 51))
        pixmap2 = QtGui.QPixmap('image/빨강체크표시.png')
        self.labell.setPixmap(pixmap2)
        self.labell.resize(pixmap2.width(), pixmap2.height())
        self.labell.raise_()

    def clickMethod2(self):
        global a_a
        a_a = 10
        self.Slabel2.setVisible(False)

        eff5 = QGraphicsDropShadowEffect()
        eff5.setOffset(2, 1)
        eff5.setBlurRadius(20)
        eff5.setColor(Qt.red)
        self.Slabel2.setText('지정횟수 : {}회'.format(a_a))
        self.Slabel2.setVisible(True)

        self.labell.setGeometry(QtCore.QRect(150, 310, 151, 51))
        pixmap2 = QtGui.QPixmap('image/빨강체크표시.png')
        self.labell.setPixmap(pixmap2)
        self.labell.resize(pixmap2.width(), pixmap2.height())
        self.labell.raise_()

    def clickMethod3(self):
        global a_a
        a_a = 15
        self.Slabel2.setVisible(False)
        eff5 = QGraphicsDropShadowEffect()
        eff5.setOffset(2, 1)
        eff5.setBlurRadius(20)
        eff5.setColor(Qt.red)
        self.Slabel2.setText('지정횟수 : {}회'.format(a_a))
        self.Slabel2.setVisible(True)

        self.labell.setGeometry(QtCore.QRect(150, 390, 151, 51))
        pixmap2 = QtGui.QPixmap('image/빨강체크표시.png')
        self.labell.setPixmap(pixmap2)
        self.labell.resize(pixmap2.width(), pixmap2.height())
        self.labell.raise_()


class UIWindow4(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 4
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)

        if a_a == 5:
            self.labeloo = QLabel("label", self.centralwidget)
            self.labeloo.setGeometry(QtCore.QRect(10, 300, 151, 51))
            pixmap = QtGui.QPixmap('image/5회지정.png')
            self.labeloo.setPixmap(pixmap)
            self.labeloo.resize(pixmap.width(), pixmap.height())
            self.labeloo.raise_()

        if a_a == 10:
            self.labeloo = QLabel("label", self.centralwidget)
            self.labeloo.setGeometry(QtCore.QRect(10, 300, 151, 51))
            pixmap = QtGui.QPixmap('image/10회지정.png')
            self.labeloo.setPixmap(pixmap)
            self.labeloo.resize(pixmap.width(), pixmap.height())
            self.labeloo.raise_()

        if a_a == 15:
            self.labeloo = QLabel("label", self.centralwidget)
            self.labeloo.setGeometry(QtCore.QRect(10, 300, 151, 51))
            pixmap = QtGui.QPixmap('image/15회지정.png')
            self.labeloo.setPixmap(pixmap)
            self.labeloo.resize(pixmap.width(), pixmap.height())
            self.labeloo.raise_()

        # 좌우 버튼
        self.pushButton6 = QPushButton("leftbutton", self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(610, 310, 50, 20))
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("")
        self.pushButton6.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton6)
        opacity_effect.setOpacity(0.0)
        self.pushButton6.setGraphicsEffect(opacity_effect)

        self.pushButton7 = QPushButton("rightbutton", self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(762, 310, 70, 5))
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("")
        self.pushButton7.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton7)
        opacity_effect.setOpacity(0.0)

        self.pushButton7.setGraphicsEffect(opacity_effect)
        self.labe6 = QLabel("labe6", self.centralwidget)
        self.labe6.setGeometry(QtCore.QRect(600, 300, 151, 51))
        self.labe6.setText("")
        pixmap6 = QtGui.QPixmap('image/흰빨왼쪽.png')
        self.labe6.setPixmap(pixmap6)
        self.labe6.resize(pixmap6.width(), pixmap6.height())
        self.pushButton6.resize(pixmap6.width(), pixmap6.height())
        self.labe6.raise_()

        self.labe7 = QLabel("labe7", self.centralwidget)
        self.labe7.setGeometry(QtCore.QRect(750, 300, 151, 51))
        self.labe7.setText("")
        pixmap7 = QtGui.QPixmap('image/빨빨오른쪽.png')
        self.labe7.setPixmap(pixmap7)
        self.labe7.resize(pixmap7.width(), pixmap7.height())
        self.pushButton7.resize(pixmap7.width(), pixmap7.height())
        self.labe7.raise_()

        self.labe8 = QLabel("labe8", self.centralwidget)
        self.labe8.setGeometry(QtCore.QRect(550, 180, 151, 51))
        self.labe8.setText("")
        pixmap8 = QtGui.QPixmap('image/boxx.png')
        self.labe8.setPixmap(pixmap8)
        self.labe8.resize(pixmap8.width(), pixmap8.height())
        self.pushButton7.resize(pixmap8.width(), pixmap8.height())
        self.labe8.raise_()
        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        self.test = QLabel('', self.centralwidget)
        self.test.setVisible(False)
        self.e_gif = QtGui.QMovie("image/cntlabel.gif", QByteArray())
        self.test.setMovie(self.e_gif)
        self.test.setGeometry(QtCore.QRect(300, 5, 500, 500))
        self.e_gif.setCacheMode(QtGui.QMovie.CacheAll)

        self.pushButton4 = QPushButton("운동시작", self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(10, 460, 151, 51))

        self.pushButton4.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton4)
        opacity_effect.setOpacity(0.0)
        self.pushButton4.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton4.raise_()

        self.startlabel = QLabel("startlabel", self.centralwidget)
        self.startlabel.setGeometry(QtCore.QRect(10, 460, 151, 51))
        self.startlabel.setText("")
        pixmap = QtGui.QPixmap('image/음쓰.png')
        pixmap = pixmap.scaled(140, 75)
        self.startlabel.setPixmap(pixmap)
        self.startlabel.resize(pixmap.width(), pixmap.height())
        self.pushButton4.resize(pixmap.width(), pixmap.height())
        self.startlabel.raise_()

        self.pushButton5 = QPushButton("뒤로가기", self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.pushButton5.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton5)
        opacity_effect.setOpacity(0.0)
        self.pushButton5.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton5.raise_()

        self.labelCPS = QLabel("labelCPS", self.centralwidget)
        self.labelCPS.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.labelCPS.setText("")
        pixmap = QtGui.QPixmap('image/뒤로가기.png')
        pixmap = pixmap.scaled(140, 75)
        self.labelCPS.setPixmap(pixmap)
        self.labelCPS.resize(pixmap.width(), pixmap.height())
        self.pushButton5.resize(pixmap.width(), pixmap.height())
        self.labelCPS.raise_()

        self.pushButton5.raise_()
        self.pushButton4.raise_()
        self.pushButton6.raise_()
        self.pushButton7.raise_()


class UIWindow5(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 5
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)

        self.pushButton6 = QPushButton("leftbutton", self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(610, 310, 50, 20))
        self.pushButton6.setAutoFillBackground(False)
        self.pushButton6.setStyleSheet("")
        self.pushButton6.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton6)
        opacity_effect.setOpacity(0.0)
        self.pushButton6.setGraphicsEffect(opacity_effect)

        self.pushButton7 = QPushButton("rightbutton", self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(762, 310, 70, 5))
        self.pushButton7.setAutoFillBackground(False)
        self.pushButton7.setStyleSheet("")
        self.pushButton7.setFixedSize(150, 94)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton7)
        opacity_effect.setOpacity(0.0)
        self.pushButton7.setGraphicsEffect(opacity_effect)

        self.labe6 = QLabel("labe6", self.centralwidget)
        self.labe6.setGeometry(QtCore.QRect(600, 300, 151, 51))
        self.labe6.setText("")
        pixmap6 = QtGui.QPixmap('image/흰빨왼쪽.png')
        self.labe6.setPixmap(pixmap6)
        self.labe6.resize(pixmap6.width(), pixmap6.height())
        self.pushButton6.resize(pixmap6.width(), pixmap6.height())
        self.labe6.raise_()

        self.labe7 = QLabel("labe7", self.centralwidget)
        self.labe7.setGeometry(QtCore.QRect(750, 300, 151, 51))
        self.labe7.setText("")
        pixmap7 = QtGui.QPixmap('image/빨빨오른쪽.png')
        self.labe7.setPixmap(pixmap7)
        self.labe7.resize(pixmap7.width(), pixmap7.height())
        self.pushButton7.resize(pixmap7.width(), pixmap7.height())
        self.labe7.raise_()

        self.labe8 = QLabel("labe8", self.centralwidget)
        self.labe8.setGeometry(QtCore.QRect(550, 180, 151, 51))
        self.labe8.setText("")
        pixmap8 = QtGui.QPixmap('image/boxx.png')
        self.labe8.setPixmap(pixmap8)
        self.labe8.resize(pixmap8.width(), pixmap8.height())
        self.pushButton7.resize(pixmap8.width(), pixmap8.height())
        self.labe8.raise_()

        # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

        self.pushButton2 = QPushButton("뒤로가기", self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.pushButton2.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton2)
        opacity_effect.setOpacity(0.0)
        self.pushButton2.setGraphicsEffect(opacity_effect)

        self.pushButton2.raise_()

        self.labelCPS = QLabel("labelCPS", self.centralwidget)
        self.labelCPS.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.labelCPS.setText("")
        pixmap = QtGui.QPixmap('image/운동중지.png')
        pixmap = pixmap.scaled(140, 75)
        self.labelCPS.setPixmap(pixmap)
        self.labelCPS.resize(pixmap.width(), pixmap.height())
        self.pushButton2.resize(pixmap.width(), pixmap.height())
        self.labelCPS.raise_()

        global b_b
        if b_b == "Squat":
            c_c = 86.41
        if b_b == "FrontRaise":
            c_c = 64.01

        self.test = QLabel('', self.centralwidget)

        self.f_gif = QtGui.QMovie("image/%s.gif" % str(a_a), QByteArray())
        self.f_gif.setScaledSize(QtCore.QSize(250, 250))
        self.test.setMovie(self.f_gif)
        self.test.setGeometry(QtCore.QRect(40, 620, 500, 500))
        self.f_gif.setCacheMode(QtGui.QMovie.CacheAll)
        self.f_gif.setSpeed(c_c)
        self.f_gif.start()

        self.pushButton2.raise_()
        self.pushButton6.raise_()
        self.pushButton7.raise_()

        MainWindow.setCentralWidget(self.centralwidget)


class UIWindow6(QObject):
    def setupUI(self, MainWindow):
        global UIflag
        UIflag = 6
        MainWindow.resize(1920, 1080)

        self.centralwidget = QWidget(MainWindow)

        self.pushButton2 = QPushButton("운동종료", self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.pushButton2.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton2)
        opacity_effect.setOpacity(0.0)
        self.pushButton2.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton2.raise_()

        self.labelCPS = QLabel("labelCPS", self.centralwidget)
        self.labelCPS.setGeometry(QtCore.QRect(10, 540, 151, 51))
        self.labelCPS.setText("")
        pixmap = QtGui.QPixmap('image/운동종료.png')
        pixmap = pixmap.scaled(140, 75)
        self.labelCPS.setPixmap(pixmap)
        self.labelCPS.resize(pixmap.width(), pixmap.height())
        self.pushButton2.resize(pixmap.width(), pixmap.height())
        self.labelCPS.raise_()

        self.pushButton3 = QPushButton("다시시작", self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(10, 460, 151, 51))
        self.pushButton3.setAutoFillBackground(False)
        opacity_effect = QGraphicsOpacityEffect(self.pushButton3)
        opacity_effect.setOpacity(0.0)
        self.pushButton3.setGraphicsEffect(opacity_effect)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton3.raise_()

        self.labelre = QLabel("labelre", self.centralwidget)
        self.labelre.setGeometry(QtCore.QRect(10, 460, 151, 51))
        self.labelre.setText("")
        pixmap = QtGui.QPixmap('image/다시시작.png')
        pixmap = pixmap.scaled(140, 75)
        self.labelre.setPixmap(pixmap)
        self.labelre.resize(pixmap.width(), pixmap.height())
        self.pushButton3.resize(pixmap.width(), pixmap.height())
        self.labelre.raise_()

        self.pushButton2.raise_()
        self.pushButton3.raise_()

        self.test = QLabel('', self.centralwidget)
        self.f_gif = QtGui.QMovie('image/흐음.gif', QByteArray())
        self.f_gif.setScaledSize(QtCore.QSize(500, 500))
        self.test.setMovie(self.f_gif)
        self.test.setGeometry(QtCore.QRect(250, 0, 960, 1080))
        self.f_gif.setCacheMode(QtGui.QMovie.CacheAll)
        opacity_effect = QGraphicsOpacityEffect(self.test)
        opacity_effect.setOpacity(0.7)
        self.f_gif.setSpeed(100)
        self.f_gif.start()
        eff = QGraphicsDropShadowEffect()
        eff.setOffset(2, 1)
        eff.setBlurRadius(20)
        eff.setColor(Qt.red)

        global score
        global a_a
        tmp = 0
        if b_b == "Squat":
            tmp = '스쿼트'
        if b_b == "FrontRaise":
            tmp = '프론트레이즈'
        score =100
        self.Slabel = QLabel('', self.centralwidget)
        self.Slabel.setText('정확도 : ' + str(score) + '%\n' + '운동 : ' + tmp + '\n횟수 : ' + str(a_a) + '회')
        self.Slabel.setGeometry(320, 60, 400, 200)
        self.Slabel.setStyleSheet("color: rgba(255, 255, 255, 1);"
                                  "line-height:1.5px;"
                                  "font: 25pt \"배달의민족 도현\";\n"
                                  "border-style: solid;"
                                  "border-width: 3px;"
                                  "border-color: rgba(255, 255, 255, 1);"
                                  "border-radius: 8px")
        self.Slabel.setGraphicsEffect(eff)
        self.Slabel.setAlignment(Qt.AlignCenter)
        self.Slabel.raise_()

        eff2 = QGraphicsDropShadowEffect()
        eff2.setOffset(2, 1)
        eff2.setBlurRadius(20)
        eff2.setColor(Qt.red)

        self.Slabe2 = QLabel('', self.centralwidget)
        self.Slabe2.setText('1분 후 운동이 다시 시작됩니다.')
        self.Slabe2.setGeometry(320, 370, 400, 2400)
        self.Slabe2.setStyleSheet("color: rgba(255, 255, 255, 1);"
                                  "line-height:1.5px;"
                                  "font: 20pt \"배달의민족 도현\";\n"
                                  "border-style: solid;"
                                  "border-width: 0px;"
                                  "border-color: rgba(255, 255, 255, 1);"
                                  "border-radius: 8px")
        self.Slabe2.setGraphicsEffect(eff2)
        self.Slabe2.setAlignment(Qt.AlignCenter)
        self.Slabe2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1.0)
        self.setAutoFillBackground(False)
        self.timer = QTimer(self)

        # 시작위치@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.startUIWindow1()

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def clickcheck(self):
        global a_a
        if a_a == 0:
            self.UItab3.Slabel2.setVisible(True)
        else:
            self.startUIWindow4()

    def startUIWindow1(self):
        self.close()

        self.UIFlag = 1
        self.UItab1 = UIWindow1()
        self.UItab1.setupUI(self)
        self.UItab1.pushButton2.clicked.connect(self.startUIWindow2)
        self.show()

    def startUIWindow2(self):
        objectinfo("Stop")
        self.close()
        self.UIFlag = 2
        self.UItab2 = UIWindow2()
        self.UItab2.setupUI(self)
        self.UItab2.pushButton1.clicked.connect(self.UItab2.clickMethod4)
        self.UItab2.pushButton1.clicked.connect(self.startUIWindow3)
        self.UItab2.pushButton2.clicked.connect(self.UItab2.clickMethod5)
        self.UItab2.pushButton2.clicked.connect(self.startUIWindow3)
        self.UItab2.pushButton4.clicked.connect(self.startUIWindow1)
        self.UItab2.pushButton6.clicked.connect(lambda: objectinfo("RotateLeft"))
        self.UItab2.pushButton7.clicked.connect(lambda: objectinfo("RotateRight"))
        self.show()

    def startUIWindow3(self):
        self.close()

        self.UIFlag = 3
        self.UItab3 = UIWindow3()
        self.UItab3.setupUI(self)
        self.UItab3.pushButton1.clicked.connect(self.UItab3.clickMethod1)
        self.UItab3.pushButton2.clicked.connect(self.UItab3.clickMethod2)
        self.UItab3.pushButton3.clicked.connect(self.UItab3.clickMethod3)
        self.UItab3.pushButton4.clicked.connect(self.clickcheck)
        self.UItab3.pushButton5.clicked.connect(self.startUIWindow2)
        self.UItab3.pushButton6.clicked.connect(lambda: objectinfo("RotateLeft"))
        self.UItab3.pushButton7.clicked.connect(lambda: objectinfo("RotateRight"))
        self.show()

    def startUIWindow4(self):
        self.close()
        self.UIFlag = 4
        self.UItab4 = UIWindow4()
        self.UItab4.setupUI(self)
        self.UItab4.pushButton4.clicked.connect(lambda: self.UItab4.test.setVisible(True))
        self.UItab4.pushButton4.clicked.connect(self.UItab4.e_gif.start)
        self.UItab4.pushButton5.clicked.connect(self.timer.stop)
        # self.UItab4.pushButton5.clicked.connect(self.timer.)
        self.UItab4.pushButton5.clicked.connect(self.startUIWindow3)
        self.UItab4.pushButton6.clicked.connect(lambda: objectinfo("RotateLeft"))
        self.UItab4.pushButton7.clicked.connect(lambda: objectinfo("RotateRight"))
        self.UItab4.e_gif.finished.connect(self.startUIWindow5)

        self.show()

    def startUIWindow5(self):
        objectinfo(b_b + str(a_a))
        self.close()
        self.UIFlag = 5
        self.UItab5 = UIWindow5()
        self.UItab5.setupUI(self)
        self.UItab5.pushButton2.clicked.connect(self.UItab5.f_gif.stop)
        self.UItab5.pushButton2.clicked.connect(self.startUIWindow3)
        self.UItab5.pushButton6.clicked.connect(lambda: objectinfo("RotateLeft"))
        self.UItab5.pushButton7.clicked.connect(lambda: objectinfo("RotateRight"))
        self.show()
        self.UItab5.f_gif.finished.connect(self.startUIWindow6)

    def startUIWindow6(self):
        objectinfo("Stop")
        self.close()
        self.UIFlag = 6
        self.UItab6 = UIWindow6()
        self.UItab6.setupUI(self)
        self.UItab6.pushButton2.clicked.connect(self.UItab6.f_gif.stop)  # 운동종료
        self.UItab6.pushButton2.clicked.connect(self.startUIWindow1)

        self.UItab6.pushButton3.clicked.connect(self.UItab6.f_gif.stop)  # 다시시작
        self.UItab6.pushButton3.clicked.connect(self.startUIWindow4)
        self.show()
        self.UItab6.f_gif.finished.connect(self.startUIWindow4)

    def select_button(self, arg):
        self.str1 = "UItab" + str(UIflag)
        self.str2 = "pushButton" + str(arg + 1)
        self.choose = getattr(self, self.str1)
        self.choose = getattr(self.choose, self.str2)
        self.choose.click()
