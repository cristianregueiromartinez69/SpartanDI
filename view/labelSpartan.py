import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton, QLabel)

class LabelSpartan(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.label_spartan = QLabel("SPARTAN PASSWORD PROTECTOR")
        self.label_spartan.setStyleSheet("""
            font-size: 25px;
            font-family: Arial;
            font-weight: bold;
            color: black;
            border-radius: 5px;
            padding: 5px;
        """)

        self.label_spartan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addWidget(self.label_spartan)