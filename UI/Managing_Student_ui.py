# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Managing_Student.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Managing_Student_Widget(object):
    def setupUi(self, Managing_Student):
        if not Managing_Student.objectName():
            Managing_Student.setObjectName(u"Managing_Student")
        Managing_Student.resize(955, 535)
        self.Student_Table = QTableWidget(Managing_Student)
        if (self.Student_Table.columnCount() < 8):
            self.Student_Table.setColumnCount(8)
        font = QFont()
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.Student_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Student_Table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.Student_Table.rowCount() < 8):
            self.Student_Table.setRowCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Student_Table.setVerticalHeaderItem(7, __qtablewidgetitem15)
        self.Student_Table.setObjectName(u"Student_Table")
        self.Student_Table.setGeometry(QRect(10, 50, 839, 481))
        self.PushButton_screening = QPushButton(Managing_Student)
        self.PushButton_screening.setObjectName(u"PushButton_screening")
        self.PushButton_screening.setGeometry(QRect(860, 100, 81, 61))
        self.label = QLabel(Managing_Student)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 10, 181, 31))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.retranslateUi(Managing_Student)

        QMetaObject.connectSlotsByName(Managing_Student)
    # setupUi

    def retranslateUi(self, Managing_Student):
        Managing_Student.setWindowTitle(QCoreApplication.translate("Managing_Student", u"Form", None))
        ___qtablewidgetitem = self.Student_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Managing_Student", u"\u5b66\u53f7", None))
        ___qtablewidgetitem1 = self.Student_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Managing_Student", u"\u59d3\u540d", None))
        ___qtablewidgetitem2 = self.Student_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Managing_Student", u"\u6027\u522b", None))
        ___qtablewidgetitem3 = self.Student_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Managing_Student", u"\u5165\u5b66\u65f6\u95f4", None))
        ___qtablewidgetitem4 = self.Student_Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Managing_Student", u"\u4e13\u4e1a", None))
        ___qtablewidgetitem5 = self.Student_Table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Managing_Student", u"\u5b66\u9662", None))
        ___qtablewidgetitem6 = self.Student_Table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Managing_Student", u"\u671f\u4e2d\u8003", None))
        ___qtablewidgetitem7 = self.Student_Table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Managing_Student", u"\u671f\u672b\u8003", None))
        ___qtablewidgetitem8 = self.Student_Table.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Managing_Student", u"1", None))
        ___qtablewidgetitem9 = self.Student_Table.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Managing_Student", u"2", None))
        ___qtablewidgetitem10 = self.Student_Table.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Managing_Student", u"3", None))
        ___qtablewidgetitem11 = self.Student_Table.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Managing_Student", u"4", None))
        ___qtablewidgetitem12 = self.Student_Table.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Managing_Student", u"5", None))
        ___qtablewidgetitem13 = self.Student_Table.verticalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Managing_Student", u"6", None))
        ___qtablewidgetitem14 = self.Student_Table.verticalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Managing_Student", u"7", None))
        ___qtablewidgetitem15 = self.Student_Table.verticalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Managing_Student", u"8", None))
        self.PushButton_screening.setText(QCoreApplication.translate("Managing_Student", u"\u7b5b\u9009", None))
        self.label.setText(QCoreApplication.translate("Managing_Student", u"\u5b66\u751f\u4fe1\u606f\u7ba1\u7406", None))
    # retranslateUi

