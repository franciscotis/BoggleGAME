"""
Autor: Francisco Tito Silva Satos Pereira - 16111203
Componente Curricular: MI - Conectividade e Concorrência
Concluido em: 22/05/2018
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
#Importações necessárias
from PyQt5 import QtCore, QtGui, QtWidgets
from rooms import Rooms
import socket,sys,json,time


class Ui_TelaIniti(object): #Classe da tela inicial
    def __init__(self, ip, porta): #Construtor que recebe o ip e a porta
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criação de uma nova conexão com o servidor
        self.conexao.connect((ip, porta)) #Conecta com o servidor
        self.salas = Rooms(self.conexao) #Instanciada um objeto contendo as salas

        #setupUi é um método do PyQT5 utilizado para a construção da interface gráfica.
    def setupUi(self, TelaIniti):
        self.tela = TelaIniti
        TelaIniti.setObjectName("TelaIniti")
        TelaIniti.resize(561, 392)
        TelaIniti.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.telaimagem = QtWidgets.QLabel(TelaIniti)
        self.telaimagem.setGeometry(QtCore.QRect(20, 20, 531, 151))
        self.telaimagem.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
        self.telaimagem.setText("")
        self.telaimagem.setObjectName("telaimagem")
        self.textopess = QtWidgets.QTextEdit(TelaIniti)
        self.textopess.setGeometry(QtCore.QRect(150, 220, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textopess.setFont(font)
        self.textopess.setAutoFillBackground(True)
        self.textopess.setStyleSheet("background-color: rgb(149, 200, 95);")
        self.textopess.setObjectName("textopess")
        self.btnentrar = QtWidgets.QPushButton(TelaIniti)
        self.btnentrar.setGeometry(QtCore.QRect(230, 300, 75, 23))
        self.btnentrar.setObjectName("btnentrar")
        self.retranslateUi(TelaIniti)
        QtCore.QMetaObject.connectSlotsByName(TelaIniti)
        self.btnentrar.clicked.connect(self.buttonAction) #Caso o botão de entrar seja clicado, ele chama o método buttonAction

    def buttonAction(self): #Metodo que será chamado quando o botão for clicado
        self.conexao.sendall(bytes("Nick", 'UTF-8')) #Manda 'Nick' para o servidor
        self.conexao.sendall(bytes(self.textopess.toPlainText(), 'UTF-8')) #Envia para o servidor o texto que o usuário digitou
        time.sleep(2) #Espera um tempo
        #Funções abaixo servem para abrir uma nova tela
        self.Form = QtWidgets.QMainWindow()
        self.salas.interface(self.Form,self.textopess.toPlainText())
        self.Form.show() #Abre a nova tela
        self.tela.hide() #Esconde essa tela

    #Função do próprio pyQt5 que dá suporte à tradução
    def retranslateUi(self, TelaIniti):
        _translate = QtCore.QCoreApplication.translate
        TelaIniti.setWindowTitle(_translate("TelaIniti", "Form"))
        self.textopess.setHtml(_translate("TelaIniti", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnentrar.setText(_translate("TelaIniti", "ENTRE"))

import resource_rc
