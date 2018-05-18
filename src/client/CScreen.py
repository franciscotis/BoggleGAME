from carregando import Ui_Form
from itertools import product
import threading
from PyQt5 import QtCore
class Carr:
    def __init__(self,conexao):
        self.conexao = conexao
        self.possibilidades = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        self.fin = {1: False, 2: False, 3:False, 4:False, 5:False,6:False,7:False}
        self.car=0
        self.fim = 1
        self.finalized = False

    def interface(self,Form,letras):
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.letras = letras
        self.th= threading.Thread(target=self.carregadados)
        self.th.start()

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.verifica)
        self.timer.start(1000)



    def carregadados(self):
        try:
            for i in range(1,5):
                for j in range(1,8):
                    for comb in product(self.letras[str(i)], repeat=j):
                        a = ''.join(comb)
                        self.possibilidades[j].append(a)
                        self.fin[j] = True
                self.finalized = True
        except Exception as e:
            print(e)

    def verifica(self):
        print(self.finalized)
        if self.fin[self.fim]:
            self.car+=12.5
            self.ui.progressBar.setValue(self.car)
            self.fim+=1
        if self.finalized:
            print(self.possibilidades[1])
            self.timer.stop()



