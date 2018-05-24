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

import socket, threading,json,sys,random,os,time # Importações necessárias para o código
salas = {"Sala 01": [],"Sala 02": [],"Sala 03": [],"Sala 04": [],"Sala 05": []} #Hash contendo todas as salas primárias disponíveis,
#elas contém um vetor no qual armazenará as pessoas que entrarão nas mesmas
nicks = {} #Hash que conterá os nicks das pessoas, a key é o endereço ip da máquina e o item é o item da pessoa
alfabeto = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
                 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
#Hash contendo as letras do alfabeto no qual será sorteado
vogais = {1:"A",2:"E",3:"I",4:"O",5:"U"} #Hash contendo as vogais do alfabeto no qual será sorteado
rodadas = {} #Hash que armazenará as letras sorteadas por cada rodada
tamanhoSala = {"Sala 01": 5 ,"Sala 02": 5,"Sala 03": 5,"Sala 04": 5,"Sala 05": 5}
#Hash que contém o tamanho de cada sala, por padrão é 5
groupSala = {"Sala 01": '225.4.5.6' ,"Sala 02": '225.4.5.7',"Sala 03": '225.4.5.8',"Sala 04": '225.4.5.9',"Sala 05": '225.4.5.10'}
#Hash que contém o multicastGroup de cada sala
help = 11 #Numero que acrescentará 1 ao numero do multicastGroup de cada sala. Válido para salas criadas pelos usuários

#Métodos
def sortear(): #Método que irá sortear as letras
    for i in range(1, 4): #For do Python, que vai de 1 até 3 -> 3 rodadas
        sorteados = []  #Criação de um vetor que armazernará as letras armazenadas
        for k in range(0,1): #For que irá sortear as vogais
            nm = random.randint(1,int(len(vogais))) #Função random que irá sortear um numero
            sorteados.append(vogais[nm]) #Armazena no vetor que armazena as letras a vogal sorteada
        for l in range(0, 15): #For que irá sortear todas as letras
            num_rolled = random.randint(1, int(len(alfabeto))) #Função random que irá sortear um número
            sorteados.append(alfabeto[num_rolled]) #Armazena no vetor que armazena as letras, a letra sorteada
        rodadas[int(i)]=sorteados #Armazena na hash todas as letras sorteadas em todas as rodadas


class ClientThread(threading.Thread): #Classe do servidor
    def __init__(self, clientAddress, clientsocket): #Construtor
        threading.Thread.__init__(self) #Criação de um novo thread
        self.csocket = clientsocket
        print("New connection added: ", clientAddress) #Mostra a nova conexão
        sortear() #Sorteia todas as palavras

    def createroom(self,ip): #Método que irá criar uma nova sala
        tamanho = len(self.salas.keys()) #Pega o tamanho da hash
        salas[tamanho+1] = [] #Crio um vetor
        salas[tamanho+1].append(ip) #Adiciona uma nova sala

    def showrooms(self):  #Método que mostra todoas as salas cadastradas
        return salas #Retorna as salas


    def run(self): #Método que irá rodar. Sobrescreve o método run da classe threading.Thread
        print("Connection from : ", clientAddress) #Mostro que existe uma conexão
        msg = ''
        while True: #Laço infinito
            data = self.csocket.recv(8) #Recebe um dado do cliente.
            if(data.decode() == "Salas"): #Se o que foi recebido for Salas
                print(data.decode())
                data_string = json.dumps(self.showrooms()) #Serializo o objeto
                self.csocket.send(bytes(data_string,'UTF-8')) #Envia para o cliente
            elif(data.decode() == "NovaSala"): #Se o que foi recebido for NovaSala
                print(data.decode())
                data = self.csocket.recv(16) #Recebe um novo dado
                k = data.decode().split(",") #Separo a string recebida, pois é recebido o nome da sala e o seu tamanho máximo
                self.csocket.send(bytes(msg, 'UTF-8'))  #Mando uma mensagem para o servidor
                salas[str(k[0])] = [] #Cria uma nova sala
                tamanhoSala[str(k[0])] = int(k[1]) #Adiciona o tamanho máximo da sala
                global help #Especifico que a variável help é global, para poder modificá-la
                groupSala[str(k[0])] = '225.4.5.'+str(help) #Adiciono o multicastGroup da sala
                help+=1 #Acrescento+1 em help
                #Adiciono mais 1
            elif(data.decode() == "Nick"): #Se o que foi recebido for Nick
                print(data.decode())
                data = self.csocket.recv(16) #Recebe um novo dado
                nicks[clientAddress[0]] = data.decode() #Adiciono o nick do usuário na hash de nicks
            elif(data.decode() == "Espera"): #Se o que foi recebido for Espera
                print(data.decode())
                data = self.csocket.recv(16) #Recebe um novo dado
                for a,b in self.showrooms().items():#Percorro a hash de salas que contém um vetor com todas as pessoas
                    if(a == data.decode()):  #Caso o nick armazenado na sala seja o mesmo que deseja a solicitação
                        pers = [] #Crio um vetor auxiliar
                        for s in salas[a]: # Percorre o vetor de salas
                            pers.append(s) #Adiciono as pessoas conectadas na sala no vetor pers
                        data_str = json.dumps(pers) #Serializo o vetor pers
                        self.csocket.send(bytes(data_str, 'UTF-8')) #Envia para o cliente

            elif(data.decode() == "Escolha"): #Se o que foi recebido for Escolha
                print(data.decode())
                data = self.csocket.recv(16) #Recebe um novo dado
                for a,b in self.showrooms().items(): #Percorre todas as salas
                    if(len(salas[a]) < tamanhoSala[a]): #Caso o tamanho atual da sala seja menor que o tamanho máximo suportado
                        if(a == data.decode()): #Se a sala que o usuário escolheu está disponível
                            salas[a].append(nicks[clientAddress[0]]) #Adiciona o usuário na sala que foi escolhida
                            self.csocket.send(bytes("yes", 'UTF-8')) #Envia 'yes' para o usuário, significando que ocorreu tudo bem
                            self.csocket.send(bytes(groupSala[a], 'UTF-8')) #Envia o multicastGroup daquela sala para o usuário
                    else: #Caso contrário
                        self.csocket.send(bytes("no", 'UTF-8')) #Envia um 'no' para o usuário, significando que não ocorreu tudo bem
            elif(data.decode() == "Sorteio"): #Se o que foi recebido for Sorteio
                print(data.decode())
                data_string = json.dumps(rodadas) #Serializa o vetor rodadas
                self.csocket.send(bytes(data_string, 'UTF-8')) #Envia para o usuário
            elif(data.decode() == "Begin"): #Se o que foi recebido for Begin
                print(data.decode())
                self.csocket.close() #Finaliza a conexão com o cliente
                break;

def readJson(): #Função que lê  Json contendo os dados do servidor - endereço ip e porta
    filename = os.path.join(os.getcwd(), "../../serverdata.json") #Verifica o caminho do arquivo
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    return data #Retorna os dados
data = readJson() #Os dados são inseridos em uma hash chamada data
LOCALHOST = data["IP"] #Define a constante do ip
PORT = data["PORT"] #Define a constante da porta
#Criação do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Servidor iniciado")
print("Esperando uma conexão com o cliente...")
while True: #Loop
    server.listen(1) #Lê de um cliente
    clientsock, clientAddress = server.accept() #Aceita a conexão
    newthread = ClientThread(clientAddress, clientsock) #Cria um novo thread
    newthread.start() #Começa a thread
