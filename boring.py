import sys, webbrowser
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from ui2 import Ui_Form

i = 0
On = 1

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 160)
        Form.setMinimumSize(QSize(320, 160))
        Form.setMaximumSize(QSize(320, 160))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 241, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text = QLabel(self.verticalLayoutWidget)
        self.text.setObjectName(u"text")
        self.text.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.text)
        self.button = QPushButton(self.verticalLayoutWidget)
        self.button.setObjectName(u"button")
        self.verticalLayout.addWidget(self.button)
        self.button2 = QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName(u"button2")
        self.verticalLayout.addWidget(self.button2)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7121\u804a\u8a08\u6642\u5668", None))
        self.text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button2.setText(QCoreApplication.translate("Form", u"PushButton", None))

def format(s, m, h):
    if s > 60:
        m = s // 60
        s = s % 60
    else: m = 0
    if m > 60:
        h = m // 60
        m = m % 60
    else: h = 0
    return s, m, h
    
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.text.setText("我無聊了 0 秒")
        self.ui.button.setText("我現在不無聊了")
        self.ui.button2.setText("有趣一下")
        self.timer_counter = 0
        self.setupControl()
        self.ui.button.clicked.connect(self.click)
        self.ui.button2.clicked.connect(self.b2)
        print("RUN")

    def setupControl(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.main)
        if On == 1:
            self.timer.start(1000)
        elif On == -1: self.timer.stop()

    def main(self):
        global i
        i = i + 1
        s, m, h = format(i, 0, 0)
        if h == 0 and m == 0:
            text = f"我無聊了 {s} 秒"
        elif h == 0 and m !=0:
            text = f"我無聊了 {m} 分 {s} 秒"
        else: text = f"我無聊了 {h} 小時 {m} 分 {s} 秒"
        self.ui.text.setText(text)
        self.timer_counter += 1
        if On == 1:
            self.timer.start(1000)
        elif On == -1: self.timer.stop()
            
    def click(self):
        global On
        print("click")
        if On == 1: self.ui.button.setText("我又無聊了")
        else: self.ui.button.setText("我現在不無聊了")
        On = -On
        self.timer_counter -= 1
        self.main()

    def b2(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

