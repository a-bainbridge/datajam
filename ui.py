from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
import texttochords
import record
import playchords
from matplotlib import pyplot as plt
from matplotlib import figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib import use
import numpy as np

use('QtAgg')

def playevent():
    playchords.play_chords(texttochords.encode(outbox.toPlainText()))

def recordevent():
    inbox.setText(record.listen())
    #inbox.setText(texttochords.decode(record.listolistonotes2indices(texttochords.encode(outbox.toPlainText()))))

def update_plot():
    global a
    ax.cla()
    ax.plot(np.sin(a)*np.sin(np.linspace(0,2*np.pi,100)))
    ax.set_axis_off()
    ax.set_ylim((-1,1),auto=False)
    canvas.draw()
    a+=.2

app = QApplication([])
window = QWidget()
withwave = QVBoxLayout()
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
withwave.addLayout(layout)
fig=figure.Figure(facecolor=(.1,.1,.1))
ax=fig.add_subplot()
canvas=FigureCanvasQTAgg(fig)
ax.plot(np.linspace(0,0,100))
ax.set_axis_off()
ax.set_ylim((-1,1),auto=False)
withwave.addWidget(canvas)
a=0
window.timer=QtCore.QTimer()
window.timer.setInterval(50)
window.timer.timeout.connect(update_plot)
window.timer.start()
window.setLayout(withwave)
window.show()
app.exec()
