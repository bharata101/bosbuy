from os import name
import sys
import uuid
from xml.etree.ElementTree import register_namespace
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
import mysql.connector as con
from uuid import uuid4
import img.logo as logo

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
            cursor.execute(f"UPDATE customer SET login_status='True' WHERE username='{user_name}' AND password='{password}'")
            db.commit()

            widget.setCurrentIndex(2)
            #masuk ke yg ghifari
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
        amount = 2000000
        login_status = "False"

        
        
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
            cursor.execute(f"insert into customer values('{customer_id}','{name}','{username}','{email}','{gender}','{address}','{password}' ,'{amount}','{login_status}')")
            QMessageBox.information(self, "Regist Output", "User Created! Welcome!")
            db.commit()

    def show_login(self):
        widget.setCurrentIndex(0) #registration form

class showWelcome(QDialog):
    def __init__(self):
        super(showWelcome, self).__init__()
        loadUi("welcome-page.ui",self)
        self.b5.clicked.connect(self.show_catalog)
        # self.b4.clicked.connect(self.show_login)

    def show_catalog(self):
        widget.setCurrentIndex(3)

#dibawah ini punya ghifari
class Katalog(QDialog):
    def __init__(self):
        id1 = 0
        id2 = 0
        id3 = 0
        id4 = 0
        super(Katalog, self).__init__()
        loadUi("Katalog.ui",self)
        db = con.connect(host="localhost", user ="root", password="", db="users")
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
        
        self.viewProfile.clicked.connect(self.view_Profile)
        self.pushButton.clicked.connect(self.connect1)
        self.pushButton_2.clicked.connect(self.connect2)
        self.pushButton_3.clicked.connect(self.connect3)
        self.pushButton_4.clicked.connect(self.connect4)
        
    def connect1(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM product WHERE idProduct=1")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            product_detail.productName.setText(nama_barang)
            product_detail.productPrice.setText(str(harga))
            product_detail.category_name.setText(category)
            product_detail.stockLeft.setText(str(stock))
        widget.setCurrentIndex(5)
        return 1        

    def connect2(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM product WHERE idProduct=2")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            product_detail.productName.setText(nama_barang)
            product_detail.productPrice.setText(str(harga))
            product_detail.category_name.setText(category)
            product_detail.stockLeft.setText(str(stock))
        widget.setCurrentIndex(5)
        return 2

    def connect3(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM product WHERE idProduct=3")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            product_detail.productName.setText(nama_barang)
            product_detail.productPrice.setText(str(harga))
            product_detail.category_name.setText(category)
            product_detail.stockLeft.setText(str(stock))
        widget.setCurrentIndex(5)
        return 3

    def connect4(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM product WHERE idProduct=4")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            product_detail.productName.setText(nama_barang)
            product_detail.productPrice.setText(str(harga))
            product_detail.category_name.setText(category)
            product_detail.stockLeft.setText(str(stock))
        widget.setCurrentIndex(5)
        return 4
    
    def view_Profile(self):
        db = con.connect(host="localhost", user ="root", password="", db="users")
        cur = db.cursor()
        cur.execute("select * from customer where login_status = 'True'")
        result = cur.fetchone()

        profil.label.setText("  Nama: " + str(result[1])+ "\n"+ 
                            "  Email: " + str(result[2])+ "\n"+
                            "  alamat: " + str(result[3])+ "\n"+
                            "  gender: " + str(result[4]))
        print(result)
        widget.setCurrentIndex(4) # nanti ganti jadi index untuk class product-detail yang punya handy

    def productDetail(self):
        print("haha blm kelar")

    

class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("Profil.ui",self)
        # self.buat()
        self.exitButton.clicked.connect(self.exit)
    
    # def buat(self):
                   

    def exit(self):
        db = con.connect(host="localhost", user ="root", password="", db="users")
        cur = db.cursor()
        cur.execute(f"UPDATE customer SET login_status='False' WHERE login_status='True'")
        db.commit()
        widget.setCurrentIndex(0)
    

#dibawah ini punya handy

class ProductDetail(QDialog):
    def __init__(self):
        super(ProductDetail, self).__init__()
        loadUi('product-detail.ui', self)
        self.addToWishlist.clicked.connect(self.addProductToWishlist)
        self.addToCart.clicked.connect(self.addProductToCart)
        self.seeWishlist.clicked.connect(self.see_wishlist)
        self.seeCart.clicked.connect(self.see_cart)
        
    def connect(self):
        namaProduk = product_detail.productName.text()
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute(f"SELECT * FROM product WHERE productName='{namaProduk}'")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            product_detail.productName.setText(nama_barang)
            product_detail.productPrice.setText(str(harga))
            product_detail.category_name.setText(category)
            product_detail.stockLeft.setText(str(stock))
        
    
    def addProductToWishlist(self):
        namaProduk = product_detail.productName.text()
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE productName='{namaProduk}'")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            self.productName.setText(nama_barang)
            self.productPrice.setText(str(harga))
            self.category_name.setText(category)
            self.stockLeft.setText(str(stock))
        nama_produk = self.productName.text()
        harga_produk = self.productPrice.text()
        jumlah_stock = self.stockLeft.text()
        quantity = self.quantityBox.value()
        total_price = int(harga_produk)*int(quantity)

        idUserQuery = f"SELECT customer_id FROM customer WHERE login_status='True'"
        cursor.execute(idUserQuery)
        idUser = cursor.fetchone()

        query = f"SELECT COUNT(id_user) FROM tbl_wishlist WHERE id_user = '{idUser[0]}'"
        cursor.execute(query)
        result = cursor.fetchone()


        if (result[0] == 0):
            query = f"INSERT INTO tbl_wishlist(id_user, id_product, nama_barang, quantity, harga_total) VALUES ('{idUser[0]}','{idProduk}','{nama_produk}',{quantity},{total_price})"
            cursor.execute(query)
        else:
            query = f"UPDATE tbl_wishlist SET quantity = quantity + {int(quantity)}, harga_total = harga_total + {total_price}"
            cursor.execute(query)

        query = f"UPDATE product SET stock = stock - {int(quantity)} WHERE idProduct = '{idProduk}'"
        cursor.execute(query)
        db.commit()
        

        self.quantityBox.setValue(0)
        self.connect()

    def addProductToCart(self):
        namaProduk = product_detail.productName.text()
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product WHERE productName='{namaProduk}'")
        result = cursor.fetchall()
        for id_produk, nama_barang, category, harga, stock in result:
            idProduk = id_produk
            self.productName.setText(nama_barang)
            self.productPrice.setText(str(harga))
            self.category_name.setText(category)
            self.stockLeft.setText(str(stock))
        nama_produk = self.productName.text()
        harga_produk = self.productPrice.text()
        jumlah_stock = self.stockLeft.text()
        quantity = self.quantityBox.value()
        total_price = int(harga_produk)*int(quantity)

        idUserQuery = f"SELECT customer_id FROM customer WHERE login_status='True'"
        cursor.execute(idUserQuery)
        idUser = cursor.fetchone()

        query = f"SELECT COUNT(id_user) FROM tbl_cart WHERE id_user = '{idUser[0]}'"
        cursor.execute(query)
        result = cursor.fetchone()


        if (result[0] == 0):
            query = f"INSERT INTO tbl_cart(id_user, id_product, nama_barang, quantity, harga_total) VALUES ('{idUser[0]}','{idProduk}','{nama_produk}',{quantity},{total_price})"
            cursor.execute(query)
        else:
            query = f"UPDATE  tbl_cart SET quantity = quantity + {int(quantity)}, harga_total = harga_total + {total_price}"
            cursor.execute(query)

        query = f"UPDATE product SET stock = stock - {int(quantity)} WHERE idProduct = '{idProduk}'"
        cursor.execute(query)
        db.commit()

        self.quantityBox.setValue(0)
        self.connect()

    def see_wishlist(self):
        widget.setCurrentIndex(6)
    
    def see_cart(self):
        widget.setCurrentIndex(7)

class Wishlist(QDialog):
    def __init__(self):
        super(Wishlist, self).__init__()
        loadUi('wishlist.ui', self)
        self.connect()

    def connect(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM tbl_wishlist")
        result = cursor.fetchall()
        self.tabelWishlist.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tabelWishlist.setRowCount(row_number+1)
            for column_number, data in enumerate(row_data):
                self.tabelWishlist.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

class Cart(QDialog):
    def __init__(self):
        super(Cart, self).__init__()
        loadUi('cart.ui', self)
        self.connect()
        self.addToPayment.clicked.connect(self.show_payment)

    def connect(self):
        db = con.connect(host='localhost', user='root', password='', db='users')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM tbl_cart")
        result = cursor.fetchall()
        self.tabelCart.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tabelCart.setRowCount(row_number+1)
            for column_number, data in enumerate(row_data):
                self.tabelCart.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        

        db.close()

    def show_payment(self):
        widget.setCurrentIndex(8)

# dibawah ini punya gavriel

class payment_form(QDialog):
    def __init__(self):
        super(payment_form, self).__init__()
        loadUi("pay.ui",self)
        self.button1.clicked.connect(self.payment)

    def payment(self):
        db = con.connect(host="localhost", user="root",password="",db="users")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM customer WHERE login_status='True' ")
        result = cursor.fetchall() #buat check colect data, kalau gaada data disini, berarti username dan password tidak valid
        idUser_active = result[0][0]

        cursor.execute(f"SELECT harga_total FROM tbl_cart WHERE id_user = '{idUser_active}'")
        
        paid = cursor.fetchall()
        
        payment_form1.label3_2.setText(str(paid[0][0]))

        if result:
            cursor.execute(f"SELECT harga_total FROM tbl_cart WHERE id_user = '{idUser_active}'")
            result2 = cursor.fetchall()
            cursor.execute(f"UPDATE customer SET amount = amount - {result2[0][0]} WHERE customer_id={idUser_active}")
            db.commit()
            widget.setCurrentIndex(9)
        else:
            QMessageBox.information(self, "Payment Output", "Payment Failed")

class showSuccess(QDialog):
    def __init__(self):
        super(showSuccess, self).__init__()
        loadUi("pay2.ui",self)
        self.goToProfile.clicked.connect(self.go_Profile)

    def show_success(self):
        widget.setCurrentIndex(9)

    def go_Profile(self):
        widget.setCurrentIndex(4)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() #buat load semua class kedalam widgetnya
#jadi ktia bisa masukin semua interface yg udah dibuat ke dalam widget

product_detail = ProductDetail()
login_Form = Login_Form()
regist_Form = Regist_Form()
welcome_page = showWelcome()
catalog = Katalog()
profil = Profile()
wishlist = Wishlist()
cart = Cart()
payment_form1 = payment_form()
success_page = showSuccess()

widget.addWidget(login_Form) # current index 0
widget.addWidget(regist_Form) #current index 1
widget.addWidget(welcome_page) #current index 2
widget.addWidget(catalog) #current index 3
widget.addWidget(profil) #current index 4
widget.addWidget(product_detail) #current index 5
widget.addWidget(wishlist) #6
widget.addWidget(cart) #7
widget.addWidget(payment_form1) # current index 8
widget.addWidget(success_page) #current index 9
widget.setCurrentIndex(0)
widget.setFixedWidth(1600)
widget.setFixedHeight(900)
widget.show()

app.exec_()








