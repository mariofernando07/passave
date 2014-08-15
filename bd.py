import sqlite3
from config import nombreBD

class Conexion:
	def open(self):
		self.conn = sqlite3.connect(nombreBD)
		self.c = self.conn.cursor()
	
	def queryInsert(self, tupla):
		self.c.execute('insert into aplicacion values(?, ?, ?)', tupla)
		self.conn.commit()

	def querySelect(self):
		self.c.execute('select * from aplicacion')
		r = self.c.fetchall()
		for row in r:
			print row

	def close(self):
		self.conn = self.conn.close()


#Clase que se encarga de las tareas de la base de datos, usando el modulo QtSql

from PyQt4 import QtSql

class ConexionBD:
	def openCon(self):
		self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName(nombreBD)
		if(self.db.open()):
			return True
		else:
			print self.db.lastError().text()
			return False

	def querySelect(self):
		model = QtSql.QSqlTableModel(None, self.db)
		model.setTable('aplicacion')
		model.select()
		return model


	def closeCon(self):
		self.db.close()
		self.db.removeDatabase(nombreBD)