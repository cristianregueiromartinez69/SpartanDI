import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout
                             )
from RestablecerContraseña import RestablecerContraseña


class ForgotPassword(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurar contraseña")
        self.setFixedSize(400,400)

        layout_principal = QVBoxLayout()
        restablecer_contraseña = RestablecerContraseña()

        layout_principal.addLayout(restablecer_contraseña)

        container = QWidget()

        container.setLayout(layout_principal)

        container.set



