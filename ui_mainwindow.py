# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui',
# licensing of 'design.ui' applies.
#
# Created: Wed Nov  6 22:36:21 2019
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
"Ubuntu Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 09/10/2019 (dd/mm/yyyy), 12:31.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Ubuntu.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QCheckBox {\n"
"    padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"      background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color:rgb(246, 134, 86);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #ffffff;\n"
"    color: rgb(81,72,65);\n"
"    selection-color:rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color:rgb(81,72,65);    \n"
"    background: #ffffff;\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color:  #1e1d23;    \n"
"    background: #ffffff;\n"
"}\n"
"QDateTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDateEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QGroupBox{\n"
"    border: #04b97f\n"
"}\n"
"QFontComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QLabel {\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255,255,255);\n"
"    selection-background-color:rgb(236,116,64);\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QMenuBar {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top:4px;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    padding-top:2px;\n"
"    padding-left:2px;\n"
"    padding-right:2px;\n"
"    border-top-width:2px;\n"
"    border-left-width:2px;\n"
"    border-right-width:2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-style:solid;\n"
"    background-color:rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-style: inset;\n"
"    border-color: rgb(150,150,150);\n"
"    background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style: solid;\n"
"    border-radius:8px;\n"
"    border-width:1px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    color:rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"     background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"      background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-color: rgb(255,150,60);\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"      border-bottom-left-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-bottom-right-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"     height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-bottom-left-radius: 3px;\n"
"      border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color:rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    padding-bottom:2px;\n"
"    padding-top:2px;\n"
"    color:rgb(81,72,65);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(247,246,246);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
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
        self.btn_open_settings.setGeometry(QtCore.QRect(148, 150, 21, 23))
        self.btn_open_settings.setObjectName("btn_open_settings")
        self.btn_clear_textboxs = QtWidgets.QPushButton(self.group_second)
        self.btn_clear_textboxs.setGeometry(QtCore.QRect(172, 150, 111, 23))
        self.btn_clear_textboxs.setObjectName("btn_clear_textboxs")
        self.label_5 = QtWidgets.QLabel(self.group_second)
        self.label_5.setGeometry(QtCore.QRect(10, 93, 91, 16))
        self.label_5.setObjectName("label_5")
        self.textbox_password = QtWidgets.QLineEdit(self.group_second)
        self.textbox_password.setGeometry(QtCore.QRect(104, 68, 171, 20))
        self.textbox_password.setObjectName("textbox_password")
        self.btn_change_key = QtWidgets.QPushButton(self.group_second)
        self.btn_change_key.setGeometry(QtCore.QRect(74, 206, 171, 23))
        self.btn_change_key.setObjectName("btn_change_key")
        self.btn_change_data = QtWidgets.QPushButton(self.group_second)
        self.btn_change_data.setGeometry(QtCore.QRect(35, 123, 111, 23))
        self.btn_change_data.setObjectName("btn_change_data")
        self.textbox_add_inf = QtWidgets.QLineEdit(self.group_second)
        self.textbox_add_inf.setGeometry(QtCore.QRect(104, 93, 171, 20))
        self.textbox_add_inf.setObjectName("textbox_add_inf")
        self.label_6 = QtWidgets.QLabel(self.group_second)
        self.label_6.setGeometry(QtCore.QRect(10, 43, 91, 16))
        self.label_6.setObjectName("label_6")
        self.btn_buffer_pass = QtWidgets.QPushButton(self.group_second)
        self.btn_buffer_pass.setGeometry(QtCore.QRect(279, 66, 21, 23))
        self.btn_buffer_pass.setText("")
        self.btn_buffer_pass.setObjectName("btn_buffer_pass")
        self.btn_add_new_data = QtWidgets.QPushButton(self.group_second)
        self.btn_add_new_data.setGeometry(QtCore.QRect(172, 123, 111, 23))
        self.btn_add_new_data.setObjectName("btn_add_new_data")
        self.textbox_change_message = QtWidgets.QLineEdit(self.group_second)
        self.textbox_change_message.setGeometry(QtCore.QRect(74, 233, 171, 20))
        self.textbox_change_message.setObjectName("textbox_change_message")
        self.textbox_change_key = QtWidgets.QLineEdit(self.group_second)
        self.textbox_change_key.setGeometry(QtCore.QRect(74, 183, 171, 20))
        self.textbox_change_key.setObjectName("textbox_change_key")
        self.btn_buffer_email = QtWidgets.QPushButton(self.group_second)
        self.btn_buffer_email.setGeometry(QtCore.QRect(279, 41, 21, 23))
        self.btn_buffer_email.setText("")
        self.btn_buffer_email.setObjectName("btn_buffer_email")
        self.btn_buff_add_inf = QtWidgets.QPushButton(self.group_second)
        self.btn_buff_add_inf.setGeometry(QtCore.QRect(279, 91, 21, 23))
        self.btn_buff_add_inf.setText("")
        self.btn_buff_add_inf.setObjectName("btn_buff_add_inf")
        self.label_2 = QtWidgets.QLabel(self.group_second)
        self.label_2.setGeometry(QtCore.QRect(10, 18, 91, 16))
        self.label_2.setObjectName("label_2")
        self.btn_delete_data = QtWidgets.QPushButton(self.group_second)
        self.btn_delete_data.setGeometry(QtCore.QRect(35, 150, 111, 23))
        self.btn_delete_data.setObjectName("btn_delete_data")
        self.textbox_email = QtWidgets.QLineEdit(self.group_second)
        self.textbox_email.setGeometry(QtCore.QRect(104, 43, 171, 20))
        self.textbox_email.setObjectName("textbox_email")
        self.btn_exit = QtWidgets.QPushButton(self.group_second)
        self.btn_exit.setGeometry(QtCore.QRect(284, 128, 25, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_export_data = QtWidgets.QPushButton(self.group_second)
        self.btn_export_data.setGeometry(QtCore.QRect(9, 128, 25, 41))
        self.btn_export_data.setObjectName("btn_export_data")
        self.label_4 = QtWidgets.QLabel(self.group_second)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 16))
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
        self.label.setGeometry(QtCore.QRect(80, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Реестр Vol. 1", None, -1))
        self.btn_open_settings.setText(QtWidgets.QApplication.translate("MainWindow", "▼", None, -1))
        self.btn_clear_textboxs.setText(QtWidgets.QApplication.translate("MainWindow", "Очистить поля", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Доп. инфор:", None, -1))
        self.btn_change_key.setText(QtWidgets.QApplication.translate("MainWindow", "Сменить ключ", None, -1))
        self.btn_change_data.setText(QtWidgets.QApplication.translate("MainWindow", "Изменить", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "E-mail/login:", None, -1))
        self.btn_add_new_data.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Тип аккаунта:", None, -1))
        self.btn_delete_data.setText(QtWidgets.QApplication.translate("MainWindow", "Удалить запись", None, -1))
        self.btn_exit.setText(QtWidgets.QApplication.translate("MainWindow", "Х", None, -1))
        self.btn_export_data.setText(QtWidgets.QApplication.translate("MainWindow", "ЭК", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.btn_change_message.setText(QtWidgets.QApplication.translate("MainWindow", "Сменить подсказку", None, -1))
        self.btn_send_answ.setText(QtWidgets.QApplication.translate("MainWindow", "Отправить ответ", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Ответьте на вопрос?", None, -1))

