from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
import texttochords
import record
import playchords

def playevent():
    playchords.play_chords(texttochords.encode(outbox.toPlainText()))

def recordevent():
    inbox.setText(record.listen())
    #inbox.setText(texttochords.decode(record.listolistonotes2indices(texttochords.encode(outbox.toPlainText()))))

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
playbutton.clicked.connect(playevent)
layout1.addWidget(playbutton)
recordbutton = QPushButton('Record')
recordbutton.clicked.connect(recordevent)
layout2.addWidget(recordbutton)
layout.addLayout(layout1)
layout.addLayout(layout2)
window.setLayout(layout)
window.show()
app.exec()
