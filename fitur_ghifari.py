import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
import mysql.connector as con

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

class Katalog(QDialog):
    def __init__(self):
        id1 = 0
        id2 = 0
        id3 = 0
        id4 = 0
        super(Katalog, self).__init__()
        loadUi("Katalog.ui",self)
        db = con.connect(host="localhost", user ="root", password="chineslog10", db="user")
        cur = db.cursor()
        cur.execute("select * from product")
        result = cur.fetchall()
        i = 1
        for id, namaProduk, kategori, harga, stok in result:
            if i == 1:
                self.label.setText("  "+namaProduk + "\n"+
                                    "  Kategori: " + kategori + "\n" +
                                    "  Harga: " + str(harga) + "\n" +
                                    "  Stok: " + str(stok))
            elif i == 2:
                self.label_2.setText("  "+namaProduk + "\n"+
                                    "  Kategori: " + kategori + "\n" +
                                    "  Harga: " + str(harga) + "\n" +
                                    "  Stok: " + str(stok))
            elif i == 3:
                self.label_3.setText("  "+namaProduk + "\n"+
                                    "  Kategori: " + kategori + "\n" +
                                    "  Harga: " + str(harga) + "\n" +
                                    "  Stok: " + str(stok))
            elif i == 4:
                self.label_4.setText("  "+namaProduk + "\n"+
                                    "  Kategori: " + kategori + "\n" +
                                    "  Harga: " + str(harga) + "\n" +
                                    "  Stok: " + str(stok))
            else:
                "KURANG LABEL"
            i+=1
        
        self.pushButton.clicked.connect(self.productDetail)
        # self.pushButton2.clicked.connect(self.productDetail(id2))
        # self.pushButton3.clicked.connect(self.productDetail(id3))
        # self.pushButton4.clicked.connect(self.productDetail(id4))
    
    def productDetail(self):
        db = con.connect(host="localhost", user ="root", password="chineslog10", db="user")
        cur = db.cursor()
        cur.execute("select * from customer where status = TRUE")
        result = cur.fetchone()
        profile.label.setText("  Nama: " + str(result[1])+ "\n"+ 
                            "  Email: " + str(result[2])+ "\n"+
                            "  alamat: " + str(result[3])+ "\n"+
                            "  gender: " + str(result[4]))
        widget.setCurrentIndex(1) # nanti ganti jadi index untuk class product-detail yang punya handy


class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profil.ui",self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
katalog = Katalog()
profile = Profile()
widget.addWidget(katalog)
widget.addWidget(profile)
widget.setCurrentIndex(0)
widget.setFixedWidth(720)
widget.setFixedHeight(900)
widget.show()
app.exec_()