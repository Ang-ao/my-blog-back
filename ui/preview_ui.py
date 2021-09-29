# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preview(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        Form.setMinimumSize(QtCore.QSize(800, 800))
        Form.setMaximumSize(QtCore.QSize(800, 800))
        self.preview_text_browser = QtWidgets.QTextBrowser(Form)
        self.preview_text_browser.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.preview_text_browser.setObjectName("preview_text_browser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
