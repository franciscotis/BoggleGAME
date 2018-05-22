import socket,threading,json,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Form
import time
from pontuacao import Pontuacao
from ranking import Ranking
from collections import OrderedDict
from itertools import product
import socket
import struct
from os.path import abspath, exists
import os, sys
from collections import Counter
import threading
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
from collections import Counter
class Client:

    def __init__(self):
        #sock - client | socks - server
      mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
      self.socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socks.bind(('', MCAST_PORT))
      self.socks.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
      self.pontuacao = 0
      self.possibilities = {1:[],2:[],3:[],4:[],5:[],6:[]}
      self.encontrados = []
      self.verdadeiros = []
      self.rodada=1
      self.available = False
      self.pontojog = []
      self.pontfinal = {}

    def interface(self,Form,nick,pessoas,rodadas):
        self.pessoas = pessoas
        th = threading.Thread(target=self.multiServer)
        th.start()
        self.nick = nick
        self.rodadas = rodadas
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.botoes = self.ui.botoes
        self.load_words()
        for a in pessoas:
            self.ui.listaJogadores.addItem(a)
        self.raffle(str(self.rodada))
        self.ui.texto = ""
        self.ui.inputjogador.setText(self.ui.texto)
        self.ui.btnenviar.clicked.connect(self.enviadados)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkRounds)
        self.timer.start(5000)
        self.parsedmsg = {}


    def checkRounds(self):
        if self.ui.total == 0 and self.rodada <3:
            self.ui.total = 180
            self.multiClient(1)
            time.sleep(3)
            for keys in self.parsedmsg.keys():
                if self.nick != keys:
                    self.tirapontua(self.parsedmsg[keys])
            self.multiClient(2)
            time.sleep(3)
            self.rodada+=1
            self.raffle(str(self.rodada))
            print("hi")
            self.multiClient(3)
            time.sleep(2)
            self.showScreen()
        if(self.rodada==3):
            time.sleep(2)
            self.finalizeScreen()
            time.sleep(2)
    def load_words(self):
        try:
            filename = os.path.join(os.getcwd(),"words_alpha.dic")
            with open(filename, "r") as english_dictionary:
                valid_words = english_dictionary.read()
                self.palavras = valid_words.split('\n')
        except Exception as e:
            print(str(e))

    def multiClient(self,tipo):
        self.sock.sendto(str(tipo).encode(encoding='utf_8', errors='strict'), (MCAST_GRP, MCAST_PORT))
        if(tipo == 1):
            self.parsedmsg[self.nick]= self.verdadeiros
            print("parsed msg")
            print(self.parsedmsg)
            print(type(self.parsedmsg))
            data_string = json.dumps(self.parsedmsg)
            self.sock.sendto(data_string.encode(encoding='utf_8', errors='strict'), (MCAST_GRP, MCAST_PORT))
        elif(tipo ==2):
            msg = self.nick+" -> "+str(self.pontuacao)+" pontos"
            self.sock.sendto(msg.encode(encoding='utf_8', errors='strict'), (MCAST_GRP, MCAST_PORT))
        elif tipo ==3:
            sg = str(self.nick)+","+str(self.pontuacao)
            print("printando sg")
            print(sg)
            self.sock.sendto(sg.encode(encoding='utf_8', errors='strict'), (MCAST_GRP, MCAST_PORT))

    def multiServer(self):
        while True:
            tipo = self.socks.recv(2).decode(encoding="utf-8", errors="strict")
            if tipo=='1':
                rcv = self.socks.recv(10240).decode(encoding="utf-8", errors="strict")
                rrv = json.loads(rcv)
                print(rrv)
                print("printando rrv")
                print(type(rrv))
                print("out")
                for i in rrv.keys():
                    print("printando rrv "+ str(rrv[i]))
                    self.parsedmsg[i] = []
                    self.parsedmsg[i].append(rrv[i])
            elif tipo=='2':
                self.pontojog.append(self.socks.recv(10240).decode(encoding="utf-8", errors="strict"))
            elif tipo == '3':
                a = self.socks.recv(10240).decode(encoding="utf-8", errors="strict")
                print("printando a")
                print(a)
                lista = a.split(',')
                print("printando lista")
                print(lista)
                self.pontfinal[lista[0]] = int(lista[1])

    def showScreen(self):
        self.Form = QtWidgets.QWidget()
        self.k = Pontuacao()
        self.k.setupUi(self.Form)
        self.k.listWidget.clear()
        for i in self.pontojog:
            self.k.listWidget.addItem(i)
        self.Form.show()

    def finalizeScreen(self):
        self.Formulario = QtWidgets.QWidget()
        self.m = Ranking()
        self.m.setupUi(self.Formulario)
        from operator import itemgetter
        l = sorted(self.pontfinal.items(),key=itemgetter(1))
        print("printando l em seguir")
        print(l)
        print(l[1][0])
        print(l[0][1])
        aa = []
        for a in range(0,len(l)):
            aa.append(str(l[a][0])+" com "+str(l[a][1])+" pontos")
        print("printando aa em seguir")
        print(aa)
        print("printei")
        print(type(aa))
        print(reversed(aa))
        m = []
        for count,l in enumerate(reversed(aa)):
            m.append(str(count+1)+"º lugar - > " + l)
        print(m)
        for k in m:
            self.m.listWidget.addItem(k)
        self.Formulario.show()
        self.timer.stop()
        self.ui.this.hide()

    def enviadados(self):
        for k in self.botoes:
            k.setEnabled(True)
        for m in range(1,len(self.ui.letras)):
            self.ui.letras[m] = True
        texto = self.ui.inputjogador.toPlainText()
        self.ui.inputjogador.clear()
        self.ui.texto = ""
        if texto.lower() not in self.encontrados:
            if texto!= "":
                self.encontrados.append(texto.lower())
                self.test(texto,str(self.rodada))

    def test(self,texto,round):
        lista = self.rodadas[round]
        letrassorteadas = dict((x,lista.count(x)) for x in set(lista))
        letraescolhida = dict((x,list(texto.upper()).count(x)) for x in set(list(texto.upper())))
        palavraCerta = True
        for j in letraescolhida.keys():
            if(j in letrassorteadas.keys()):
                if letraescolhida[j] > letrassorteadas[j]:
                    palavraCerta = False
                else:
                    palavraCerta = True
            else:
                palavraCerta = False
                break
        if palavraCerta:
            if texto.lower() in self.palavras:
                item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(11)
                item.setFont(font)
                item.setText(texto)
                brush = QtGui.QBrush(QtGui.QColor(3, 195, 32))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.ui.listaPalavrasEncontradas.addItem(item)
                self.pontuacao +=self.pontua(texto)
                self.ui.pontosEdit.setText(self.ui.k("Form", str(self.pontuacao)))
                self.verdadeiros.append(texto)

            else:
                item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStrikeOut(True)
                item.setFont(font)
                item.setText(texto)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.ui.listaPalavrasEncontradas.addItem(item)

        else:
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setStrikeOut(True)
            item.setFont(font)
            item.setText(texto)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            self.ui.listaPalavrasEncontradas.addItem(item)

    def pontua(self,texto):
        if len(texto) == 3:
            return 1
        elif len(texto) ==4:
            return 4
        elif len(texto) >=5:
            return 6
        else:
            return 0

    def tirapontua(self,arrs):
        print("ok")
        for i in arrs:
            print(i)
            if i in self.verdadeiros:
                print("tttttt")
                if(self.pontuacao > 0):
                    self.pontuacao -= self.pontua(i)
                    self.ui.pontosEdit.setText(self.ui.k("Form", str(self.pontuacao)))

    def raffle(self,round):
        self.ui.letra1.setText(self.ui.k("Form", self.rodadas[round][0]))
        self.ui.letra2.setText(self.ui.k("Form", self.rodadas[round][1]))
        self.ui.letra3.setText(self.ui.k("Form", self.rodadas[round][2]))
        self.ui.letra4.setText(self.ui.k("Form", self.rodadas[round][3]))
        self.ui.letra5.setText(self.ui.k("Form", self.rodadas[round][4]))
        self.ui.letra6.setText(self.ui.k("Form", self.rodadas[round][5]))
        self.ui.letra7.setText(self.ui.k("Form", self.rodadas[round][6]))
        self.ui.letra8.setText(self.ui.k("Form", self.rodadas[round][7]))
        self.ui.letra9.setText(self.ui.k("Form", self.rodadas[round][8]))
        self.ui.letra10.setText(self.ui.k("Form", self.rodadas[round][9]))
        self.ui.letra11.setText(self.ui.k("Form", self.rodadas[round][10]))
        self.ui.letra12.setText(self.ui.k("Form", self.rodadas[round][11]))
        self.ui.letra13.setText(self.ui.k("Form", self.rodadas[round][12]))
        self.ui.letra14.setText(self.ui.k("Form", self.rodadas[round][13]))
        self.ui.letra15.setText(self.ui.k("Form", self.rodadas[round][14]))
        self.ui.letra16.setText(self.ui.k("Form", self.rodadas[round][15]))


