import sys
from PyQt5.QtWidgets import QApplication
from GUI import GUI
# Test
app = QApplication(sys.argv)
chattings = ['Music', 'Movie', 'Animal', 'Tech']
gui = GUI(chattings)
sys.exit(app.exec_())