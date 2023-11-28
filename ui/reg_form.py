# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg_form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QWidget)

class Ui_reg_Form(object):
    def setupUi(self, reg_Form):
        if not reg_Form.objectName():
            reg_Form.setObjectName(u"reg_Form")
        reg_Form.resize(285, 200)
        reg_Form.setMinimumSize(QSize(285, 200))
        reg_Form.setMaximumSize(QSize(300, 200))
        self.layoutWidget = QWidget(reg_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 253, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_log = QLabel(self.layoutWidget)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setMinimumSize(QSize(50, 40))
        self.label_log.setMaximumSize(QSize(50, 40))

        self.horizontalLayout_2.addWidget(self.label_log)

        self.lineEdit_log = QLineEdit(self.layoutWidget)
        self.lineEdit_log.setObjectName(u"lineEdit_log")
        self.lineEdit_log.setMinimumSize(QSize(195, 20))
        self.lineEdit_log.setMaximumSize(QSize(195, 20))

        self.horizontalLayout_2.addWidget(self.lineEdit_log)

        self.layoutWidget1 = QWidget(reg_Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 60, 253, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_psw = QLabel(self.layoutWidget1)
        self.label_psw.setObjectName(u"label_psw")
        self.label_psw.setMinimumSize(QSize(50, 40))
        self.label_psw.setMaximumSize(QSize(50, 40))

        self.horizontalLayout.addWidget(self.label_psw)

        self.lineEdit_psw = QLineEdit(self.layoutWidget1)
        self.lineEdit_psw.setObjectName(u"lineEdit_psw")
        self.lineEdit_psw.setMinimumSize(QSize(195, 20))
        self.lineEdit_psw.setMaximumSize(QSize(195, 20))
        self.lineEdit_psw.setEchoMode(QLineEdit.Password)
        self.lineEdit_psw.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_psw)

        self.layoutWidget2 = QWidget(reg_Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 110, 253, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_psw_cnf = QLabel(self.layoutWidget2)
        self.label_psw_cnf.setObjectName(u"label_psw_cnf")
        self.label_psw_cnf.setMinimumSize(QSize(50, 40))
        self.label_psw_cnf.setMaximumSize(QSize(50, 40))

        self.horizontalLayout_3.addWidget(self.label_psw_cnf)

        self.lineEdit_psw_cnf = QLineEdit(self.layoutWidget2)
        self.lineEdit_psw_cnf.setObjectName(u"lineEdit_psw_cnf")
        self.lineEdit_psw_cnf.setMinimumSize(QSize(195, 20))
        self.lineEdit_psw_cnf.setMaximumSize(QSize(195, 20))
        self.lineEdit_psw_cnf.setEchoMode(QLineEdit.Password)
        self.lineEdit_psw_cnf.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_psw_cnf)

        self.widget = QWidget(reg_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 160, 158, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_OK = QPushButton(self.widget)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.horizontalLayout_4.addWidget(self.pushButton_OK)

        self.pushButton_cncl = QPushButton(self.widget)
        self.pushButton_cncl.setObjectName(u"pushButton_cncl")

        self.horizontalLayout_4.addWidget(self.pushButton_cncl)


        self.retranslateUi1(reg_Form)

        QMetaObject.connectSlotsByName(reg_Form)
    # setupUi

    def retranslateUi1(self, reg_Form):
        reg_Form.setWindowTitle(QCoreApplication.translate("reg_Form", u"Form", None))
        self.label_log.setText(QCoreApplication.translate("reg_Form", u"login", None))
        self.lineEdit_log.setText("")
        self.lineEdit_log.setPlaceholderText(QCoreApplication.translate("reg_Form", u"enter login", None))
        self.label_psw.setText(QCoreApplication.translate("reg_Form", u"password", None))
        self.lineEdit_psw.setText("")
        self.lineEdit_psw.setPlaceholderText(QCoreApplication.translate("reg_Form", u"enter password", None))
        self.label_psw_cnf.setText(QCoreApplication.translate("reg_Form", u"confirm", None))
        self.lineEdit_psw_cnf.setText("")
        self.lineEdit_psw_cnf.setPlaceholderText(QCoreApplication.translate("reg_Form", u"enter password", None))
        self.pushButton_OK.setText(QCoreApplication.translate("reg_Form", u"OK", None))
        self.pushButton_cncl.setText(QCoreApplication.translate("reg_Form", u"cancel", None))
    # retranslateUi

