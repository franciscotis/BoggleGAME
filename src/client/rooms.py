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
import json,time
from PyQt5 import QtCore, QtGui, QtWidgets
from salas import Ui_SalasDisponiveis
from waitlist import Waitlist

class Rooms: #Classe Rooms -> irá mostrar ao usuário as salas do jogo
    def __init__(self,conexao): #Construtor
        self.conexao = conexao

    def getSalas(self): #Método que mostra todas as salas do jogo
        self.ui.listWidget.clear() #Limpa a lista de salas disponíveis
        self.conexao.sendall(bytes("Salas", 'UTF-8')) #Manda 'Salas' para o servidor
        dado = self.conexao.recv(1024) #Recebe o dado do servidor
        self.salas = json.loads(dado.decode()) #Desserializa o dado recebido do servidor e coloca na variável self.salas
        for a,value in self.salas.items(): #Percorre a hash self.salas
                self.ui.listWidget.addItem(a) #Para cada item, adiciona na lista de salas disponíveis que será exibida na tela

    def interface(self,Form,nick): #Método que chama a interface gráfica disponível no arquivo salas
        self.nick = nick
        self.ui = Ui_SalasDisponiveis(self.conexao) #Instancia um objeto da classe Ui_SalasDisponiveis, presente no arquivo salas
        self.ui.setupUi(Form) #Chama o método setupUi do arquivo 'salas' no qual irá mostrar a tela
        self.getSalas() #Chama o método getSalas
        #Abaixo contem alguns metodos que fazem a lista ser atualizada a cada 5 segundos
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getSalas)
        self.timer.start(5000)
        self.ui.btnBegin.clicked.connect(self.waitlist)

    def waitlist(self): #Método que faz o usuário ser redirecionado para a sala de espera
        for self.a in self.ui.listWidget.selectedItems(): #Caso o usuário selecione um item
            self.timer.stop() #Para de atualizar a lista
            time.sleep(3) #Pausa de 3 segundos
            self.conexao.sendall(bytes("Escolha", 'UTF-8')) #Manda "Escolha" para o usuário
            self.conexao.sendall(bytes(self.a.text(),'UTF-8')) #Manda a sala escolhida para o usuário
        dado = self.conexao.recv(1024) #Recebe dados do servidor
        if(dado.decode() == "yes"): #Se o dado recebido for yes
            conexao = self.conexao.recv(1024) #Recebe um dado do servidor
            #Abaixo contém instruções para abrir uma nova tela
            self.Form = QtWidgets.QMainWindow()
            self.wait = Waitlist(self.conexao,conexao.decode())
            self.wait.interface(self.Form,self.a.text(),self.nick)
            self.Form.show()
            self.ui.this.hide()

