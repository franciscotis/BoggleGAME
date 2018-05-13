import socket,threading,json,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Form
import socket
import struct
from os.path import abspath, exists
import os, sys
import threading
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
class Client:

    def __init__(self):
      mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
      self.socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socks.bind(('', MCAST_PORT))
      self.socks.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

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


    def load_words(self):
        try:
            filename = os.path.join(os.getcwd(), "words_alpha.dic")
            with open(filename, "r") as english_dictionary:
                valid_words = english_dictionary.read()
                self.palavras = valid_words.split('\n')
        except Exception as e:
            return str(e)

    def raffle(self,round):
        self.ui.letra1.setText(self.ui.k("Form",self.rodadas[round][0]))
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

