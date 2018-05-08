import socket,threading,json
from PyQt5 import QtCore, QtGui, QtWidgets
from salas import Ui_Form
from criarsala import Ui_CriarSala
class Rooms:
    def __init__(self,ip,porta):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conexao.connect((ip, porta))


    def getSalas(self):
        self.ui.listWidget.clear()
        self.conexao.sendall(bytes("Salas", 'UTF-8'))
        dado = self.conexao.recv(1024)
        self.salas = json.loads(dado)
        for a,value in self.salas.items():
            for b,value in value.items():
                self.ui.listWidget.addItem(b)

    def interface(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.getSalas()
        th = threading.Thread(target=self.teste())
        th.start()
        Form.show()
        sys.exit(app.exec_())

    def teste(self):
        while (self.ui.teste()):
            print(self.ui.teste())
            self.getSalas()


salas = Rooms("localhost",8080)
t = threading.Thread(target=salas.interface())
t.start()
print("hey")



