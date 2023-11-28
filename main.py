from PySide6 import QtWidgets  # Импорт пакета, который содержит виджеты
from ui.login import Ui_Form
from reg_main import RegWindow


def authenticate(log_, passwrd):
    return DB[log_] == passwrd  # True / False по ключу "логин" - пароль


class Mfwindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        #  print("window print")
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.__reg_window.show()

        self.__initUI()
        self.__initSignal()

    def __initUI(self):
        self.ui.lineEdit_passwrd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def __initSignal(self):
        self.ui.pushButton_OK.clicked.connect(
            self.__onPushButtonLoginConnect)
        #  self.ui.pushButton_regstrn.clicked.connect(self.__reg_window.show)
        self.ui.pushButton_regstrn.clicked.connect(self.__reg_clicked)  # (self.__onPushButtonRegClicked)

    ## self.__onPushButtonLoginConnect - правильно
    # self.__onPushButtonLoginConnect() - НЕПРАВИЛЬНО
    def __onPushButtonRegClicked(self):

        self.__reg_window = RegWindow()
        self.__reg_window.registred.connect(self._fromRegForm)
        self.__reg_window.ui.lineEdit_log.setText(self.ui.lineEdi_login.text())
        self.__reg_window.show()

    def _fromRegForm(self, data):
        self.ui.lineEdi_login.setText(data[0])
        self.ui.lineEdit_passwrd.setText(data[1])

        DB[data[0]] = data[1]
        print(DB)

    def __reg_clicked(self):
        #  self.close()
        self.__onPushButtonRegClicked()

    def __onPushButtonLoginConnect(self):

        __login_ = self.ui.lineEdi_login.text()
        __passwrd = self.ui.lineEdit_passwrd.text()

        try:
            auth_ = authenticate(__login_, __passwrd)
        except KeyError:
            QtWidgets.QMessageBox.warning(self, "Error", "wrong login")
            return

        if auth_:

            QtWidgets.QMessageBox.about(self, "welcome", __login_)
            # QtWidgets.QMessageBox.warning(self,"Hi!",__login_ )
            # print(f"welcome {__login_}")
            self.close()
            return
        QtWidgets.QMessageBox.warning(self, "Error", "try again")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    wnd = Mfwindow()
    wnd.show()
    DB = {"nick": "12345", "anybody": "54321"}
    app.exec_()
# cd ui
#
# PySide6-uic login.ui -o login.py
