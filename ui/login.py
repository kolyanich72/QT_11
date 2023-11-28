# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(215, 200)
        Form.setMinimumSize(QSize(215, 160))
        Form.setMaximumSize(QSize(250, 200))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 30))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdi_login = QLineEdit(Form)
        self.lineEdi_login.setObjectName(u"lineEdi_login")

        self.horizontalLayout.addWidget(self.lineEdi_login)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(55, 30))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_passwrd = QLineEdit(Form)
        self.lineEdit_passwrd.setObjectName(u"lineEdit_passwrd")
        self.lineEdit_passwrd.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.lineEdit_passwrd)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox_autoLogin = QCheckBox(Form)
        self.checkBox_autoLogin.setObjectName(u"checkBox_autoLogin")

        self.verticalLayout.addWidget(self.checkBox_autoLogin)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_OK = QPushButton(Form)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.horizontalLayout_4.addWidget(self.pushButton_OK)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_restr_pswrd = QPushButton(Form)
        self.pushButton_restr_pswrd.setObjectName(u"pushButton_restr_pswrd")
        self.pushButton_restr_pswrd.setText(u"restore password")

        self.horizontalLayout_3.addWidget(self.pushButton_restr_pswrd)

        self.pushButton_regstrn = QPushButton(Form)
        self.pushButton_regstrn.setObjectName(u"pushButton_regstrn")

        self.horizontalLayout_3.addWidget(self.pushButton_regstrn)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Enter", None))
        self.label.setText(QCoreApplication.translate("Form", u"login", None))
        self.lineEdi_login.setPlaceholderText(QCoreApplication.translate("Form", u"enter login", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"password", None))
        self.lineEdit_passwrd.setPlaceholderText(QCoreApplication.translate("Form", u"enter password", None))
        self.checkBox_autoLogin.setText(QCoreApplication.translate("Form", u"auto enter", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_regstrn.setText(QCoreApplication.translate("Form", u"Registration", None))
    # retranslateUi
