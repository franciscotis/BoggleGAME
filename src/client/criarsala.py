# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criarsala.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
class Ui_CriarSala(object):
    def setupUi(self, CriarSala):
        self.sala = CriarSala
        CriarSala.setObjectName("CriarSala")
        CriarSala.resize(405, 293)
        self.pushButton = QtWidgets.QPushButton(CriarSala)
        self.pushButton.setGeometry(QtCore.QRect(110, 170, 151, 81))
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
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CriarSala)
        QtCore.QMetaObject.connectSlotsByName(CriarSala)

    def retranslateUi(self, CriarSala):
        _translate = QtCore.QCoreApplication.translate
        CriarSala.setWindowTitle(_translate("CriarSala", "Form"))
        self.pushButton.setText(_translate("CriarSala", "CRIAR"))
        self.label.setText(_translate("CriarSala", "NOME DA SALA"))
        self.label_2.setText(_translate("CriarSala", "CRIE A SUA SALA"))

    def enviaDadoServidor(self):
        SERVER = "localhost"
        PORT = 8080
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conexao.connect((SERVER, PORT))
        nomeSala = self.textEdit.toPlainText()
        print(nomeSala)
        self.conexao.sendall(bytes("NovaSala", 'UTF-8'))
        self.conexao.sendall(bytes(nomeSala, 'UTF-8'))
        self.conexao.close()
        self.sala.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CriarSala = QtWidgets.QWidget()
    ui = Ui_CriarSala()
    ui.setupUi(CriarSala)
    CriarSala.show()
    sys.exit(app.exec_())
