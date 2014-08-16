
#!/usr/bin/python
import sys
from form import *
from bd import *

class Main(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.salvarDatos)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'), self.mostrarDatos)

    def salvarDatos(self):
        app = str(self.ui.txtapp.text())
        self.ui.txtapp.setText("")
        mail = str(self.ui.txtmail.text())
        self.ui.txtmail.setText("")
        pas = str(self.ui.txtpas.text())
        self.ui.txtpas.setText("")
        t = (app, mail, pas)
        conexion = Conexion()
        conexion.open()
        conexion.queryInsert(t)
        #conexion.querySelect()
        conexion = conexion.close()
        self.mostrarDatos()

    def mostrarDatos(self):
        con = ConexionBD()
        if con.openCon():
            model = con.querySelect()
            self.ui.tableView.setModel(model)
        con = con.closeCon()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
        

