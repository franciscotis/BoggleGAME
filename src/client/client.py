import socket,threading,json,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Form
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

    def interface(self,Form,nick,pessoas,rodadas):
        self.pessoas = pessoas
        self.nick = nick
        self.rodadas = rodadas
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.load_words()
        for a in pessoas:
            self.ui.listaJogadores.addItem(a)
        self.raffle('1')
        self.ui.btnenviar.clicked.connect(self.enviadados)


    def load_words(self):
        try:
            filename = os.path.join(os.getcwd(),"words_alpha.dic")
            with open(filename, "r") as english_dictionary:
                valid_words = english_dictionary.read()
                self.palavras = valid_words.split('\n')
        except Exception as e:
            print( str(e))

    def enviadados(self):
        texto = self.ui.inputjogador.toPlainText()
        self.ui.inputjogador.clear()
        if texto not in self.encontrados:
            if texto!= "":
                self.encontrados.append(texto)
                self.test(texto,'1')

    def test(self,texto,round):
        lista = self.rodadas[round]
        print(lista)
        letrassorteadas = dict((x,lista.count(x)) for x in set(lista))
        print(letrassorteadas)
        letraescolhida = dict((x,list(texto.upper()).count(x)) for x in set(list(texto.upper())))
        print(letraescolhida)
        palavraCerta = True
        for j in letraescolhida.keys():
            if(j in letrassorteadas.values()):
                if letraescolhida[j] > letrassorteadas[j]:
                    palavraCerta = False
            else:
                palavraCerta = False
        if palavraCerta:
            print("ta")
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
                print(self.pontuacao)
                self.ui.pontosEdit.setText(self.ui.k("Form", str(self.pontuacao)))

            else:
                print(texto, " não ta")
                item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(11)
                font.setStrikeOut(True)
                item.setFont(font)
                item.setText(texto)
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                print("here?")
                self.ui.listaPalavrasEncontradas.addItem(item)

        else:
            print(texto," não ta")
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setStrikeOut(True)
            item.setFont(font)
            item.setText(texto)
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            print("here?")
            self.ui.listaPalavrasEncontradas.addItem(item)
        print("irá verificar se o texto está correto")

    def pontua(self,texto):
        if len(texto) == 3:
            return 1
        elif len(texto) ==4:
            return 4
        elif len(texto) >=5:
            return 6
        else:
            return 0

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

