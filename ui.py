from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout

def ondaclick():
    print(outbox.toPlainText())

def recordevent():
    inbox.setText('the decoded message')

app = QApplication([])
window = QWidget()
layout = QHBoxLayout()
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
outbox = QTextEdit('Message to send')
layout1.addWidget(outbox)
inbox = QTextEdit('Recorded message')
layout2.addWidget(inbox)
playbutton = QPushButton('Play')
playbutton.clicked.connect(ondaclick)
layout1.addWidget(playbutton)
recordbutton = QPushButton('Record')
recordbutton.clicked.connect(recordevent)
layout2.addWidget(recordbutton)
layout.addLayout(layout1)
layout.addLayout(layout2)
window.setLayout(layout)
window.show()
app.exec()
