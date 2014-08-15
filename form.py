# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Aug 14 22:15:53 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(660, 480)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 10, 371, 79))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txtpas = QtGui.QLineEdit(self.formLayoutWidget)
        self.txtpas.setObjectName(_fromUtf8("txtpas"))
        self.gridLayout.addWidget(self.txtpas, 2, 1, 1, 1)
        self.txtapp = QtGui.QLineEdit(self.formLayoutWidget)
        self.txtapp.setObjectName(_fromUtf8("txtapp"))
        self.gridLayout.addWidget(self.txtapp, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtmail = QtGui.QLineEdit(self.formLayoutWidget)
        self.txtmail.setObjectName(_fromUtf8("txtmail"))
        self.gridLayout.addWidget(self.txtmail, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 641, 54))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 170, 641, 301))
        self.tableView.setObjectName(_fromUtf8("tableView"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Passave", None))
        self.label_2.setText(_translate("Dialog", "Contraseña:", None))
        self.label.setText(_translate("Dialog", "Aplicación:", None))
        self.label_3.setText(_translate("Dialog", "Correo:", None))
        self.pushButton.setText(_translate("Dialog", "Guardar", None))
        self.pushButton_2.setText(_translate("Dialog", "Listar Todo", None))

