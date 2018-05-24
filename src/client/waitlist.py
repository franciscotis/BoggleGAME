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
#importações necessárias
from salaespera import Ui_SalaEspera
from PyQt5 import QtCore, QtGui, QtWidgets
import json,random
from PyQt5 import  QtCore
from client import Client
class Waitlist:
    def __init__(self,conexao,dadosconec): #construtor
        self.salas = []
        self.begin = False
        self.conexao = conexao
        self.dadosconec = dadosconec
        self.client = Client(self.dadosconec)

    def addToWaitList(self): #método que adiciona usuários na lista de fila de espera
        if not self.begin: #se o jogo não começou
            self.ui.listaEspera.clear() #limpa a lista
            self.conexao.sendall(bytes("Espera", 'UTF-8')) #envia "Espera" para o servidor
            self.conexao.sendall(bytes(self.tipo, 'UTF-8')) #Envia o nome da sala para o servidor
            dado = self.conexao.recv(1024) #recebe dados do servidor
            self.salas = json.loads(dado.decode()) #Deserializa os dados
            self.count = len(self.salas) #o contador é o tamanho da sala
            if self.count==2 and self.begin == False: #Se for igual a 2 e não tiver começado
                self.begin = True #Indica que o jogo começou
                self.beginGame() #O jogo começa
            for a in self.salas:
                self.ui.listaEspera.addItem(a) #Adiciona um item na lista de espera

    def interface(self,Form,tipo,nick): #Método que faz a interface gráfica funcionar
        self.nick = nick
        self.tipo = tipo
        self.ui = Ui_SalaEspera()
        self.ui.setupUi(Form)
        #Abaixo contém as instruções para adicionar um item na lista a cada 1 segundo
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.addToWaitList)
        self.timer.start(1000)

    def beginGame(self): #Método que faz a tela de jogo ser mostrada na tela
        self.Form = QtWidgets.QWidget()
        self.rodadas = self.rollDice()
        self.client.interface(self.Form, self.nick,self.salas,self.rodadas)
        self.conexao.sendall(bytes("Begin", 'UTF-8'))
        self.conexao.close()
        self.Form.show()
        self.ui.this.hide()

    def rollDice(self): #Método que faz com que o servidor envie os dados sorteados
        self.conexao.sendall(bytes("Sorteio", 'UTF-8')) #Envia "Sorteio" para o servidor
        dado = self.conexao.recv(1024) #Recebe os dados
        rodadas = json.loads(dado) #Deserializa os dados
        return rodadas