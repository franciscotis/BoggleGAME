from PyQt5 import QtCore, QtGui, QtWidgets
import json,os
from initscreen import Ui_TelaIniti

def readJson():
    print(os.path.abspath("serverdata.json"))
    filename = os.path.join(os.getcwd(), "serverdata.json")
    with open(filename, "r") as read_file:
        data = json.load(read_file)
    return data

if __name__ == "__main__":
    data  = readJson()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaIniti(data["IP"],data["PORT"])
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


