# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salas.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from criarsala import Ui_CriarSala
class Ui_SalasDisponiveis(object):
        def setupUi(self, SalasDisponiveis):
            SalasDisponiveis.setObjectName("SalasDisponiveis")
            SalasDisponiveis.resize(591, 514)
            SalasDisponiveis.setStyleSheet("background-color: rgb(93, 177, 255);")
            self.listWidget = QtWidgets.QListWidget(SalasDisponiveis)
            self.listWidget.setGeometry(QtCore.QRect(140, 200, 291, 221))
            self.listWidget.setObjectName("listWidget")
            self.btnCreate = QtWidgets.QPushButton(SalasDisponiveis)
            self.btnCreate.setGeometry(QtCore.QRect(150, 440, 131, 51))
            font = QtGui.QFont()
            font.setFamily("Sitka Text")
            self.btnCreate.setFont(font)
            self.btnCreate.setObjectName("btnCreate")
            self.btnBegin = QtWidgets.QPushButton(SalasDisponiveis)
            self.btnBegin.setGeometry(QtCore.QRect(310, 440, 131, 51))
            font = QtGui.QFont()
            font.setFamily("Sitka Text")
            self.btnBegin.setFont(font)
            self.btnBegin.setObjectName("btnBegin")
            self.imgboggle = QtWidgets.QLabel(SalasDisponiveis)
            self.imgboggle.setGeometry(QtCore.QRect(170, 10, 211, 91))
            self.imgboggle.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
            self.imgboggle.setText("")
            self.imgboggle.setObjectName("imgboggle")
            self.refresh = QtWidgets.QPushButton(SalasDisponiveis)
            self.refresh.setGeometry(QtCore.QRect(60, 110, 471, 81))
            font = QtGui.QFont()
            font.setFamily("Letter Gothic Std")
            font.setPointSize(35)
            self.refresh.setFont(font)
            self.refresh.setFlat(True)
            self.refresh.setObjectName("refresh")
            self.btnCreate.clicked.connect(self.buttonAction)
            self.retranslateUi(SalasDisponiveis)
            QtCore.QMetaObject.connectSlotsByName(SalasDisponiveis)

        def buttonAction(self):
            for a in self.listWidget.selectedItems():
                print (a.text())
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CriarSala()
            self.ui.setupUi(self.window)
            self.window.show()




        def retranslateUi(self, SalasDisponiveis):
            _translate = QtCore.QCoreApplication.translate
            SalasDisponiveis.setWindowTitle(_translate("SalasDisponiveis", "Form"))
            self.btnCreate.setText(_translate("SalasDisponiveis", "CRIAR SALA"))
            self.btnBegin.setText(_translate("SalasDisponiveis", "COMEÇAR"))
            self.refresh.setText(_translate("SalasDisponiveis", "SALAS DISPONÍVEIS"))

import resource_rc
