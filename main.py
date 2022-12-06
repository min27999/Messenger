import sys
from PyQt5.QtWidgets import QApplication
from chat import MainWindow

app = QApplication(sys.argv)

myWindow = MainWindow()

app.exec_()