import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, Qt
from PySide2 import QtCore, QtWidgets, QtGui

from ui_mainwindow import Ui_MainWindow
from time import sleep


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.resize(321,180)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.groupBox.setVisible(False)
        self.ui.btn_send_answ.clicked.connect(self.send_answer_and_start_program)
        self.ui.btn_open_settings.clicked.connect(self.settings_open)
        self.ui.btn_clear_textboxs.clicked.connect(self.clear_text_boxes)

        # Init params
        self.send_ans = False
        self.status_open_settings = False

    def send_answer_and_start_program(self):
        self.ui.groupBox_2.setVisible(False)
        self.ui.groupBox.setVisible(True)
        self.ui.groupBox.geometry()
        # self.resize(343,319)
        geom = self.ui.groupBox.geometry()
        geom.setX(0)
        geom.setY(0)
        self.ui.groupBox.setGeometry(geom)
        self.send_ans = True

    def settings_open(self):
        if self.status_open_settings:
            self.ui.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▼", None, -1))
            self.status_open_settings = False
            self.resize(321, 180)
        else:
            self.ui.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▲", None, -1))
            self.status_open_settings = True
            self.resize(321, 285)

    @staticmethod
    def message_box():
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Information)
        box.setWindowTitle('Внимание!')
        box.setText('Вы уверены, что хотите очистить\nтестовые поля?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        buttonY = box.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('Да')
        buttonN = box.button(QtWidgets.QMessageBox.No)
        buttonN.setText('Нет')
        box.exec_()
        if box.clickedButton() == buttonY:
            return 1
        elif box.clickedButton() == buttonN:
            return 0

    def clear_text_boxes(self):
        result = self.message_box()
        if result == 1:
            self.ui.textbox_email.setText("")
            self.ui.textbox_password.setText("")
            self.ui.textbox_add_inf.setText("")

    def add_new_record(self):
        ...

    def delete_exist_record(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
