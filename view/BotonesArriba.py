import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton)

class BotonesArriba(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.data_vault = QPushButton("Data Vault")
        self.data_vault.setFixedSize(160,160)

        self.settings = QPushButton("Settings")
        self.settings.setFixedSize(160,160)

        self.help = QPushButton("Help")
        self.help.setFixedSize(160,160)

        self.close = QPushButton("Close")
        self.close.setFixedSize(160,160)

        self.addWidget(self.data_vault)
        self.addWidget(self.settings)
        self.addWidget(self.help)
        self.addWidget(self.close)