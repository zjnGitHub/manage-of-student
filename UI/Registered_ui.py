# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registered.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_registered_Widget(object):
    def setupUi(self, registered):
        if not registered.objectName():
            registered.setObjectName(u"registered")
        registered.resize(400, 255)
        self.verticalLayout_3 = QVBoxLayout(registered)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(registered)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(registered)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_8 = QLabel(registered)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_6 = QLabel(registered)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(registered)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(registered)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_Account = QLineEdit(registered)
        self.lineEdit_Account.setObjectName(u"lineEdit_Account")

        self.horizontalLayout_2.addWidget(self.lineEdit_Account)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(registered)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_Password = QLineEdit(registered)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")

        self.horizontalLayout_3.addWidget(self.lineEdit_Password)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(registered)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_Password2 = QLineEdit(registered)
        self.lineEdit_Password2.setObjectName(u"lineEdit_Password2")

        self.horizontalLayout_4.addWidget(self.lineEdit_Password2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(registered)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_Email = QLineEdit(registered)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")

        self.horizontalLayout_5.addWidget(self.lineEdit_Email)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.PushButton_Submit = QPushButton(registered)
        self.PushButton_Submit.setObjectName(u"PushButton_Submit")
        self.PushButton_Submit.setFont(font1)

        self.horizontalLayout_7.addWidget(self.PushButton_Submit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.retranslateUi(registered)

        QMetaObject.connectSlotsByName(registered)
    # setupUi

    def retranslateUi(self, registered):
        registered.setWindowTitle(QCoreApplication.translate("registered", u"Form", None))
        self.label.setText(QCoreApplication.translate("registered", u"\u6ce8\u518c", None))
        self.label_9.setText("")
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("registered", u"\u518d\u6b21\u8f93\u5165", None))
        self.label_7.setText("")
        self.label_2.setText(QCoreApplication.translate("registered", u"\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("registered", u"\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("registered", u"\u5bc6\u7801", None))
        self.label_5.setText(QCoreApplication.translate("registered", u"\u90ae\u7bb1", None))
        self.PushButton_Submit.setText(QCoreApplication.translate("registered", u"\u786e\u5b9a", None))
    # retranslateUi

