import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton, QLabel, QGridLayout, QLineEdit, QComboBox, QFrame)

class Register:
    def __init__(self):
        self.frame = QFrame()

        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(2)

        self.grid_layout = QGridLayout()

        self.label_register = QLabel("Register")
        self.label_username = QLabel("Username")
        self.txt_username = QLineEdit()

        self.label_password = QLabel("Password")
        self.label_confirm_password = QLabel("Confirm Password")
        self.txt_password = QLineEdit()
        self.txt_confirm_password = QLineEdit()

        self.label_forename = QLabel("Forename")
        self.label_surname = QLabel("Surname")
        self.txt_forename = QLineEdit()
        self.txt_surname = QLineEdit()

        self.label_combo_question = QLabel("Secret Question")
        self.combo_box_question = QComboBox()

        self.label_secret_answer = QLabel("Secret Answer")
        self.txt_secret_answer = QLineEdit()
        self.button_register = QPushButton("register")

        self.grid_layout.addWidget(self.label_register, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.label_username, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_username, 2, 0, 1, 1)

        self.grid_layout.addWidget(self.label_password, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_password, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.label_confirm_password, 3, 1, 1, 1)
        self.grid_layout.addWidget(self.txt_confirm_password, 4, 1, 1, 1)

        self.grid_layout.addWidget(self.label_forename, 5, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_forename, 6, 0, 1, 1)
        self.grid_layout.addWidget(self.label_surname, 5, 1, 1, 1)
        self.grid_layout.addWidget(self.txt_surname, 6, 1, 1, 1)

        self.grid_layout.addWidget(self.label_combo_question, 7, 0, 1, 1)
        self.grid_layout.addWidget(self.combo_box_question, 8, 0, 1, 1)

        self.grid_layout.addWidget(self.label_secret_answer, 9, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_secret_answer, 10, 0, 1, 1)
        self.grid_layout.addWidget(self.button_register, 11, 1, 1, 1)

        self.frame.setLayout(self.grid_layout)

    def get_frame(self):
        return self.frame
