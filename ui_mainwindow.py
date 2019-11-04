# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Mon Nov  4 01:25:48 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(321, 183)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("/*\n"
"Material Dark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Inspired on https://github.com/jxfwinter/qt-material-stylesheet\n"
"Company: GTRONICK\n"
"Last updated: 04/12/2018, 15:00.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/MaterialDark.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"QGroupBox{\n"
"    border: #04b97f\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_second = QtWidgets.QGroupBox(self.centralwidget)
        self.group_second.setEnabled(True)
        self.group_second.setGeometry(QtCore.QRect(15, 10, 321, 301))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.group_second.setFont(font)
        self.group_second.setAutoFillBackground(False)
        self.group_second.setTitle("")
        self.group_second.setFlat(False)
        self.group_second.setCheckable(False)
        self.group_second.setObjectName("group_second")
        self.btn_open_settings = QtWidgets.QPushButton(self.group_second)
        self.btn_open_settings.setGeometry(QtCore.QRect(151, 150, 16, 23))
        self.btn_open_settings.setObjectName("btn_open_settings")
        self.btn_clear_textboxs = QtWidgets.QPushButton(self.group_second)
        self.btn_clear_textboxs.setGeometry(QtCore.QRect(167, 150, 111, 23))
        self.btn_clear_textboxs.setObjectName("btn_clear_textboxs")
        self.label_5 = QtWidgets.QLabel(self.group_second)
        self.label_5.setGeometry(QtCore.QRect(24, 93, 81, 16))
        self.label_5.setObjectName("label_5")
        self.textbox_password = QtWidgets.QLineEdit(self.group_second)
        self.textbox_password.setGeometry(QtCore.QRect(104, 68, 171, 20))
        self.textbox_password.setObjectName("textbox_password")
        self.btn_change_key = QtWidgets.QPushButton(self.group_second)
        self.btn_change_key.setGeometry(QtCore.QRect(74, 206, 171, 23))
        self.btn_change_key.setObjectName("btn_change_key")
        self.btn_change_data = QtWidgets.QPushButton(self.group_second)
        self.btn_change_data.setGeometry(QtCore.QRect(41, 123, 111, 23))
        self.btn_change_data.setObjectName("btn_change_data")
        self.textbox_add_inf = QtWidgets.QLineEdit(self.group_second)
        self.textbox_add_inf.setGeometry(QtCore.QRect(104, 93, 171, 20))
        self.textbox_add_inf.setObjectName("textbox_add_inf")
        self.label_6 = QtWidgets.QLabel(self.group_second)
        self.label_6.setGeometry(QtCore.QRect(24, 43, 81, 16))
        self.label_6.setObjectName("label_6")
        self.btn_buffer_pass = QtWidgets.QPushButton(self.group_second)
        self.btn_buffer_pass.setGeometry(QtCore.QRect(279, 66, 21, 23))
        self.btn_buffer_pass.setObjectName("btn_buffer_pass")
        self.btn_add_new_data = QtWidgets.QPushButton(self.group_second)
        self.btn_add_new_data.setGeometry(QtCore.QRect(167, 123, 111, 23))
        self.btn_add_new_data.setObjectName("btn_add_new_data")
        self.textbox_change_message = QtWidgets.QLineEdit(self.group_second)
        self.textbox_change_message.setGeometry(QtCore.QRect(74, 233, 171, 20))
        self.textbox_change_message.setObjectName("textbox_change_message")
        self.textbox_change_key = QtWidgets.QLineEdit(self.group_second)
        self.textbox_change_key.setGeometry(QtCore.QRect(74, 183, 171, 20))
        self.textbox_change_key.setObjectName("textbox_change_key")
        self.btn_buffer_email = QtWidgets.QPushButton(self.group_second)
        self.btn_buffer_email.setGeometry(QtCore.QRect(279, 41, 21, 23))
        self.btn_buffer_email.setObjectName("btn_buffer_email")
        self.btn_buff_add_inf = QtWidgets.QPushButton(self.group_second)
        self.btn_buff_add_inf.setGeometry(QtCore.QRect(279, 91, 21, 23))
        self.btn_buff_add_inf.setObjectName("btn_buff_add_inf")
        self.label_2 = QtWidgets.QLabel(self.group_second)
        self.label_2.setGeometry(QtCore.QRect(24, 18, 81, 16))
        self.label_2.setObjectName("label_2")
        self.btn_delete_data = QtWidgets.QPushButton(self.group_second)
        self.btn_delete_data.setGeometry(QtCore.QRect(41, 150, 111, 23))
        self.btn_delete_data.setObjectName("btn_delete_data")
        self.textbox_email = QtWidgets.QLineEdit(self.group_second)
        self.textbox_email.setGeometry(QtCore.QRect(104, 43, 171, 20))
        self.textbox_email.setObjectName("textbox_email")
        self.btn_exit = QtWidgets.QPushButton(self.group_second)
        self.btn_exit.setGeometry(QtCore.QRect(279, 128, 21, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_export_data = QtWidgets.QPushButton(self.group_second)
        self.btn_export_data.setGeometry(QtCore.QRect(19, 128, 21, 41))
        self.btn_export_data.setObjectName("btn_export_data")
        self.label_4 = QtWidgets.QLabel(self.group_second)
        self.label_4.setGeometry(QtCore.QRect(24, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.btn_change_message = QtWidgets.QPushButton(self.group_second)
        self.btn_change_message.setGeometry(QtCore.QRect(74, 256, 171, 23))
        self.btn_change_message.setObjectName("btn_change_message")
        self.comboBox_check = QtWidgets.QComboBox(self.group_second)
        self.comboBox_check.setGeometry(QtCore.QRect(104, 18, 171, 22))
        self.comboBox_check.setObjectName("comboBox_check")
        self.group_first = QtWidgets.QGroupBox(self.centralwidget)
        self.group_first.setGeometry(QtCore.QRect(15, 10, 291, 171))
        font = QtGui.QFont()
        self.group_first.setFont(font)
        self.group_first.setFocusPolicy(QtCore.Qt.NoFocus)
        self.group_first.setToolTip("")
        self.group_first.setTitle("")
        self.group_first.setFlat(False)
        self.group_first.setCheckable(False)
        self.group_first.setObjectName("group_first")
        self.btn_send_answ = QtWidgets.QPushButton(self.group_first)
        self.btn_send_answ.setGeometry(QtCore.QRect(10, 100, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_send_answ.setFont(font)
        self.btn_send_answ.setObjectName("btn_send_answ")
        self.textbox_question = QtWidgets.QLineEdit(self.group_first)
        self.textbox_question.setGeometry(QtCore.QRect(10, 40, 271, 21))
        self.textbox_question.setObjectName("textbox_question")
        self.textbox_answer = QtWidgets.QLineEdit(self.group_first)
        self.textbox_answer.setGeometry(QtCore.QRect(10, 70, 271, 21))
        self.textbox_answer.setObjectName("textbox_answer")
        self.label = QtWidgets.QLabel(self.group_first)
        self.label.setGeometry(QtCore.QRect(80, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▼", None, -1))
        self.btn_clear_textboxs.setText(QtWidgets.QApplication.translate("MainWindow", "Очистить поля", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Доп. инфор:", None, -1))
        self.btn_change_key.setText(QtWidgets.QApplication.translate("MainWindow", "Сменить ключ", None, -1))
        self.btn_change_data.setText(QtWidgets.QApplication.translate("MainWindow", "Изменить", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "E-mail/login:", None, -1))
        self.btn_buffer_pass.setText(QtWidgets.QApplication.translate("MainWindow", "K", None, -1))
        self.btn_add_new_data.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.btn_buffer_email.setText(QtWidgets.QApplication.translate("MainWindow", "K", None, -1))
        self.btn_buff_add_inf.setText(QtWidgets.QApplication.translate("MainWindow", "K", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Тип аккаунта:", None, -1))
        self.btn_delete_data.setText(QtWidgets.QApplication.translate("MainWindow", "Удалить запись", None, -1))
        self.btn_exit.setText(QtWidgets.QApplication.translate("MainWindow", "Х", None, -1))
        self.btn_export_data.setText(QtWidgets.QApplication.translate("MainWindow", "ЭК", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.btn_change_message.setText(QtWidgets.QApplication.translate("MainWindow", "Сменить подсказку", None, -1))
        self.btn_send_answ.setText(QtWidgets.QApplication.translate("MainWindow", "Отправить ответ", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Ответьте на вопрос?", None, -1))

