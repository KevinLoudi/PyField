# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:08:13 2018

@author: kevin
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QMessageBox,QDesktopWidget, QMainWindow,
    QAction, qApp, QMenu, QWidget, QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtGui import (QFont, QIcon)   
from PyQt5.QtCore import (QCoreApplication, Qt) 



class Example(QMainWindow): #(QWidget):
    
    def __init__(self):
        super().__init__() #super() return the parent obj 
        
        self.initUI()
        
        
    def initUI(self):
        
        # exit action does not work well
#        exitAct = QAction(QIcon('exit.png'), '&Exit', self) #action with icon and label
#        exitAct.setShortcut('Ctrl+Q') #shortcut for the action
#        exitAct.setStatusTip('Exit Application') #status tip
#        exitAct.triggered.connect(qApp.quit) #emit trigger signal 
#        
         # add menu
#        self.statusBar()
#        #create a menu bar
#        menuBar = self.menuBar() 
#        fileMenu = menuBar.addMenu('&File')
#        fileMenu.addAction(exitAct) #contain one action to end the app
#        menuBar = self.menuBar()
#        fileMenu = menuBar.addMenu('File')
#        impMenu = QMenu('Import', self)
#        impAct = QAction('Import mail', self)
#        impMenu.addAction(impAct)
#        newAct = QAction('New', self)
#        fileMenu.addAction(newAct)
#        fileMenu.addMenu(impMenu)
        
#        self.statusBar().showMessage('Ready') #from method of QMainWindow, display message on status bar
#        QToolTip.setFont(QFont('SansSerif', 10)) #tool tip font
#        self.setToolTip('This is a <b>QWidget</b> widget') #tooltip for menu, rich text format
        
        #LCD Event driver
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        
#        btn = QPushButton('Button', self)
#        btn.setToolTip('This is a <b>QPushButton</b> widget')
#        btn.resize(btn.sizeHint()) #give a recommend size for button
#        btn.move(50, 50)       
        
        #cannot work well
#        btnQuit = QPushButton('Quit', self)
#        btnQuit.clicked.connect(QCoreApplication.instance().quit) # signal & slot mechanism
#        btnQuit.resize(btnQuit.sizeHint())
#        btnQuit.move(50, 80)
        
        self.setGeometry(300, 300, 900, 600) #locate and set size of window
        #self.resize(900, 600)
        #self.center() #put window in the center
        self.setWindowTitle('Example of Centerialized Window')    
        self.show()
        
    #reimplement the QCloseEvent
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
                                     "Sure to Quit?", QMessageBox.Yes|
                                     QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept() #terminate the application
        else:
            event.ignore()
            
    #put the window in the center of screen
    def center(self):
        qr = self.frameGeometry() #get the rectangle specifying the geometry of the main window
        cp = QDesktopWidget().availableGeometry().center() #figure out the resoultion of monitor, get center point
        qr.moveCenter(cp)  #qr rectangle
        self.move(qr.topLeft()) #two TL point match
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
        


#
#import sys
#from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
#from PyQt5.QtCore import QCoreApplication
#
#class UserLogin(QWidget):
#    
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#        
#        
#    def initUI(self):
#        
#        qbtn = QPushButton('Quit', self)
#        qbtn.clicked.connect(QCoreApplication.instance().quit)
#        qbtn.resize(qbtn.sizeHint())
#        qbtn.move(50,50)
#        
#        self.setGeometry(300, 300, 250, 150)
#        self.setWindowTitle('Quit')
#        self.show()
#        
#        
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv)
#    userManager = UserLogin()
#    sys.exit(app.exec_())


#import sys
#from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
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
#        self.setGeometry(300, 300, 250, 150)        
#        self.setWindowTitle('Message box')    
#        self.show()
#        
#        
#    def closeEvent(self, event): #close event
#        
#        reply = QMessageBox.question(self, 'Message',
#            "Are you sure to quit?", QMessageBox.Yes | 
#            QMessageBox.No, QMessageBox.No)
#
#        if reply == QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()        
#        
#        
#if __name__ == '__main__':
#    
#    app = QApplication(sys.argv)
#    ex = Example()
#    sys.exit(app.exec_())


        