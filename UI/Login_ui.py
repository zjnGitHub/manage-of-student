# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Login_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 431, 261))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Label_Account = QLabel(self.widget)
        self.Label_Account.setObjectName(u"Label_Account")
        self.Label_Account.setFont(font)

        self.horizontalLayout.addWidget(self.Label_Account)

        self.lineEdit_Account = QLineEdit(self.widget)
        self.lineEdit_Account.setObjectName(u"lineEdit_Account")

        self.horizontalLayout.addWidget(self.lineEdit_Account)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Label_PassWord = QLabel(self.widget)
        self.Label_PassWord.setObjectName(u"Label_PassWord")
        self.Label_PassWord.setFont(font)

        self.horizontalLayout_3.addWidget(self.Label_PassWord)

        self.lineEdit_PassWord = QLineEdit(self.widget)
        self.lineEdit_PassWord.setObjectName(u"lineEdit_PassWord")

        self.horizontalLayout_3.addWidget(self.lineEdit_PassWord)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.checkBox_PassWord = QCheckBox(self.widget)
        self.checkBox_PassWord.setObjectName(u"checkBox_PassWord")

        self.verticalLayout_2.addWidget(self.checkBox_PassWord)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PushButton_Login = QPushButton(self.widget)
        self.PushButton_Login.setObjectName(u"PushButton_Login")
        self.PushButton_Login.setFont(font)

        self.horizontalLayout_2.addWidget(self.PushButton_Login)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.PushButton_Register = QPushButton(self.widget)
        self.PushButton_Register.setObjectName(u"PushButton_Register")
        self.PushButton_Register.setFont(font)

        self.horizontalLayout_2.addWidget(self.PushButton_Register)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.PushButton_back = QPushButton(self.centralwidget)
        self.PushButton_back.setObjectName(u"PushButton_back")
        self.PushButton_back.setGeometry(QRect(10, 0, 75, 24))
        self.PushButton_back.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 449, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u4fe1\u606f\u7ba1\u7406\u7cfb\u7edf", None))
        self.Label_Account.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.lineEdit_Account.setText("")
        self.Label_PassWord.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.lineEdit_PassWord.setText("")
        self.checkBox_PassWord.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.PushButton_Login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.PushButton_Register.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.PushButton_back.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
    # retranslateUi

