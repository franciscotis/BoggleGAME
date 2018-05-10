import socket,threading,json
from PyQt5 import QtCore, QtGui, QtWidgets
from salas import Ui_SalasDisponiveis
class Rooms:
    def __init__(self,conexao):
        self.conexao = conexao

    def getSalas(self):
        self.ui.listWidget.clear()
        self.conexao.sendall(bytes("Salas", 'UTF-8'))
        dado = self.conexao.recv(1024)
        self.salas = json.loads(dado)
        for a,value in self.salas.items():
                self.ui.listWidget.addItem(a)

    def interface(self,Form):
        self.ui = Ui_SalasDisponiveis()
        self.ui.setupUi(Form)
        self.getSalas()
        self.ui.refresh.clicked.connect(self.getSalas)
