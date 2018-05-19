from salaespera import Ui_SalaEspera
from PyQt5 import QtCore, QtGui, QtWidgets
import json,random
from PyQt5 import  QtCore
from client import Client
class Waitlist:
    def __init__(self,conexao):
        self.salas = []
        self.begin = False
        self.conexao = conexao
        self.client = Client()
    def addToWaitList(self):
        if not self.begin:
            self.ui.listaEspera.clear()
            self.conexao.sendall(bytes("Espera", 'UTF-8'))
            self.conexao.sendall(bytes(self.tipo, 'UTF-8'))
            dado = self.conexao.recv(1024)
            self.salas = json.loads(dado)
            self.count = len(self.salas)
            if self.count==2 and self.begin == False:
                self.begin = True
                self.beginGame()
            print(self.salas)
            for a in self.salas:
                self.ui.listaEspera.addItem(a)

    def interface(self,Form,tipo,nick):
        self.nick = nick
        self.tipo = tipo
        self.ui = Ui_SalaEspera()
        self.ui.setupUi(Form)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.addToWaitList)
        self.timer.start(1000)

    def beginGame(self):
        self.Form = QtWidgets.QWidget()
        self.rodadas = self.rollDice()
        self.client.interface(self.Form, self.nick,self.salas,self.rodadas)
        self.conexao.sendall(bytes("Begin", 'UTF-8'))
        self.conexao.close()
        self.Form.show()
        self.ui.this.hide()
    def rollDice(self):
        self.conexao.sendall(bytes("Sorteio", 'UTF-8'))
        dado = self.conexao.recv(1024)
        rodadas = json.loads(dado)
        print(rodadas)
        return rodadas