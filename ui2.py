# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui2.ui'
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
        Form.resize(360, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(360, 160))
        Form.setMaximumSize(QSize(360, 160))
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 9, 341, 141))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayoutWidget = QWidget(self.tab_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 301, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_3 = QLabel(self.verticalLayoutWidget)
        self.text_3.setObjectName(u"text_3")
        self.text_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text_3)

        self.button_3 = QPushButton(self.verticalLayoutWidget)
        self.button_3.setObjectName(u"button_3")

        self.verticalLayout.addWidget(self.button_3)

        self.button2_3 = QPushButton(self.verticalLayoutWidget)
        self.button2_3.setObjectName(u"button2_3")

        self.verticalLayout.addWidget(self.button2_3)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 331, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget_2)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 27))
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.counter = QLabel(self.verticalLayoutWidget_2)
        self.counter.setObjectName(u"counter")
        self.counter.setMaximumSize(QSize(16777215, 27))
        self.counter.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.counter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(45, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.hour_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.hour_spinBox.setObjectName(u"hour_spinBox")
        self.hour_spinBox.setMaximumSize(QSize(57, 16777215))
        self.hour_spinBox.setRange(0, 24)

        self.horizontalLayout.addWidget(self.hour_spinBox)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(45, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.minute_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.minute_spinBox.setObjectName(u"minute_spinBox")
        self.minute_spinBox.setMaximumSize(QSize(57, 16777215))
        self.minute_spinBox.setRange(0, 59)

        self.horizontalLayout.addWidget(self.minute_spinBox)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(45, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.second_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.second_spinBox.setObjectName(u"second_spinBox")
        self.second_spinBox.setMaximumSize(QSize(57, 16777215))
        self.second_spinBox.setRange(0, 59)

        self.horizontalLayout.addWidget(self.second_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_tab2 = QPushButton(self.verticalLayoutWidget_2)
        self.button_tab2.setObjectName(u"button_tab2")

        self.horizontalLayout_2.addWidget(self.button_tab2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7121\u804a\u8a08\u6642\u5668", None))
        self.text_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button2_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u7121\u804a\u78bc\u8868", None))
        self.title.setText(QCoreApplication.translate("Form", u"無聊倒數計時  在下面設定時間吧", None))
        self.counter.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5c0f\u6642", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5206\u9418", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u79d2", None))
        self.button_tab2.setText(QCoreApplication.translate("Form", u"開始倒數", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u7121\u804a\u8a08\u6642", None))
    # retranslateUi
