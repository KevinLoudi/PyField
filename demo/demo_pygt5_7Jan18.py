# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:05:33 2018

@author: kevin
"""

import sys
from PyQt5.QtCore import (Qt, QObject, pyqtSignal)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication, QGridLayout, QLabel, QMessageBox,
    QPushButton, QMainWindow)

class Communicate(QObject):
    closeApp = pyqtSignal() #a new signal called closeApp

class Example(QMainWindow):  #QWidget
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
#        #event source and send
#        lcd = QLCDNumber(self) #lcd number
#        sld = QSlider(Qt.Horizontal, self) #slider
#        vbox = QVBoxLayout()
#        vbox.addWidget(lcd)
#        vbox.addWidget(sld)
#        self.setLayout(vbox)
#        sld.valueChanged.connect(lcd.display) #event to lcd
        
        #label to track the mouse position
#        grid = QGridLayout()
#        grid.setSpacing(10)
#        x = 0
#        y = 0
#        self.text = "x: {0}, y: {1}".format(x, y)
#        self.label = QLabel(self.text, self) #display coordinates in QLabel
#        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
#        self.setMouseTracking(True) #enable mouse track
#        self.setLayout(grid)
        
        #set up two button and track which one was pressed
        #  display status in status-bar
        btn1 = QPushButton("Btn 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Btn 2", self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()
        
        #set up new signal and connect with application close
        # when it is clicked
        self.c = Communicate()
        self.c.closeApp.connect(self.close) #signal closeApp connect to close

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Signal and slot')
        self.show()
        
    def mousePressEvent(self, event):
        self.c.closeApp.emit() #when click window with a mouse pointer, app erminates
        
    def buttonClicked(self):
        #give the name of message sender in the status bar
        sender = self.sender() 
        self.statusBar().showMessage(sender.text() + 'was pressed')
        
    def keyPressEvent(self, e): 
        #terminate application when hit esc
        if e.key() == Qt.Key_Escape:
            self.close()
        
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        
        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Sure to Quit?", QMessageBox.Yes|
                                     QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept() #terminate the application
        else:
            event.ignore()
            
from PyQt5.QtWidgets import (QLineEdit, QInputDialog, QApplication,
                             QFrame, QColorDialog, QVBoxLayout, 
                             QSizePolicy, QFontDialog, QFileDialog,
                             QTextEdit, QAction, QCheckBox)
from PyQt5.QtGui import (QColor, QIcon)

class DialogEx(QWidget): #QWidget
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # layout box
        vbox = QVBoxLayout()
        
        # set up a btn connected with input dialog
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        # set up a btn connected with color sheet
        col = QColor(0,0,0) #default color is black
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 50)
        self.btn.clicked.connect(self.showColorSelectDialog)
        self.frm = QFrame(self)
        #set background color
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130,50,100,100) #230, 150
        
        # set up font selection dialog
        self.btn = QPushButton('Dialog', self)
        self.btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn.move(20, 170)
        self.btn.clicked.connect(self.showFontSelectDialog)
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 170) #230, 170
        
        # set up check-box to change title
        self.cb = QCheckBox('Show Title', self)
        self.cb.move(20, 200) #200 +30
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeTitle)
        
        #set background color with toggle button
        self.col = QColor(0,0,0)
        self.redb = QPushButton('Red', self)
        self.redb.setCheckable(True) #make it checkable
        self.redb.move(20, 230)
        self.redb.clicked[bool].connect(self.setColor)
        self.greenb = QPushButton('Green', self)
        self.greenb.setCheckable(True)
        self.greenb.move(20, 260)
        self.greenb.clicked[bool].connect(self.setColor)
        self.blueb = QPushButton('Blue', self)
        self.blueb.setCheckable(True)
        self.blueb.move(20, 290)
        self.blueb.clicked[bool].connect(self.setColor)
        
        self.square = QFrame(self)
        self.square.setGeometry(130, 230, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        # shape the whole window
        self.setGeometry(300, 300, 800, 750)
        self.setWindowTitle('Input Dialog')
        self.show()
        
    def setColor(self, pressed):
        source = self.sender()
        
        if pressed:
            val = 255
        else:
            val = 0
            
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())
        
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
            
        
    def showFontSelectDialog(self):
        font, ok = QFontDialog.getFont()
        
        if ok:
            self.lbl.setFont(font)
        
    def showColorSelectDialog(self):
        col = QColorDialog.getColor()
        
        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" %col.name())
        
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
#            self.statusBar().showMessage(str(text))
            
# select file through file-select dialog and read into edit
class FileReader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileSelectDialog)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showFileSelectDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\')
    
        if fname[0]:
            f = open(fname[0], 'r')
            
            with f: #read contents of file
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
#    ex = Example()
    ex = DialogEx()
#    ex = FileReader()
    sys.exit(app.exec_())