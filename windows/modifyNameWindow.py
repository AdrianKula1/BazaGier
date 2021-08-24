from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton

class modifyNameWindow(QWidget):
    path=""
    modifyElementSignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(modifyNameWindow, self).__init__(parent)
        self.setup()

    def setText(self, data):
        if data != "Nie dodano jeszcze tej zawartości":
            self.nameWindow.setText(data)

    def sendData(self):
        self.modifyElementSignal.emit(self.nameWindow.text())
        self.close()


    def exit(self):
        self.close()

    def setup(self):

        self.nameText = QLabel('Nazwa gry: ', self)
        self.nameWindow = QLineEdit()

        self.applyButton = QPushButton("Zatwierdz", self)
        self.applyButton.clicked.connect(self.sendData)

        self.exitButton = QPushButton("Anuluj", self)
        self.exitButton.clicked.connect(self.exit)

        layout = QGridLayout()
        layout.addWidget(self.nameText, 0, 0)
        layout.addWidget(self.nameWindow, 0, 1)
        layout.addWidget(self.applyButton, 0, 2)
        layout.addWidget(self.exitButton, 1, 2)

        self.setLayout(layout)
        self.setWindowTitle("modyfikuj")
        self.show()