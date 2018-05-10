from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import socket,threading,json
from initscreen import Ui_TelaIniti
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaIniti("localhost",8080)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())