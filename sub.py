# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sub(object):
    def setupUi(self, sub):
        if not sub.objectName():
            sub.setObjectName(u"sub")
        sub.resize(320, 100)
        sub.setMinimumSize(QSize(320, 100))
        sub.setMaximumSize(QSize(320, 100))
        self.text = QLabel(sub)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(50, 10, 221, 41))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignCenter)
        self.Button = QPushButton(sub)
        self.Button.setObjectName(u"Button")
        self.Button.setGeometry(QRect(120, 60, 75, 23))

        self.retranslateUi(sub)

        QMetaObject.connectSlotsByName(sub)
    # setupUi

    def retranslateUi(self, sub):
        sub.setWindowTitle(QCoreApplication.translate("sub", u"\u4f60\u7684\u7121\u804a\u6642\u9593\u5230\u5566", None))
        self.text.setText(QCoreApplication.translate("sub", u"\u662f\u6642\u5019\u53bb\u505a\u4e9b\u6709\u8da3\u7684\u4e8b\u4e86", None))
        self.Button.setText(QCoreApplication.translate("sub", u"\u6709\u8da3\u4e00\u4e0b", None))
    # retranslateUi

