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
#Importações necessárias
import json,time,socket,struct,os,threading
from PyQt5 import QtCore, QtGui, QtWidgets
from demo import Ui_Form
from pontuacao import Pontuacao
from ranking import Ranking
MCAST_PORT = 5007
class Client: #Classe onde contém o jogo

    def __init__(self,dadosconect): #Construtor
      self.conecc = dadosconect #DadosConect é o endereço do grupo multicast

      #Abaixo contém a declaração de self.sock, que é o cliente que estará no grupo multicast
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
      #Abaixo contém a declaração de self.socks, que é o servidor que estará no grupo multicast
      self.socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
      self.socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.socks.bind(('', MCAST_PORT))
      mreq = struct.pack("4sl", socket.inet_aton(self.conecc), socket.INADDR_ANY)
      self.socks.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        #Como o cliente também é servidor, está utilizando uma arquitetura p2p
      self.pontuacao = 0
      self.possibilities = {1:[],2:[],3:[],4:[],5:[],6:[]}
      self.encontrados = []
      self.verdadeiros = []
      self.rodada=1
      self.pontojog = []
      self.pontfinal = {}

    def interface(self,Form,nick,pessoas,rodadas): #Método que fará com que a interface gráfica funcione
        self.pessoas = pessoas
        th = threading.Thread(target=self.multiServer) #Novo thread para fazer o servidor rodar
        th.start()
        self.nick = nick
        self.rodadas = rodadas
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.botoes = self.ui.botoes
        self.load_words()
        for a in pessoas:
            self.ui.listaJogadores.addItem(a) #Adiciona as pessoas conectadas no jogo na lista de jogadores
        self.raffle(str(self.rodada)) #Emabaralha as letras de acordo com a rodada
        self.ui.texto = ""
        self.ui.inputjogador.setText(self.ui.texto)
        self.ui.btnenviar.clicked.connect(self.enviadados) #Caso o botão seja clicado, os dados são enviados
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkRounds)
        self.timer.start(1000)
        self.parsedmsg = {}


    def checkRounds(self): #Verifica se uma rodada acabou
        if self.ui.total == 120 and self.rodada <4: #Caso a tempo restante seja 0 e a rodada seja menor que 3
            self.pontojog.clear() #Limpa o vetor de pontuação dos jogadores
            self.ui.total = 180 #Digo que o total é 180
            time.sleep(2) #Espera um tempo
            self.multiClient(1) #Envia 2 vezes a mesma informação, que é as palavras certas encontradas pelo jogador
            #  como é  UDP - uma forma de garantir a entrega
            self.multiClient(1)
            time.sleep(2) #espera um tempo
            for keys in self.parsedmsg.keys():
                if self.nick != keys:
                    print("indo tirar pontos hehehe")
                    print(self.parsedmsg)
                    self.tirapontua(self.parsedmsg[keys]) #A partir das mensagens recebidas pelos outros jogadores,
                    # essa é a checagem feita para descontar os pontos se as palavras forem iguais
            time.sleep(3) #espera um tempo
            self.multiClient(2) #Envia 2 vezes a mesma informação, que é a pontuação atual do jogador
            time.sleep(2) #Espera um tempo
            self.rodada+=1 #Aumenta a rodada
            if(self.rodada<=3):
                self.raffle(str(self.rodada)) #Embaralha os dados
            time.sleep(3) #Espera um tempo
            self.multiClient(3) #Envia 2 vezes a mesma informação, que é a pontuação do jogador
            time.sleep(3) #Espera um tempo
            self.showScreen() #Mostra a tela
        if(self.rodada==4): #Caso tenha passado 3 rodadas
            time.sleep(2) #Espera um pouco
            self.finalizeScreen() #Abre a tela de fim de jogo
            time.sleep(2) #Espera um pouco

            #Método que faz a leitura do arquivo.dic e adiciona no array
    def load_words(self):
        try:
            filename = os.path.join(os.getcwd(),"words_alpha.dic")
            with open(filename, "r") as english_dictionary:
                valid_words = english_dictionary.read()
                self.palavras = valid_words.split('\n')
        except Exception as e:
            print(str(e))

    def multiClient(self,tipo): #Método com as ações do cliente multicast
        self.sock.sendto(str(tipo).encode(encoding='utf_8', errors='strict'), (self.conecc, MCAST_PORT)) #Envia o tipo para o servidor
        if(tipo == 1): #Se o tipo for 1
            self.parsedmsg[self.nick]= self.verdadeiros #Associa as palavras verdadeiras a um usuário e armazenando em um hash map
            data_string = json.dumps(self.parsedmsg) #Serializa o dicionário
            self.sock.sendto(data_string.encode(encoding='utf_8', errors='strict'), (self.conecc, MCAST_PORT)) #Envia para o servidor
        elif(tipo ==2): #Caso o tipo for 2
            msg = self.nick+" -> "+str(self.pontuacao)+" pontos" #Associa os pontos do jogador com o seu nick
            self.sock.sendto(msg.encode(encoding='utf_8', errors='strict'), (self.conecc, MCAST_PORT)) #Envia para o servidor
        elif tipo ==3: #Se o tipo for 3
            sg = str(self.nick)+","+str(self.pontuacao) #Envia o nick do jogador com a sua pontuação
            self.sock.sendto(sg.encode(encoding='utf_8', errors='strict'), (self.conecc, MCAST_PORT)) #Envia para o servidor

    def multiServer(self): #Método com as ações do servidor
        while True: #Loop infinito
            tipo = self.socks.recv(2).decode(encoding="utf-8", errors="strict") #Recebe o tipo do cliente
            if tipo=='1': #Se o tipo for 1
                rcv = self.socks.recv(10240).decode(encoding="utf-8", errors="strict")  #Recebe os dados
                rrv = json.loads(rcv) #Deserializa os dados
                for i in rrv: #Percorre o hashmap
                    self.parsedmsg[i]= rrv[i] #Adiciona todas as palavras encontradas nela na hash
            elif tipo=='2': #Caso o tipo for 2
                msg = self.socks.recv(10240).decode(encoding="utf-8", errors="strict") #Recebe o dado
                if not msg in self.pontojog: #Se a mensagem recebida não estiver no vetor de pontuação
                    self.pontojog.append(msg) #Coloca a mensagem no vetor
            elif tipo == '3': #Caso o tipo for 3
                a = self.socks.recv(10240).decode(encoding="utf-8", errors="strict") #Recebe o dado
                lista = a.split(',') #Fatia a string pela virgula e coloca em um vetor
                self.pontfinal[lista[0]] = int(lista[1]) #Adiciona a pontuação e o nick do jogador em uma hash

    def showScreen(self): #Método que mostra a tela de jogo
        self.Form = QtWidgets.QWidget()
        self.k = Pontuacao()
        self.k.setupUi(self.Form)
        self.k.listWidget.clear()
        for i in self.pontojog:
            self.k.listWidget.addItem(i)
        self.Form.show()

    def finalizeScreen(self): #Método que finaliza o jogo
        self.Formulario = QtWidgets.QWidget()
        self.m = Ranking()
        self.m.setupUi(self.Formulario)
        from operator import itemgetter
        l = sorted(self.pontfinal.items(),key=itemgetter(1))  #Ordena a hash com base na pontuação [ ordenação em ordem decrescente
        aa = []
        for a in range(0,len(l)):
            aa.append(str(l[a][0])+" com "+str(l[a][1])+" pontos") #Adiciona no vetor de pontuação
        m = []
        for count,l in enumerate(reversed(aa)):
            m.append(str(count+1)+"º lugar - > " + l) #Coloca o array ao contrário na lista de ganhadores
        for k in m:
            self.m.listWidget.addItem(k) #adiciona na lista
        self.Formulario.show() #Mostra a lista de ganhadores
        self.timer.stop()
        self.ui.this.hide() #Fecha a tela

    def enviadados(self): #Método que captura o que o jogador escreveu e adiciona nas palavras
        for k in self.botoes: #Quando enviar habilita todos os botões
            k.setEnabled(True)
        for m in range(1,len(self.ui.letras)):
            self.ui.letras[m] = True
        texto = self.ui.inputjogador.toPlainText() #Coleta os dados do jogador
        self.ui.inputjogador.clear() #Limpa a caia de texto
        self.ui.texto = ""
        if texto.lower() not in self.encontrados: #Se o jogador não tiver digitado aquela palavra
            if texto!= "": #Se ele não digitou nada vazio
                self.encontrados.append(texto.lower()) #Coloca o texto digitado na lista de palavras encontradas
                self.test(texto,str(self.rodada)) #Faz a verificação se o que ele digitou foi uma palavra válida

    def test(self,texto,round): #Método que verifica a validez de uma palavra
        lista = self.rodadas[round] #Captura todas as palavras sorteadas de uma determinada rodada
        letrassorteadas = dict((x,lista.count(x)) for x in set(lista)) #Método que verifica a frequência de uma determinada letra
        # no vetor "lista"
        letraescolhida = dict((x,list(texto.upper()).count(x)) for x in set(list(texto.upper())))
        #Método que verifica a frequência de uma determinada letra nas palavras que o usuário digitou
        palavraCerta = True
        for j in letraescolhida.keys(): #For
            if(j in letrassorteadas.keys()): # Se a letra que o usuário digitou foi uma letra sorteada
                if letraescolhida[j] > letrassorteadas[j] : #Caso a quantidade de letras que o usuário digitou seja maior que a quantidade disponível
                    palavraCerta = False # A palavra não está certa
                else: #Caso contrário
                    palavraCerta = True # A palavra está correta
            else: #Caso contrário
                palavraCerta = False # A palavra está falsa
                break
        if palavraCerta: #Se a palavra estiver certa
            if texto.lower() in self.palavras: #Se a palavra escolhida estiver no dicionário, é adicionado com a cor verde na lista de
                #palavras encontradas
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

            else: #Caso contrário, é adicionado com a cor vermelho e riscado no meio na lista de palavras encontradas
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

        else: #Caso contrário, é adicionado com a cor vermelho e riscado no meio na lista de palavras encontradas
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

#Método que faz aumenta a pontuação com o tamanho do texto
    def pontua(self,texto):
        if len(texto) == 3: #Se o tamanho do texto for igual a 3
            return 1 #Pontuação = 1
        elif len(texto) ==4: # Se o tamanho do texto for igual a 4
            return 4 #Pontuação = 4
        elif len(texto) >=5: #Se o tamanho do texto for maior ou igual a 5
            return 6 #Pontuação = 6
        else: #Caso contrário
            return 0 #Pontuação = 0

#Método que faz diminuir a pontuação de acordo com as palavras iguais encontradas pelos usuários
    def tirapontua(self,arrs):
        for i in arrs: #Percorre o vetor
            if i in self.verdadeiros: #Se a palavra for uma palavra já encontrada
                if(self.pontuacao > 0): #Se a pontuação do jogador for maior que 0
                    self.pontuacao -= self.pontua(i) #Diminui a pontuação de acordo com o tamanho da palavra
                    self.ui.pontosEdit.setText(self.ui.k("Form", str(self.pontuacao))) #Muda a sua pontuação disponível na tela

#Método que emabaralha as letras na tela de acordo com a rodada
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


