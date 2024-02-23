import sys
import os
from heart import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.lsfacts)
     self.ui.pushButton_2.clicked.connect(self.crcsv)
     self.ui.pushButton_3.clicked.connect(self.pdtls)
     self.ui.pushButton_5.clicked.connect(self.weights)
     self.ui.pushButton_6.clicked.connect(self.pred)
     self.ui.pushButton_7.clicked.connect(self.pnbeat)
     self.ui.pushButton_8.clicked.connect(self.ptbeat)
     self.ui.pushButton_9.clicked.connect(self.nhplot)
     self.ui.pushButton_10.clicked.connect(self.thplot)
     self.ui.pushButton_11.clicked.connect(self.mlpc)
     self.ui.pushButton_12.clicked.connect(self.qda)

  def lsfacts(self):
    os.system("python lsfacts1.py")       

  def crcsv(self):
    os.system("python createcsv1.py")

  def pdtls(self):
    os.system("python patient1.py")

  def weights(self):
    os.system("python nn1.py")

  def pred(self):
    os.system("python nn2.py")
	
  def pnbeat(self):
    os.system("python play_normal.py")

  def ptbeat(self):
    os.system("python play_trouble.py")

  def nhplot(self):
    os.system("python hplot1.py")

  def thplot(self):
    os.system("python hplot2.py")
	
  def mlpc(self):
    os.system("python mlpc1.py")

  def qda(self):
    os.system("python qda1.py")
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
