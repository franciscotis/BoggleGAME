# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from criarsala import Ui_CriarSala
class Ui_Form(object):
    def setupUi(self, Form):
        self.cont = False
        Form.setObjectName("Form")
        Form.resize(591, 514)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 90, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(140, 200, 291, 221))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 440, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonAction)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SALAS DISPONÍVEIS"))
        self.pushButton.setText(_translate("Form", "CRIAR SALA"))

    def buttonAction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CriarSala()
        self.ui.setupUi(self.window)
        self.window.show()
        self.cont = True

    def teste(self):
        if (self.cont == True):
            self.cont = False
            return True
        else:
            return self.cont


