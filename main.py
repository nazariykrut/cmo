from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QInputDialog
import sys


app = QApplication([])
window = QWidget()
window.resize(900,600)
window.show()


window.setWindowTitle("perevodka")


translatetext = QTextEdit()

col1 = QVBoxLayout()
col1.addWidget(translatetext)

window.setLayout(col1)





app.exec_()





