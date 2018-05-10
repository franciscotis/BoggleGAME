from salaespera import Ui_SalaEspera
import json,threading
from PyQt5 import  QtCore
class Waitlist:
    def __init__(self,conexao):
        self.salas = []
        self.conexao = conexao
    def addToWaitList(self):
        for i in range(10):
            self.ui.listaEspera.clear()
            self.conexao.sendall(bytes("Espera", 'UTF-8'))
            self.conexao.sendall(bytes(self.tipo, 'UTF-8'))
            dado = self.conexao.recv(1024)
            self.salas = json.loads(dado)
            print(self.salas)
            for a in self.salas:
                self.ui.listaEspera.addItem(a)

    def interface(self,Form,tipo):
        self.tipo = tipo
        self.ui = Ui_SalaEspera()
        self.ui.setupUi(Form)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.addToWaitList)
        self.timer.start(5000)
        t = threading.Thread(self.addToWaitList())
        t.start()

