# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 474)
        self.listaPalavrasEncontradas = QtWidgets.QListWidget(Form)
        self.listaPalavrasEncontradas.setGeometry(QtCore.QRect(120, 100, 278, 302))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listaPalavrasEncontradas.sizePolicy().hasHeightForWidth())
        self.listaPalavrasEncontradas.setSizePolicy(sizePolicy)
        self.listaPalavrasEncontradas.setMinimumSize(QtCore.QSize(0, 260))
        self.listaPalavrasEncontradas.setObjectName("listaPalavrasEncontradas")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listaPalavrasEncontradas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(3, 195, 32))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listaPalavrasEncontradas.addItem(item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listaPalavrasEncontradas.isSortingEnabled()
        self.listaPalavrasEncontradas.setSortingEnabled(False)
        item = self.listaPalavrasEncontradas.item(0)
        item.setText(_translate("Form", "teste"))
        item = self.listaPalavrasEncontradas.item(1)
        item.setText(_translate("Form", "aa"))
        self.listaPalavrasEncontradas.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

