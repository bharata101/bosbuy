from os import name
import sys
import uuid
from xml.etree.ElementTree import register_namespace
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
import mysql.connector as con
from uuid import uuid4
import logo

class Login_Form(QDialog):
    def __init__(self):
        super(Login_Form, self).__init__()
        loadUi("login-form.ui",self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_reg)

    def login(self):
        #harus connect text box 
        user_name = self.tb1.text()
        password = self.tb2.text()
        # karna run di local, jadi localhost
        db = con.connect(host="localhost", user="root",password="",db="users")
        cursor = db.cursor()
        cursor.execute("select * from customer where username='"+ user_name +"' and password='"+ password +"'")
        result = cursor.fetchone() #buat check colect data, kalau gaada data disini, berarti username dan password tidak valid
        self.tb1.setText("")
        self.tb2.setText("")
        if result:
            QMessageBox.information(self, "Login Output", "Login Successfully!")
            widget.setCurrentIndex(2)
        else:
            QMessageBox.information(self, "Login Output", "Invalid!, Username or Password Incorrect!")
    
    def show_reg(self):
        widget.setCurrentIndex(1) #registration form


class Regist_Form(QDialog):
    def __init__(self):
        super(Regist_Form, self).__init__()
        loadUi("register-form.ui",self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)
    
    def reg(self):
        db = con.connect(host="localhost", user="root",password="",db="users")
        cursor = db.cursor()
        
        customer_id = uuid.uuid4().hex
        name = self.tb3.text()
        username = self.tb4.text()
        email = self.tb5.text()
        gender = self.tb6.text()
        address = self.tb7.text()
        password = self.tb8.text()
        
        
        cursor.execute("select * from customer where username='"+ username +"' and password ='"+ password +"'")
        result = cursor.fetchone()

        self.tb3.setText("")
        self.tb4.setText("")
        self.tb5.setText("")
        self.tb6.setText("")
        self.tb7.setText("")
        self.tb8.setText("")

        if result:
            QMessageBox.information(self, "Regist Output", "User already exist!")
        else:
            cursor.execute("insert into customer values( '"+ customer_id +"', '"+ name +"','"+ username +"','"+ email +"','"+ gender +"','"+ address +"','"+ password +"')")
            QMessageBox.information(self, "Regist Output", "User Created! Welcome!")
            db.commit()

    def show_login(self):
        widget.setCurrentIndex(0) #registration form

class showWelcome(QDialog):
    def __init__(self):
        super(showWelcome, self).__init__()
        loadUi("welcome-page.ui",self)
        # self.b3.clicked.connect(self.reg)
        # self.b4.clicked.connect(self.show_login)

    def show_welcome(self):
        widget.setCurrentIndex(2)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() #buat load semua class kedalam widgetnya
#jadi ktia bisa masukin semua interface yg udah dibuat ke dalam widget

login_Form = Login_Form()
regist_Form = Regist_Form()
welcome_page = showWelcome()
widget.addWidget(login_Form) # current index 0
widget.addWidget(regist_Form) #current index 1
widget.addWidget(welcome_page) #current index 2
widget.setCurrentIndex(0)
widget.setFixedWidth(400)
widget.setFixedHeight(500)
widget.show()

app.exec_()








