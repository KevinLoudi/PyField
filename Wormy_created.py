import sys

from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit

def getPassword():
    text, ok = QInputDialog.getText(None, "User Login", "Password", 
                                    QLineEdit.Password)
    
    if ok and text:
        print("password=%s" % text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    getPassword()