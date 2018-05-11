from salaespera import Ui_SalaEspera
import json,threading
from PyQt5 import  QtCore
class Waitlist:
    def __init__(self,conexao):
        self.salas = []
        self.count = len(self.salas)
        self.conexao = conexao
    def addToWaitList(self):
        self.ui.listaEspera.clear()
        self.conexao.sendall(bytes("Espera", 'UTF-8'))
        self.conexao.sendall(bytes(self.tipo, 'UTF-8'))
        dado = self.conexao.recv(1024)
        self.salas = json.loads(dado)
        if(self.count==5):
            self.count+=1
            self.beginGame()
        print(self.salas)
        for a in self.salas:
            self.ui.listaEspera.addItem(a)

    def interface(self,Form,tipo):
        self.tipo = tipo
        self.ui = Ui_SalaEspera()
        self.ui.setupUi(Form)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.addToWaitList)
        self.timer.start(1000)

    def beginGame(self):
        print("a ser implementado -- abre nova janela de jogo + leitura arquivo dic + insersção no dicionario +"
              "será capturado os dados já misturados pelo servidor e enviado por parâmetro // ideia topperson"
              "utilização da classe client na qual irá ter a conexão p2p-multicast e que vai chamar a "
              "classe demo.py || Basicamente eh isso, vai dar tudo certo, vida que segue, vida que passa.")
