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
from PyQt5 import QtCore, QtGui, QtWidgets
import json,os
from initscreen import Ui_TelaIniti

def readJson(): #Função que lê  Json contendo os dados do servidor - endereço ip e porta
    print(os.path.abspath("serverdata.json"))
    filename = os.path.join(os.getcwd(), "serverdata.json")
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    return data #Retorna os dados

if __name__ == "__main__": #Começa a aplicação
    data  = readJson() #Lê o Json
    import sys #Importa o #sys
    #Chama a tela
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaIniti(data["IP"],data["PORT"])
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


