import socket,threading,json,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Form
ui = ""
class Client:

    def __init__(self,ip,porta):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conexao.connect((ip,porta))
        self.conexoes = []
        # client.sendall(bytes(str(Ui_Form.letra1clicked), 'UTF-8'))

    def enviaDados(self,tipo):
        if tipo== "Salas":
            self.conexao.sendall(bytes(tipo,'UTF-8'))
            data = self.recebeDados()
            self.salas = json.loads(data)
            print(self.salas)

    def recebeDados(self):
        dado = self.conexao.recv(1024)
        return dado

        """
        while True:
            in_data = client.recv(1024)
            print("From Server :", in_data.decode())
            out_data = input()
            client.sendall(bytes(out_data, 'UTF-8'))
            if out_data == 'bye':
                break
        client.close()
    
        """

def interface(self):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    self.ui = Ui_Form()
    self.ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    t = threading.Thread(target=interface())
    t.start()
    #oi.listaJogadores.addItem("i")


SERVER = "localhost"
PORT = 8080
cliente = Client("localhost",PORT)
cliente.enviaDados("Salas")

