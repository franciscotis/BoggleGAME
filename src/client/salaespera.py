# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salaespera.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SalaEspera(object):
    def setupUi(self, Form):
        self.this = Form
        Form.setObjectName("Form")
        Form.resize(623, 467)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483, y1:0.352273, x2:0.603, y2:0.943, stop:0 rgba(244, 222, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.listaEspera = QtWidgets.QListWidget(Form)
        self.listaEspera.setGeometry(QtCore.QRect(150, 200, 331, 251))
        self.listaEspera.setObjectName("listaEspera")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(90, 0, 20, 471))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(520, 0, 20, 471))
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.nomeespera = QtWidgets.QLabel(Form)
        self.nomeespera.setGeometry(QtCore.QRect(260, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(50)
        self.nomeespera.setFont(font)
        self.nomeespera.setObjectName("nomeespera")
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setGeometry(QtCore.QRect(180, 30, 261, 131))
        self.icon.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
        self.icon.setText("")
        self.icon.setObjectName("icon")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nomeespera.setText(_translate("Form", "SALA DE ESPERA"))

import resource_rc
