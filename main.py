from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, \
    QVBoxLayout, QInputDialog, QMessageBox, QComboBox
import sys


app = QApplication([])
window = QWidget()
window.resize(900,600)
window.show()


window.setWindowTitle("Переводчик")




translatetext = QComboBox()

col1 = QVBoxLayout()
col1.addWidget(translatetext)




window.setLayout(col1)

text1 = QTextEdit()
col2 = QVBoxLayout()
col2.addWidget(text1)

window.setLayout(col2)

app.exec()


