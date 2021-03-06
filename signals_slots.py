"""Signals and slots example"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
    # Slot FUNCTION
    if msg.text():
        msg.setText("")
    else:
        msg.setText('HOWDY, WORLD')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
