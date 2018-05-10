import socket, threading,json,sys
salas = {"Sala 01": [],"Sala 02": [],"Sala 03": [],"Sala 04": [],"Sala 05": []}
nicks = {}
class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)


    def createroom(self,ip):
        tamanho = len(self.salas.keys())
        salas[tamanho+1] = []
        salas[tamanho+1].append(ip)

    def showrooms(self):
        return salas


    def run(self):
        print("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(8)
            if(data.decode() == "Salas"):
                print(data)
                print(self.showrooms())
                data_string = json.dumps(self.showrooms())
                self.csocket.send(bytes(data_string,'UTF-8'))
            elif(data.decode() == "NovaSala"):
                print(data)
                data = self.csocket.recv(16)
                print(data)
                self.csocket.send(bytes(msg, 'UTF-8'))
                salas["Teste"] = []
                salas[str(data.decode())] = []
                print(salas)
            elif(data.decode() == "Nick"):
                print(data)
                data = self.csocket.recv(16)
                nicks[clientAddress[0]] = data.decode()
                print(nicks)
            elif(data.decode() == "Espera"):
                print(data.decode())
                data = self.csocket.recv(16)
                print(data.decode())
                for a,b in self.showrooms().items():
                    if(a == data.decode()):
                        print(a)
                        pers = []
                        for s in salas[a]: # salas[a] = array
                            pers.append(s)
                        print(pers)
                        data_str = json.dumps(pers)
                        self.csocket.send(bytes(data_str, 'UTF-8'))
            elif(data.decode() == "Escolha"):
                print(data.decode())
                data = self.csocket.recv(16)
                print(data)
                for a,b in self.showrooms().items():
                    if(a == data.decode()):
                        salas[a].append(nicks[clientAddress[0]])
                        print(salas)


    def next_power_of_2(self,x):
        return 1 if x == 0 else 2 ** (x - 1).bit_length()


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
