# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criarsala.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import socket
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CriarSala(object):
    def __init__(self,conexao):
        self.conexao = conexao
    def setupUi(self, CriarSala):
        self.sala = CriarSala
        CriarSala.setObjectName("CriarSala")
        CriarSala.resize(405, 293)
        CriarSala.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton = QtWidgets.QPushButton(CriarSala)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 151, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.enviaDadoServidor)
        self.label = QtWidgets.QLabel(CriarSala)
        self.label.setGeometry(QtCore.QRect(30, 90, 101, 41))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(CriarSala)
        self.textEdit.setGeometry(QtCore.QRect(130, 90, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(CriarSala)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CriarSala)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(CriarSala)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 150, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(CriarSala)
        QtCore.QMetaObject.connectSlotsByName(CriarSala)

    def retranslateUi(self, CriarSala):
        _translate = QtCore.QCoreApplication.translate
        CriarSala.setWindowTitle(_translate("CriarSala", "Form"))
        self.pushButton.setText(_translate("CriarSala", "CRIAR"))
        self.label.setText(_translate("CriarSala", "NOME DA SALA"))
        self.label_2.setText(_translate("CriarSala", "CRIE A SUA SALA"))
        self.label_3.setText(_translate("CriarSala", "Jogadores Por Sala"))

    def enviaDadoServidor(self):
        nomeSala = self.textEdit.toPlainText()
        tamanho = self.textEdit_2.toPlainText()
        msg = nomeSala+","+tamanho
        print(nomeSala)
        self.conexao.sendall(bytes("NovaSala", 'UTF-8'))
        self.conexao.sendall(bytes(msg, 'UTF-8'))
        self.sala.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CriarSala = QtWidgets.QWidget()
    ui = Ui_CriarSala()
    ui.setupUi(CriarSala)
    CriarSala.show()
    sys.exit(app.exec_())
