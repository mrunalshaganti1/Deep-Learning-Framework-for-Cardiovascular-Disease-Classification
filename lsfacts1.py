import sys
import os
from lsfacts import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('heart1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.factsadd)
     with con:
    
        cur = con.cursor()
        cur.execute('SELECT lsdesc FROM smoker ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM drinker ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_2.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM diabetic ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_3.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM Arrhythmiatic ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_4.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM exercise ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_5.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM stress ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_6.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM cholesterol ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_7.addItem(row[0]))
        cur.execute('SELECT lsdesc FROM sleeptime ;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox_8.addItem(row[0]))
   

  def factsadd(self):
    with con:
    
        cur = con.cursor()
        text1 = self.ui.comboBox.currentText()
        text2 = self.ui.comboBox_2.currentText()
        text3 = self.ui.comboBox_3.currentText()
        text4 = self.ui.comboBox_4.currentText()
        text5 = self.ui.comboBox_5.currentText()
        text6 = self.ui.comboBox_6.currentText()
        text7 = self.ui.comboBox_7.currentText()
        text8 = self.ui.comboBox_8.currentText()
        cur.execute('INSERT INTO lsfacts VALUES(?,?,?,?,?,?,?,?)',(text1,text2,text3,text4,text5,text6,text7,text8))
        print('Attributes Successfully Added to Database')
        con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



	
