import sys
from PySide import QtGui

class FilePicker:

	def __init__( self, name, window, layout ):
		self.window = window
		self.name = name

		self.button = QtGui.QPushButton( name )
		self.button.clicked.connect( self.clicked )

		layout.addWidget( self.button )

	def clicked( self ):
		self.file = QtGui.QFileDialog( self.window ).getOpenFileName( self.window , self.name, '~')

def execute():
	print "Hello"

app = QtGui.QApplication(sys.argv)
win = QtGui.QWidget()

## commands

layout = QtGui.QVBoxLayout()

moduleStore = FilePicker("Module store", win, layout )
inputFiles = FilePicker("Log files", win, layout )
outputFiles = FilePicker("Output folder", win, layout )

doneButton = QtGui.QPushButton( "Ready" )
doneButton.clicked.connect( execute )
layout.addWidget( doneButton )

## set up and start app
 
win.setWindowTitle("edX log")
win.setLayout( layout )
win.show() 

sys.exit(app.exec_())
