import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton, QLabel, QFrame)

class PasswordStrength:
    def __init__(self):
        self.frame = QFrame()

        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(2)

        self.layout = QVBoxLayout()

        self.label_password_strength = QLabel("Password Strength")

        self.label_password_strength.setStyleSheet("""
            font-size: 15px;
            font-family: Arial;
            font-weight: bold;
            color: black;
            border-radius: 5px;
            padding: 5px;
        """)

        self.layout.addWidget(self.label_password_strength)

        self.frame.setLayout(self.layout)

    def get_frame(self):
        return self.frame