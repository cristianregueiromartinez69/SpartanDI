import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton, QLabel, QGridLayout, QLineEdit, QFrame)

class Login:
    def __init__(self):
        self.frame = QFrame()

        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(2)

        self.grid_layout = QGridLayout()

        self.label_login = QLabel("Login")
        self.label_username = QLabel("Username")
        self.label_password = QLabel("Password")

        self.text_username = QLineEdit()
        self.text_password = QLineEdit()

        self.forgot_button = QPushButton("Forgot Password")
        self.login_button = QPushButton("Login")

        self.grid_layout.addWidget(self.label_login, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.label_username, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.label_password, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.text_username, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.text_password, 2, 1, 1, 1)

        self.grid_layout.addWidget(self.forgot_button, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.login_button, 3, 2, 1, 1)

        self.frame.setLayout(self.grid_layout)

    def get_frame(self):
        return self.frame