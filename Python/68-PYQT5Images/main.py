import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool first GUI")
        self.setGeometry(700,200,500,500)
        label=QLabel(self)
        label.setGeometry(0,0,250,250)

        
        
        pixmap =QPixmap("Drago-Nightmare.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry(self.width(),0,label.width(),label.height())


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    main()