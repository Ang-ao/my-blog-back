# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1001, 761))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.home_page_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.home_page_btn.setObjectName("home_page_btn")
        self.horizontalLayout.addWidget(self.home_page_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.edit_page_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.edit_page_btn.setObjectName("edit_page_btn")
        self.horizontalLayout.addWidget(self.edit_page_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.new_page_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.new_page_btn.setObjectName("new_page_btn")
        self.horizontalLayout.addWidget(self.new_page_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.board_page_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.board_page_btn.setObjectName("board_page_btn")
        self.horizontalLayout.addWidget(self.board_page_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.main_stacked_widget = QtWidgets.QStackedWidget(self.layoutWidget)
        self.main_stacked_widget.setObjectName("main_stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.home_title_label = QtWidgets.QLabel(self.page)
        self.home_title_label.setGeometry(QtCore.QRect(430, 20, 81, 31))
        self.home_title_label.setObjectName("home_title_label")
        self.home_calendar = QtWidgets.QCalendarWidget(self.page)
        self.home_calendar.setGeometry(QtCore.QRect(50, 70, 901, 291))
        self.home_calendar.setObjectName("home_calendar")
        self.home_date_time_edit = QtWidgets.QDateTimeEdit(self.page)
        self.home_date_time_edit.setGeometry(QtCore.QRect(400, 440, 194, 22))
        self.home_date_time_edit.setObjectName("home_date_time_edit")
        self.main_stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.edit_text_edit = QtWidgets.QTextEdit(self.page_2)
        self.edit_text_edit.setGeometry(QtCore.QRect(230, 50, 761, 661))
        self.edit_text_edit.setObjectName("edit_text_edit")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(600, 10, 371, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_out_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.edit_out_btn.setObjectName("edit_out_btn")
        self.horizontalLayout_4.addWidget(self.edit_out_btn)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.edit_preview_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.edit_preview_btn.setObjectName("edit_preview_btn")
        self.horizontalLayout_4.addWidget(self.edit_preview_btn)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.edit_issue_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.edit_issue_btn.setObjectName("edit_issue_btn")
        self.horizontalLayout_4.addWidget(self.edit_issue_btn)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.edit_delete_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.edit_delete_btn.setObjectName("edit_delete_btn")
        self.horizontalLayout_4.addWidget(self.edit_delete_btn)
        self.layoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(230, 10, 351, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edit_title_label = QtWidgets.QLabel(self.layoutWidget_3)
        self.edit_title_label.setObjectName("edit_title_label")
        self.horizontalLayout_5.addWidget(self.edit_title_label)
        self.edit_title_line_edit = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.edit_title_line_edit.setObjectName("edit_title_line_edit")
        self.horizontalLayout_5.addWidget(self.edit_title_line_edit)
        self.edit_list_label = QtWidgets.QLabel(self.page_2)
        self.edit_list_label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.edit_list_label.setObjectName("edit_list_label")
        self.line = QtWidgets.QFrame(self.page_2)
        self.line.setGeometry(QtCore.QRect(210, -10, 20, 741))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.edit_list_widget = QtWidgets.QListWidget(self.page_2)
        self.edit_list_widget.setGeometry(QtCore.QRect(10, 50, 200, 661))
        self.edit_list_widget.setObjectName("edit_list_widget")
        self.main_stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_title_label = QtWidgets.QLabel(self.layoutWidget1)
        self.new_title_label.setObjectName("new_title_label")
        self.horizontalLayout_2.addWidget(self.new_title_label)
        self.new_title_line_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.new_title_line_edit.setObjectName("new_title_line_edit")
        self.horizontalLayout_2.addWidget(self.new_title_line_edit)
        self.new_text_edit = QtWidgets.QTextEdit(self.page_3)
        self.new_text_edit.setGeometry(QtCore.QRect(10, 50, 981, 661))
        self.new_text_edit.setObjectName("new_text_edit")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 10, 551, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.new_save_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_save_btn.setObjectName("new_save_btn")
        self.horizontalLayout_3.addWidget(self.new_save_btn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.new_open_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_open_btn.setObjectName("new_open_btn")
        self.horizontalLayout_3.addWidget(self.new_open_btn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.new_clear_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_clear_btn.setObjectName("new_clear_btn")
        self.horizontalLayout_3.addWidget(self.new_clear_btn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.new_preview_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_preview_btn.setObjectName("new_preview_btn")
        self.horizontalLayout_3.addWidget(self.new_preview_btn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.new_issue_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.new_issue_btn.setObjectName("new_issue_btn")
        self.horizontalLayout_3.addWidget(self.new_issue_btn)
        self.main_stacked_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.mesg_board_text_browser = QtWidgets.QTextBrowser(self.page_4)
        self.mesg_board_text_browser.setGeometry(QtCore.QRect(10, 70, 981, 641))
        self.mesg_board_text_browser.setObjectName("mesg_board_text_browser")
        self.mesg_board_label = QtWidgets.QLabel(self.page_4)
        self.mesg_board_label.setGeometry(QtCore.QRect(340, 10, 251, 41))
        self.mesg_board_label.setObjectName("mesg_board_label")
        self.mesg_board_btn = QtWidgets.QPushButton(self.page_4)
        self.mesg_board_btn.setGeometry(QtCore.QRect(860, 20, 81, 28))
        self.mesg_board_btn.setObjectName("mesg_board_btn")
        self.main_stacked_widget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.main_stacked_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_page_btn.setText(_translate("MainWindow", "Home"))
        self.edit_page_btn.setText(_translate("MainWindow", "edit article"))
        self.new_page_btn.setText(_translate("MainWindow", "new article"))
        self.board_page_btn.setText(_translate("MainWindow", "mesg board"))
        self.home_title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Home</span></p></body></html>"))
        self.edit_out_btn.setText(_translate("MainWindow", "Out"))
        self.edit_preview_btn.setText(_translate("MainWindow", "preview"))
        self.edit_issue_btn.setText(_translate("MainWindow", "issue"))
        self.edit_delete_btn.setText(_translate("MainWindow", "delete"))
        self.edit_title_label.setText(_translate("MainWindow", "*Title:"))
        self.edit_list_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Articles...</span></p></body></html>"))
        self.new_title_label.setText(_translate("MainWindow", "*Title:"))
        self.new_save_btn.setText(_translate("MainWindow", "Save"))
        self.new_open_btn.setText(_translate("MainWindow", "Open..."))
        self.new_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.new_preview_btn.setText(_translate("MainWindow", "Preview"))
        self.new_issue_btn.setText(_translate("MainWindow", "Issue"))
        self.mesg_board_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Message Board</span></p></body></html>"))
        self.mesg_board_btn.setText(_translate("MainWindow", "Refresh"))
