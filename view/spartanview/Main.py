import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout
                             )

from view.spartanview.BotonesArriba import BotonesArriba
from labelSpartan import LabelSpartan
from Login import Login
from view.spartanview.About import About
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
        self.login.login_button.clicked.connect(self.check_login)
        self.botones_arriba.close.clicked.connect(QApplication.quit)

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
        if self.checkEmptyDatos():
            datos = (
                self.register.txt_username.text(),
                self.register.txt_password.text(),
                self.register.txt_forename.text(),
                self.register.txt_surname.text(),
                self.register.combo_box_question.currentText(),
                self.register.txt_secret_answer.text()
            )
            self.base.insertar_usuario(datos)
            print("Datos usuarios insertados correctamente")
            self.limpiar_datos_registro()
        else:
            print("Rellene los campos faltantes")


    def check_login(self):
        username = self.login.text_username.text()
        password = self.login.text_password.text()

        consultaSQL = "SELECT username, password FROM usuarios where username = ? AND password = ?"
        resultados = self.base.consultaConParametros(consultaSQL, (username, password))
        if self.aux_check_login(resultados):
            print("login perfecto, todo coincide")
            self.limpiar_datos_login()
        else:
            print("usuario o contraseña incorrectos")

    def aux_check_login(self, resultados):
        if resultados:
            return True
        else:
            return False


    def checkEmptyDatos(self):
        if self.register.txt_username.text() == "" or self.register.txt_password.text() == "" or self.register.txt_confirm_password.text() == "" or self.register.txt_forename.text() == "" or self.register.txt_surname.text() == "" or self.register.txt_secret_answer.text() == "" or self.register.combo_box_question.currentIndex() == -1 or  self.register.combo_box_question.currentIndex() == 0:
            return False
        elif self.register.txt_password.text() != self.register.txt_confirm_password.text():
            return False
        else:
            return True


    def limpiar_datos_registro(self):
        self.register.txt_username.clear()
        self.register.txt_password.clear()
        self.register.txt_confirm_password.clear()
        self.register.txt_forename.clear()
        self.register.txt_surname.clear()
        self.register.combo_box_question.setCurrentIndex(-1),
        self.register.txt_secret_answer.clear()

    def limpiar_datos_login(self):
        self.login.text_username.clear()
        self.login.text_password.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec()
