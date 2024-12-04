import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout
                             )
from view.forgorpassword.RestablecerContraseña import RestablecerContraseña


class ForgotPassword(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Restaurar contraseña")
        self.setFixedSize(400, 400)
        layout_principal = QVBoxLayout()
        restablecer_contraseña = RestablecerContraseña()
        layout_principal.addWidget(restablecer_contraseña)
        self.setLayout(layout_principal)




    def cerrar_ventana(self):
        self.hide()



