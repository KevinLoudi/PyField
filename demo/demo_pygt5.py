# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:38:56 2018

@author: kevin
@propose: demo the use of pygt package
"""
####date time
#from PyQt5.QtCore import QDate, QTime, QDateTime, Qt #no-GUI
#
#now = QDate.currentDate()
#
#print(now.toString(Qt.ISODate)) #time in format
#print(now.toString(Qt.DefaultLocaleLongDate)) #local time
#
#dateTime = QDateTime.currentDateTime()
#print(dateTime.toString())
#
##can get global time
##number of days in a month
##days between two dates
#
#### small window  coded in a procedural style
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget
#
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv) #create a application object from a command line
#    #control the start up of scripts
#    
#    w = QWidget() #base class of all user interface objects
#    #A widget with no parent is called a window.
#    
#    w.resize(250, 150) #px
#    w.move(300, 300)
#    w.setWindowTitle('A Sample Window')
#    w.show()
#    
#    sys.exit(app.exec_()) # The event handling starts from this point
#    
#    
####simple window with a icon,  object oriented programming styles
#
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtGui import QIcon
#
#
#class Example(QWidget): #inherit
#    
#    def __init__(self): #constructor 
#        super().__init__() #
#        
#        self.initUI()
#        
#        
#    def initUI(self): #creation of windows
#        
#        self.setGeometry(300, 300, 300, 220) #set location and size
#        self.setWindowTitle('Icon')
#        self.setWindowIcon(QIcon('web.png')) #set a icon       
#    
#        self.show()
#        
#        
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())   
#    
#    
####tool tip
#import sys
#from PyQt5.QtWidgets import (QWidget, QToolTip, 
#    QPushButton, QApplication)
#from PyQt5.QtGui import QFont    
#
#
#class Example(QWidget):
#    
#    def __init__(self):
#        super().__init__()
#        
#        self.initUI()
#        
#        
#    def initUI(self):
#        
#        QToolTip.setFont(QFont('SansSerif', 10))
#        
#        self.setToolTip('This is a <b>QWidget</b> widget') #tool tip
#        
#        btn = QPushButton('Button', self)
#        btn.setToolTip('This is a <b>QPushButton</b> widget')
#        btn.resize(btn.sizeHint())
#        btn.move(50, 50)       
#        
#        self.setGeometry(300, 300, 300, 200)
#        self.setWindowTitle('Tooltips')    
#        self.show()
#        
#        
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())