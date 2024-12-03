import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton, QLabel)

from BotonesArriba import BotonesArriba
from labelSpartan import LabelSpartan
from Login import Login
from About import About
from Register import  Register
from PasswordStrength import PasswordStrength
from model.conexionDB import ConexionBD
from model.DatosComboPreguntas import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejemplo interfaz')
        self.setFixedSize(800, 800)

        #declaraciones de frames
        self.botones_arriba = BotonesArriba()
        self.label_spartan = LabelSpartan()
        self.login = Login()
        self.about = About()
        self.register = Register()
        self.password_strength = PasswordStrength()

        #click de botones
        self.register.button_register.clicked.connect(self.insert_datos_db)

        #declaracion de base de datos
        self.base = ConexionBD("usuarios.db")
        #self.base.crear_tabla()

        #añadir funcionalidades
        self.register.combo_box_question.addItems(get_questions_secret())

        #declaracion y añadir layouts
        layout_principal = QVBoxLayout()
        layout_secundario = QHBoxLayout()

        layout_vertical_registro_password_strength = QVBoxLayout()
        layout_vertical_registro_password_strength.addWidget(self.register.get_frame())
        layout_vertical_registro_password_strength.addWidget(self.password_strength.get_frame())

        layout_login_register = QVBoxLayout()

        layout_login_register.addWidget(self.login.get_frame())
        layout_login_register.addWidget(self.about.get_frame())

        layout_secundario.addLayout(layout_login_register)
        layout_secundario.addLayout(layout_vertical_registro_password_strength)

        layout_principal.addLayout(self.botones_arriba)
        layout_principal.addLayout(self.label_spartan)
        layout_principal.addLayout(layout_secundario)


        container_principal = QWidget()

        container_principal.setLayout(layout_principal)

        self.setCentralWidget(container_principal)
        self.show()


    def insert_datos_db(self):
        print("aqui estoy")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec()
