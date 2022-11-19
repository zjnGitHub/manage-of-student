# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student.ui'
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

class Ui_Student_Widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(537, 355)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_8.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_ID = QLineEdit(Form)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.horizontalLayout_2.addWidget(self.lineEdit_ID)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_Name = QLineEdit(Form)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.horizontalLayout_3.addWidget(self.lineEdit_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_Major = QLineEdit(Form)
        self.lineEdit_Major.setObjectName(u"lineEdit_Major")

        self.horizontalLayout_4.addWidget(self.lineEdit_Major)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_Gender = QLineEdit(Form)
        self.lineEdit_Gender.setObjectName(u"lineEdit_Gender")

        self.horizontalLayout.addWidget(self.lineEdit_Gender)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_Enrollment_year = QLineEdit(Form)
        self.lineEdit_Enrollment_year.setObjectName(u"lineEdit_Enrollment_year")

        self.horizontalLayout_5.addWidget(self.lineEdit_Enrollment_year)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_College = QLineEdit(Form)
        self.lineEdit_College.setObjectName(u"lineEdit_College")

        self.horizontalLayout_6.addWidget(self.lineEdit_College)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.PushButton_submit = QPushButton(Form)
        self.PushButton_submit.setObjectName(u"PushButton_submit")
        self.PushButton_submit.setFont(font)

        self.verticalLayout_3.addWidget(self.PushButton_submit)

        self.verticalSpacer_3 = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5b66\u751f\u4fe1\u606f\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4e13\u4e1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6027\u522b", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5165\u5b66\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6240\u5c5e\u9662\u6821", None))
        self.PushButton_submit.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
    # retranslateUi

