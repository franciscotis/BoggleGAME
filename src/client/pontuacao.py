# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pontuacao.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Pontuacao(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(516, 347)
        Form.setStyleSheet("background-color: rgb(178, 201, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(130, 120, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 90, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 511, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(90, 100, 20, 251))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(410, 100, 20, 251))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 81, 121))
        self.label_2.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 150, 81, 121))
        self.label_3.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PONTUAÇÃO"))

import resource_rc
