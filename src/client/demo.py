# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaJogo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 686)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.603, y2:0.943182, stop:0 rgba(161, 186, 199, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(600, 75))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("image: url(:/newPrefix/img/BoggleIcon.png);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temporestante = QtWidgets.QProgressBar(Form)
        self.total = 180
        self.temporestante.setMaximum(180)
        self.temporestante.setProperty("value", self.total)
        self.temporestante.setObjectName("temporestante")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(1000)
        self.horizontalLayout.addWidget(self.temporestante)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.JogadoresSessao = QtWidgets.QLabel(Form)
        self.JogadoresSessao.setFrameShape(QtWidgets.QFrame.Box)
        self.JogadoresSessao.setObjectName("JogadoresSessao")
        self.verticalLayout_9.addWidget(self.JogadoresSessao)
        self.listaJogadores = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listaJogadores.sizePolicy().hasHeightForWidth())
        self.listaJogadores.setSizePolicy(sizePolicy)
        self.listaJogadores.setMinimumSize(QtCore.QSize(0, 0))
        self.listaJogadores.setObjectName("listaJogadores")
        self.verticalLayout_9.addWidget(self.listaJogadores)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.letra1 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra1.sizePolicy().hasHeightForWidth())
        self.letra1.setSizePolicy(sizePolicy)
        self.letra1.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra1.setFont(font)
        self.letra1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra1.setStyleSheet("")
        self.letra1.setAutoDefault(False)
        self.letra1.setDefault(False)
        self.letra1.setFlat(True)
        self.letra1.setObjectName("letra1")
        self.gridLayout.addWidget(self.letra1, 0, 0, 1, 1)
        self.letra7 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra7.sizePolicy().hasHeightForWidth())
        self.letra7.setSizePolicy(sizePolicy)
        self.letra7.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra7.setFont(font)
        self.letra7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra7.setAutoDefault(False)
        self.letra7.setDefault(False)
        self.letra7.setFlat(True)
        self.letra7.setObjectName("letra7")
        self.gridLayout.addWidget(self.letra7, 1, 2, 1, 1)
        self.letra8 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra8.sizePolicy().hasHeightForWidth())
        self.letra8.setSizePolicy(sizePolicy)
        self.letra8.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra8.setFont(font)
        self.letra8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra8.setAutoDefault(False)
        self.letra8.setDefault(False)
        self.letra8.setFlat(True)
        self.letra8.setObjectName("letra8")
        self.gridLayout.addWidget(self.letra8, 1, 3, 1, 1)
        self.letra9 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra9.sizePolicy().hasHeightForWidth())
        self.letra9.setSizePolicy(sizePolicy)
        self.letra9.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra9.setFont(font)
        self.letra9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra9.setAutoDefault(False)
        self.letra9.setDefault(False)
        self.letra9.setFlat(True)
        self.letra9.setObjectName("letra9")
        self.gridLayout.addWidget(self.letra9, 2, 0, 1, 1)
        self.letra11 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra11.sizePolicy().hasHeightForWidth())
        self.letra11.setSizePolicy(sizePolicy)
        self.letra11.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra11.setFont(font)
        self.letra11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra11.setAutoDefault(False)
        self.letra11.setDefault(False)
        self.letra11.setFlat(True)
        self.letra11.setObjectName("letra11")
        self.gridLayout.addWidget(self.letra11, 2, 2, 1, 1)
        self.letra12 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra12.sizePolicy().hasHeightForWidth())
        self.letra12.setSizePolicy(sizePolicy)
        self.letra12.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra12.setFont(font)
        self.letra12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra12.setAutoDefault(False)
        self.letra12.setDefault(False)
        self.letra12.setFlat(True)
        self.letra12.setObjectName("letra12")
        self.gridLayout.addWidget(self.letra12, 2, 3, 1, 1)
        self.letra13 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra13.sizePolicy().hasHeightForWidth())
        self.letra13.setSizePolicy(sizePolicy)
        self.letra13.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra13.setFont(font)
        self.letra13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra13.setAutoDefault(False)
        self.letra13.setDefault(False)
        self.letra13.setFlat(True)
        self.letra13.setObjectName("letra13")
        self.gridLayout.addWidget(self.letra13, 3, 0, 1, 1)
        self.letra14 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra14.sizePolicy().hasHeightForWidth())
        self.letra14.setSizePolicy(sizePolicy)
        self.letra14.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra14.setFont(font)
        self.letra14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra14.setAutoDefault(False)
        self.letra14.setDefault(False)
        self.letra14.setFlat(True)
        self.letra14.setObjectName("letra14")
        self.gridLayout.addWidget(self.letra14, 3, 1, 1, 1)
        self.letra15 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra15.sizePolicy().hasHeightForWidth())
        self.letra15.setSizePolicy(sizePolicy)
        self.letra15.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra15.setFont(font)
        self.letra15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra15.setAutoDefault(False)
        self.letra15.setDefault(False)
        self.letra15.setFlat(True)
        self.letra15.setObjectName("letra15")
        self.gridLayout.addWidget(self.letra15, 3, 2, 1, 1)
        self.letra2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra2.sizePolicy().hasHeightForWidth())
        self.letra2.setSizePolicy(sizePolicy)
        self.letra2.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra2.setFont(font)
        self.letra2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra2.setAutoDefault(False)
        self.letra2.setDefault(False)
        self.letra2.setFlat(True)
        self.letra2.setObjectName("letra2")
        self.gridLayout.addWidget(self.letra2, 0, 1, 1, 1)
        self.letra3 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra3.sizePolicy().hasHeightForWidth())
        self.letra3.setSizePolicy(sizePolicy)
        self.letra3.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra3.setFont(font)
        self.letra3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra3.setAutoDefault(False)
        self.letra3.setDefault(False)
        self.letra3.setFlat(True)
        self.letra3.setObjectName("letra3")
        self.gridLayout.addWidget(self.letra3, 0, 2, 1, 1)
        self.letra4 = QtWidgets.QPushButton(Form)
        self.letra4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra4.sizePolicy().hasHeightForWidth())
        self.letra4.setSizePolicy(sizePolicy)
        self.letra4.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra4.setFont(font)
        self.letra4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra4.setStyleSheet("")
        self.letra4.setAutoDefault(False)
        self.letra4.setDefault(False)
        self.letra4.setFlat(True)
        self.letra4.setObjectName("letra4")
        self.gridLayout.addWidget(self.letra4, 0, 3, 1, 1)
        self.letra5 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra5.sizePolicy().hasHeightForWidth())
        self.letra5.setSizePolicy(sizePolicy)
        self.letra5.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra5.setFont(font)
        self.letra5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra5.setAutoDefault(False)
        self.letra5.setDefault(False)
        self.letra5.setFlat(True)
        self.letra5.setObjectName("letra5")
        self.gridLayout.addWidget(self.letra5, 1, 0, 1, 1)
        self.letra6 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra6.sizePolicy().hasHeightForWidth())
        self.letra6.setSizePolicy(sizePolicy)
        self.letra6.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra6.setFont(font)
        self.letra6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra6.setAutoDefault(False)
        self.letra6.setDefault(False)
        self.letra6.setFlat(True)
        self.letra6.setObjectName("letra6")
        self.gridLayout.addWidget(self.letra6, 1, 1, 1, 1)
        self.letra10 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra10.sizePolicy().hasHeightForWidth())
        self.letra10.setSizePolicy(sizePolicy)
        self.letra10.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra10.setFont(font)
        self.letra10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra10.setAutoDefault(False)
        self.letra10.setDefault(False)
        self.letra10.setFlat(True)
        self.letra10.setObjectName("letra10")
        self.gridLayout.addWidget(self.letra10, 2, 1, 1, 1)
        self.letra16 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.letra16.sizePolicy().hasHeightForWidth())
        self.letra16.setSizePolicy(sizePolicy)
        self.letra16.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N EL")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.letra16.setFont(font)
        self.letra16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letra16.setAutoDefault(False)
        self.letra16.setDefault(False)
        self.letra16.setFlat(True)
        self.letra16.setObjectName("letra16")
        self.gridLayout.addWidget(self.letra16, 3, 3, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Pontuacao = QtWidgets.QLabel(Form)
        self.Pontuacao.setFrameShape(QtWidgets.QFrame.Box)
        self.Pontuacao.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Pontuacao.setScaledContents(False)
        self.Pontuacao.setWordWrap(False)
        self.Pontuacao.setIndent(51)
        self.Pontuacao.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Pontuacao.setObjectName("Pontuacao")
        self.verticalLayout_2.addWidget(self.Pontuacao)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.pontosEdit = QtWidgets.QLabel(Form)
        self.pontosEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.pontosEdit.setObjectName("pontosEdit")
        self.horizontalLayout_7.addWidget(self.pontosEdit)
        self.points = QtWidgets.QLabel(Form)
        self.points.setFrameShape(QtWidgets.QFrame.Box)
        self.points.setObjectName("points")
        self.horizontalLayout_7.addWidget(self.points)
        spacerItem4 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setIndent(64)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listaPalavrasEncontradas = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listaPalavrasEncontradas.sizePolicy().hasHeightForWidth())
        self.listaPalavrasEncontradas.setSizePolicy(sizePolicy)
        self.listaPalavrasEncontradas.setMinimumSize(QtCore.QSize(0, 260))
        self.listaPalavrasEncontradas.setObjectName("listaPalavrasEncontradas")
        self.verticalLayout_2.addWidget(self.listaPalavrasEncontradas)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.inputjogador = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputjogador.sizePolicy().hasHeightForWidth())
        self.inputjogador.setSizePolicy(sizePolicy)
        self.inputjogador.setMinimumSize(QtCore.QSize(200, 10))
        self.inputjogador.setSizeIncrement(QtCore.QSize(0, 0))
        self.inputjogador.setBaseSize(QtCore.QSize(0, 0))
        self.inputjogador.setAutoFillBackground(False)
        self.inputjogador.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputjogador.setObjectName("inputjogador")
        self.horizontalLayout_6.addWidget(self.inputjogador)
        self.btnenviar = QtWidgets.QPushButton(Form)
        self.btnenviar.setObjectName("btnenviar")
        self.horizontalLayout_6.addWidget(self.btnenviar)
        spacerItem6 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.regraPont = QtWidgets.QTextEdit(Form)
        self.regraPont.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.regraPont.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.regraPont.setFrameShape(QtWidgets.QFrame.Box)
        self.regraPont.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.regraPont.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.regraPont.setUndoRedoEnabled(False)
        self.regraPont.setReadOnly(True)
        self.regraPont.setObjectName("regraPont")
        self.verticalLayout.addWidget(self.regraPont)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.sair = QtWidgets.QPushButton(Form)
        self.sair.setObjectName("sair")
        self.horizontalLayout_4.addWidget(self.sair)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def progress(self):
        if self.total >= 0:
            self.total -= 1
            self.temporestante.setValue(self.total)
            self.temporestante.setFormat(self.k("Form", "%m segundos"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.k = _translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.temporestante.setFormat(_translate("Form", "%m segundos"))
        self.JogadoresSessao.setText(_translate("Form", "   Jogadores da Sessão"))
        self.letra1.setText(_translate("Form", "A"))
        self.letra7.setText(_translate("Form", "G"))
        self.letra8.setText(_translate("Form", "H"))
        self.letra9.setText(_translate("Form", "I"))
        self.letra11.setText(_translate("Form", "K"))
        self.letra12.setText(_translate("Form", "L"))
        self.letra13.setText(_translate("Form", "M"))
        self.letra14.setText(_translate("Form", "N"))
        self.letra15.setText(_translate("Form", "O"))
        self.letra2.setText(_translate("Form", "B"))
        self.letra3.setText(_translate("Form", "C"))
        self.letra4.setText(_translate("Form", "D"))
        self.letra5.setText(_translate("Form", "E"))
        self.letra6.setText(_translate("Form", "F"))
        self.letra10.setText(_translate("Form", "J"))
        self.letra16.setText(_translate("Form", "P"))
        self.Pontuacao.setText(_translate("Form", "                PONTUAÇÃO"))
        self.pontosEdit.setText(_translate("Form", "0"))
        self.points.setText(_translate("Form", "pontos"))
        self.label_3.setText(_translate("Form", " PALAVRAS ENCONTRADAS"))
        self.btnenviar.setText(_translate("Form", "ENVIAR"))
        self.regraPont.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">REGRAS DE PONTUAÇÃO</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; color:#ef2929;\">3 Letras - 1 Ponto</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; color:#3465a4;\">4 Letras - 4 Pontos</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; color:#8ae234;\">5 ou mais Letras - 6 Pontos</span></p></body></html>"))
        self.sair.setText(_translate("Form", "SAIR"))

import resource_rc
