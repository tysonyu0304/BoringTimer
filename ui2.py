# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiAMgyBB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7121\u804a\u8a08\u6642\u5668", None))
        self.text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button2.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

