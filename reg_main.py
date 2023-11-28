from PySide6 import QtWidgets, QtCore  # Импорт пакета, который содержит виджеты
from ui.reg_form import Ui_reg_Form




class RegWindow(QtWidgets.QWidget):
    registred = QtCore.Signal(tuple)
    def __init__(self, parent=None):
        super().__init__(parent)
        print("window2 print")
        self.ui = Ui_reg_Form()
        self.ui.setupUi(self)
        self.__initSignal()

        # self.ui.pushButton_OK.clicked.connect(
        #     lambda: print("confirmed") if self.ui.lineEdit_psw_cnf.text() == self.ui.lineEdit_psw.text() else print(
        #         "try again"))
        # self.ui.pushButton_OK.clicked.connect(print(str_))
    def __initSignal(self):
        self.ui.pushButton_OK.clicked.connect(
            self.__onPushButtonRegClicked)

    def __onPushButtonRegClicked(self):

        __login_ = self.ui.lineEdit_log.text()
        __passwrd = self.ui.lineEdit_psw.text()
        __pswrdCnf = self.ui.lineEdit_psw_cnf.text()
        if len(__login_) == 0:
            QtWidgets.QMessageBox.warning(self, "try again", "login is empty")
        elif len(__passwrd) == 0:
            QtWidgets.QMessageBox.warning(self, "try again", "password is empty")
        elif __passwrd != __pswrdCnf:
            QtWidgets.QMessageBox.warning(self,"try again", "password differs from confirmation" )
            str_ = "try again"
            print(str_)
        else:
            str_ = f"confirmed, login {__login_}, password {__passwrd}"
            self.ui.pushButton_OK.clicked.connect( print(str_))
            self.registred.emit((__login_, __passwrd))
            self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    wnd2 = RegWindow()
    wnd2.show()
    app.exec_()
# cd ui
#
# PySide6-uic login.ui -o login.py
