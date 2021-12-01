
print('hello world - ini adalah feature gavriel')

from os import name
import sys
import uuid
from xml.etree.ElementTree import register_namespace
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
import mysql.connector as con

class payment_form(QDialog):
    def __init__(self):
        super(payment_form, self).__init__()
        loadUi("pay.ui",self)
        self.button1.clicked.connect(self.payment)

    def payment(self):
        db = con.connect(host="localhost", user="root",password="",db="rpl")
        cursor = db.cursor()
        cursor.execute("select * from user where userId='"+ '234' +"'")
        result = cursor.fetchone() #buat check colect data, kalau gaada data disini, berarti username dan password tidak valid
        if result:
            cursor.execute("UPDATE user SET balance = balance - 20000 WHERE userId = '234'")
            db.commit()
            widget.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "Payment Output", "Payment Failed")

class showSuccess(QDialog):
    def __init__(self):
        super(showSuccess, self).__init__()
        loadUi("pay2.ui",self)

    def show_success(self):
        widget.setCurrentIndex(1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() #buat load semua class kedalam widgetnya
#jadi ktia bisa masukin semua interface yg udah dibuat ke dalam widget

payment_form = payment_form()
success_page = showSuccess()
widget.addWidget(payment_form) # current index 0
widget.addWidget(success_page) #current index 1

widget.setCurrentIndex(0)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

app.exec_()

