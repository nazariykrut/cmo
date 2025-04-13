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

languages = {
    "Англійська": "en", "Польска": "pl",
"Японьска": "ja", "Французька": "fr",
"Німецька": "de", "Іспаньська": "es",
"Італийська": "it", "Португальска": "pt",
"Китайська (спрощена)": "zh-cn", "Корейська": "ko",
"Турецька": "tr", "Голандська": "nl", "Шведьска": "sv"
}

for lang_name in languages:
    translatetext.addItem(lang_name,languages[lang_name])


text = QLabel("Введіть текст")
text1 = QTextEdit()
trans = QComboBox()

for lang_name in languages:
    trans.addItem(lang_name,languages[lang_name])


tex = QLabel("Наш переклад")
tex1 = QTextEdit()

col1 = QVBoxLayout()

col1.addWidget(translatetext)
col1.addWidget(text)
col1.addWidget(text1)
col1.addWidget(trans)
col1.addWidget(tex)
col1.addWidget(tex1)

window.setLayout(col1)

app.exec()

