import sys
from PyQt4 import QtCore, QtGui
from SCFGenerator import Ui_Form

class MyForm(QtGui.QWidget,Ui_Form):
	"""docstring for MyForm"""
	def __init__(self):
		QtGui.QWidget.__init__(self)
		#self.ui = Ui_Form()
		self.setupUi(self)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
