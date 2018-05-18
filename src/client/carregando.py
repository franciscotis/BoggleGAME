# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carregando.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 383)
        font = QtGui.QFont()
        font.setPointSize(17)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 70, 381, 131))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(37)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 210, 271, 41))
        self.progressBar.setStyleSheet("gridline-color: rgb(85, 0, 0);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CARREGANDO..."))
        self.progressBar.setFormat(_translate("Form", "%p%"))

