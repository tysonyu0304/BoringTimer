from fileinput import close
import sys, webbrowser
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui2 import Ui_Form
from sub import Ui_sub

i = 0
On = -1

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
        self.sub = SubWindow()
        self.ui.setupUi(self)
        self.ui.text_3.setText("我無聊了 0 秒")
        self.ui.button_3.setText("我現在無聊了")
        self.ui.button2_3.setText("有趣一下")
        self.ui.counter.setText("0:00:00")
        self.timer_counter = 0
        self.setupControl()
        self.Timer2_control()
        self.ui.button_3.clicked.connect(self.click)
        self.ui.button2_3.clicked.connect(self.b2)
        self.ui.button_tab2.clicked.connect(self.start)
        print("RUN")
        self.timeout = False
        self.time = 0
        self.timer2_count = 1

    def setupControl(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.main1)
        if On == 1:
            self.timer.start(1000)
        elif On == -1: self.timer.stop()
        self.timer2 = QTimer()

    def Timer2_control(self):
        self.timer2.start(1000)
        self.timer2.timeout.connect(self.countdown(self.time))
        if self.timer2_count >= self.time:
            self.Istime()
            self.timer2.stop()

    def main1(self):
        global i
        i = i + 1
        s, m, h = format(i, 0, 0)
        if h == 0 and m == 0:
            text = f"我無聊了 {s} 秒"
        elif h == 0 and m !=0:
            text = f"我無聊了 {m} 分 {s} 秒"
        else: text = f"我無聊了 {h} 小時 {m} 分 {s} 秒"
        self.ui.text_3.setText(text)
        self.timer_counter += 1
        if On == 1:
            self.timer.start(1000)
        elif On == -1: self.timer.stop()
            
    def click(self):
        global On
        print("click")
        if On == 1: self.ui.button_3.setText("我又無聊了")
        else: self.ui.button_3.setText("我現在不無聊了")
        On = -On
        self.timer_counter -= 1
        self.main1()

    def b2(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def start(self):
        h = self.ui.hour_spinBox.value()
        m = self.ui.minute_spinBox.value()
        s = self.ui.second_spinBox.value()
        self.time = int(h) * 3600 + int(m) * 60 + int(s)
        self.timer2_count = 0
    
    def countdown(self, time):
        self.timer2_count += 1
        time - self.timer2_count
        s, m, h = format(time, 0, 0)
        self.ui.counter.setText(f"{h}:{m}:{s}")

    def Istime(self):
        self.sub.show()
        self.timeout = True

class SubWindow(QWidget):
    def __init__(self):
        super(SubWindow, self).__init__(None)
        self.subui = Ui_sub()
        self.subui.setupUi(self)
        self.subui.Button.clicked.connect(self.Fun)

    def Fun(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.close()
       
    def closeEvent(self, event):
        MainWindow().timeout = False
        MainWindow().timer2.stop()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

