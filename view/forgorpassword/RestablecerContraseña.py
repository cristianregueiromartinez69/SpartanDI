import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QGridLayout
                             )

class RestablecerContraseña(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.label_username = QLabel("Username")
        self.label_nueva_contraseña = QLabel("Nueva Contraseña")
        self.label_confirmar_nueva_contraseña = QLabel("Confirmar nueva contraseña")

        self.txt_username = QLineEdit()
        self.txt_nueva_contraseña = QLineEdit()
        self.txt_confirmar_nueva_contraseña = QLineEdit()

        self.grid_layout.addWidget(self.label_username, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.label_nueva_contraseña, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.label_confirmar_nueva_contraseña, 2, 1, 1, 1)

        self.grid_layout.addWidget(self.txt_username, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_nueva_contraseña, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.txt_confirmar_nueva_contraseña, 3, 1, 1, 1)