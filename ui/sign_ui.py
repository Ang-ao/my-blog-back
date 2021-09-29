# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signIn.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(70, 220, 93, 28))
        self.quit_btn.setObjectName("quit_btn")
        self.sign_btn = QtWidgets.QPushButton(Form)
        self.sign_btn.setGeometry(QtCore.QRect(230, 220, 93, 28))
        self.sign_btn.setObjectName("sign_btn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 141, 31))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 70, 251, 127))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pw_line = QtWidgets.QLineEdit(self.widget)
        self.pw_line.setObjectName("pw_line")
        self.gridLayout.addWidget(self.pw_line, 1, 1, 1, 1)
        self.name_line = QtWidgets.QLineEdit(self.widget)
        self.name_line.setObjectName("name_line")
        self.gridLayout.addWidget(self.name_line, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit_btn.setText(_translate("Form", "Quit"))
        self.sign_btn.setText(_translate("Form", "Sign in"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sign in</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "passWord:"))
        self.label.setText(_translate("Form", "name:"))
