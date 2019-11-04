import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, Qt
from PySide2 import QtCore, QtWidgets, QtGui

from ui_mainwindow import Ui_MainWindow
from time import sleep
from backend import Backend


class MainWindow(QMainWindow, Backend):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.group_second.setVisible(False)
        self.ui.btn_send_answ.clicked.connect(self.send_answer_and_start_program)
        self.ui.btn_open_settings.clicked.connect(self.settings_open)
        self.ui.btn_clear_textboxs.clicked.connect(self.clear_text_boxes)
        self.ui.textbox_answer.setText("Ключ")
        self.ui.comboBox_check.setEditable(True)

        # Init params
        self.send_ans = False
        self.status_open_settings = False
        self.choice_account = '<Выберите аккаунт>'

        self.ui.textbox_question.setReadOnly(True)


        # with open('bin/ini') as file:
        #     self.ui.textbox_question.setText(file.read())

        # Init from Backend
        self.back_end = Backend(self)

        self.ui.textbox_question.setText(self.back_end.text_question())
        self.ui.btn_change_data.clicked.connect(self.back_end.change_data)
        self.ui.btn_add_new_data.clicked.connect(self.back_end.add_data)
        self.ui.btn_delete_data.clicked.connect(self.back_end.del_acc)

    def init_combobox(self):
        if self.choice_account not in self.ui.comboBox_check.currentText():
            print(self.ui.comboBox_check.currentText())
            self.ui.textbox_password.setEnabled(True)
            self.ui.textbox_email.setEnabled(True)
            self.ui.textbox_add_inf.setEnabled(True)
            self.back_end.inizil_data()

    def send_answer_and_start_program(self):
        # self.message_box_warnning(title="Внимание!",question='Настоятельно рекомендуется поменять\nключ шифрования на cвой, особый!')
        self.back_end.main_funn()

        self.ui.group_first.setVisible(False)
        self.ui.group_second.setVisible(True)
        self.ui.group_second.geometry()
        # self.resize(343,319)
        geom = self.ui.group_second.geometry()
        geom.setX(0)
        geom.setY(0)
        self.ui.group_second.setGeometry(geom)
        self.send_ans = True
        self.ui.comboBox_check.currentTextChanged.connect(self.init_combobox)

    def settings_open(self):
        if self.status_open_settings:
            self.ui.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▼", None, -1))
            self.status_open_settings = False
            self.resize(321, 180)
        else:
            self.ui.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▲", None, -1))
            self.status_open_settings = True
            self.resize(321, 285)

    def message_box_yes_no(self, title: str='Внимание!', message: str='Вы уверены, что хотите очистить\nтестовые поля?'):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Information)
        box.setWindowTitle(title)
        box.setText(message)
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

    def message_box_warnning(self, title: str, question: str):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(question)
        box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        buttonY = box.button(QtWidgets.QMessageBox.Ok)
        buttonY.setText('Ок')
        box.exec_()
        if box.clickedButton() == buttonY:
            return 1

    def clear_text_boxes(self):
        result = self.message_box_yes_no()
        if result == 1:
            self.ui.textbox_email.setText("")
            self.ui.textbox_password.setText("")
            self.ui.textbox_add_inf.setText("")
            self.ui.comboBox_check.setEditText(self.choice_account)

    def add_new_record(self):
        ...

    def delete_exist_record(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
