import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, Qt
from PySide2 import QtCore, QtWidgets, QtGui

from ui_mainwindow import Ui_MainWindow
from time import sleep
from backend import Backend
import inspect


class MainWindow(QMainWindow, Backend):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(321, 183)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(self, Qt.MSWindowsFixedSizeDialogHint)
        self.ui.group_second.setVisible(False)
        self.ui.btn_send_answ.clicked.connect(self.send_answer_and_start_program)
        self.ui.btn_open_settings.clicked.connect(self.settings_open)
        self.ui.btn_clear_textboxs.clicked.connect(self.clear_text_boxes)
        # self.ui.textbox_answer.setText("Ключ")
        self.ui.comboBox_check.setEditable(True)

        # Init params
        self.send_ans = False
        self.status_open_settings = False
        self.choice_account = '<Выберите аккаунт>'

        self.ui.textbox_question.setReadOnly(True)

        # Init from Backend
        self.back_end = Backend(self)

        self.ui.textbox_question.setText(self.back_end.text_question())
        self.ui.btn_change_data.clicked.connect(self.back_end.change_data)
        self.ui.btn_add_new_data.clicked.connect(self.back_end.add_data)
        self.ui.btn_delete_data.clicked.connect(self.back_end.del_acc)
        self.ui.btn_change_key.clicked.connect(self.back_end.change_key)
        self.ui.btn_change_message.clicked.connect(self.back_end.change_message_fun)
        self.ui.btn_export_data.clicked.connect(self.back_end.ex_cop)
        self.ui.btn_exit.clicked.connect(self.back_end.exit_fun)
        self.ui.btn_buffer_email.clicked.connect(self.buffer_email_textbox)
        self.ui.btn_buffer_pass.clicked.connect(self.buffer_pass_textbox)
        self.ui.btn_buff_add_inf.clicked.connect(self.buffer_inf_textbox)
        self.ui.textbox_answer.textEdited.connect(self.loop_check_edited_textbox_answer)
        self.loop_check_edited_textbox_answer()
        self.ui.textbox_change_message.textEdited.connect(self.loop_check_edited_textbox_change_message)
        self.loop_check_edited_textbox_change_message()
        self.ui.textbox_change_key.textEdited.connect(self.loop_check_edited_textbox_change_key)
        self.loop_check_edited_textbox_change_key()

    @staticmethod
    def move2RightBottomCorner(win):
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (win.frameSize().width(), win.frameSize().height())
        x = screen_size[0]/2
        y = screen_size[1]/2
        win.move(x, y)

    def loop_check_edited_textbox_answer(self):
        text = self.ui.textbox_answer.text()
        if text != "":
            self.ui.btn_send_answ.setEnabled(True)
        else:
            self.ui.btn_send_answ.setEnabled(False)

    def loop_check_edited_textbox_change_message(self):
        text = self.ui.textbox_change_message.text()
        if text != "":
            self.ui.btn_change_message.setEnabled(True)
        else:
            self.ui.btn_change_message.setEnabled(False)

    def loop_check_edited_textbox_change_key(self):
        text = self.ui.textbox_change_key.text()
        if text != "":
            self.ui.btn_change_key.setEnabled(True)
        else:
            self.ui.btn_change_key.setEnabled(False)

    def buffer_email_textbox(self):
        clipboard = QApplication.clipboard()
        clipboard.text()
        clipboard.setText(self.ui.textbox_email.text())

    def buffer_pass_textbox(self):
        clipboard = QApplication.clipboard()
        clipboard.text()
        clipboard.setText(self.ui.textbox_password.text())

    def buffer_inf_textbox(self):
        clipboard = QApplication.clipboard()
        clipboard.text()
        clipboard.setText(self.ui.textbox_add_inf.text())

    def init_combobox(self):
        if self.choice_account not in self.ui.comboBox_check.currentText():
            self.ui.textbox_password.setEnabled(True)
            self.ui.textbox_email.setEnabled(True)
            self.ui.textbox_add_inf.setEnabled(True)
            if self.ui.comboBox_check.currentText() in self.back_end.name_keys:
                self.back_end.select = self.ui.comboBox_check.currentText()
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
            self.setFixedSize(321, 180)
        else:
            self.ui.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▲", None, -1))
            self.status_open_settings = True
            self.setFixedSize(321, 285)

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

    def message_box_error(self, title: str, message: str):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Critical)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        buttonY = box.button(QtWidgets.QMessageBox.Ok)
        buttonY.setText('Ок')
        box.exec_()
        if box.clickedButton() == buttonY:
            return 1

    def message_box_warnning(self, title: str, message: str):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        buttonY = box.button(QtWidgets.QMessageBox.Ok)
        buttonY.setText('Ок')
        box.exec_()
        if box.clickedButton() == buttonY:
            return 1

    def message_box_information(self, title: str, message: str):
        box = QtWidgets.QMessageBox(self)
        box.setIcon(QtWidgets.QMessageBox.Information)
        box.setWindowTitle(title)
        box.setText(message)
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
            self.back_end.select=self.choice_account

    def closeEvent(self, event: QtGui.QCloseEvent):
        self.back_end.exit_fun(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.move(window.width()*-3,0)
    window.move(0,0)
    window.show()
    window.move2RightBottomCorner(window)
    sys.exit(app.exec_())
