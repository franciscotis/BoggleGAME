import socket,threading,json
from PyQt5 import QtCore, QtGui, QtWidgets
from salas import Ui_SalasDisponiveis
from waitlist import Waitlist
class Rooms:
    def __init__(self,conexao):
        self.conexao = conexao

    def getSalas(self):
        self.ui.listWidget.clear()
        self.conexao.sendall(bytes("Salas", 'UTF-8'))
        dado = self.conexao.recv(1024)
        self.salas = json.loads(dado.decode())
        for a,value in self.salas.items():
                self.ui.listWidget.addItem(a)

    def interface(self,Form,nick):
        self.nick = nick
        self.ui = Ui_SalasDisponiveis(self.conexao)
        self.ui.setupUi(Form)
        self.getSalas()
        self.ui.refresh.clicked.connect(self.getSalas)
        self.ui.btnBegin.clicked.connect(self.waitlist)

    def waitlist(self):
        for self.a in self.ui.listWidget.selectedItems():
            self.conexao.sendall(bytes("Escolha", 'UTF-8'))
            self.conexao.sendall(bytes(self.a.text(),'UTF-8'))
        dado = self.conexao.recv(1024)
        print(dado.decode())
        if(dado.decode() == "yes"):
            conexao = self.conexao.recv(1024)
            self.Form = QtWidgets.QMainWindow()
            self.wait = Waitlist(self.conexao,conexao.decode())
            self.wait.interface(self.Form,self.a.text(),self.nick)
            self.Form.show()
            self.ui.this.hide()

