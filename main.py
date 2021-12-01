import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con

ID_USER_GLOBAL = 1

class ProductDetail(QDialog):
    def __init__(self):
        super(ProductDetail, self).__init__()
        loadUi('product-detail.ui', self)
        self.connect()
        self.addToWishlist.clicked.connect(self.addProductToWishlist)
        self.addToCart.clicked.connect(self.addProductToCart)
        self.seeWishlist.clicked.connect(self.see_wishlist)
        self.seeCart.clicked.connect(self.see_cart)

    def connect(self):
        db = con.connect(host='localhost', user='root', password='', db='db_bosbuy')
        cursor = db.cursor()
        # nanti perlu sesuaiin id_user dengan id_user yang login
        cursor.execute("SELECT * FROM tbl_product")
        result = cursor.fetchall()
        for id_produk, nama_barang, harga, stock in result:
            idProduk = id_produk
            self.productName.setText(nama_barang)
            self.productPrice.setText(str(harga))
            self.stockLeft.setText(str(stock))
    
    def addProductToWishlist(self):
        db = con.connect(host='localhost', user='root', password='', db='db_bosbuy')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tbl_product")
        result = cursor.fetchall()
        for id_produk, nama_barang, harga, stock in result:
            idProduk = id_produk
            self.productName.setText(nama_barang)
            self.productPrice.setText(str(harga))
            self.stockLeft.setText(str(stock))
        nama_produk = self.productName.text()
        harga_produk = self.productPrice.text()
        jumlah_stock = self.stockLeft.text()
        quantity = self.quantityBox.value()
        total_price = int(harga_produk)*int(quantity)

        query = f"SELECT COUNT(id_user) FROM tbl_wishlist WHERE id_user = '{ID_USER_GLOBAL}' AND id_product = '{idProduk}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if (result[0] == 0):
            query = f"INSERT INTO tbl_wishlist (id_user, id_product, nama_barang, quantity, harga_total) VALUES ('{ID_USER_GLOBAL}','{idProduk}','{nama_produk}',{quantity},{total_price})"
            cursor.execute(query)
        else:
            query = f"UPDATE tbl_wishlist SET quantity = quantity + {int(quantity)}, harga_total = harga_total + {total_price}"
            cursor.execute(query)

        query = f"UPDATE tbl_product SET stock = stock - {int(quantity)} WHERE id_produk = '{idProduk}'"
        cursor.execute(query)
        db.commit()

        self.quantityBox.setValue(0)
        self.connect()

    def addProductToCart(self):
        db = con.connect(host='localhost', user='root', password='', db='db_bosbuy')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tbl_product")
        result = cursor.fetchall()
        for id_produk, nama_barang, harga, stock in result:
            idProduk = id_produk
            self.productName.setText(nama_barang)
            self.productPrice.setText(str(harga))
            self.stockLeft.setText(str(stock))
        nama_produk = self.productName.text()
        harga_produk = self.productPrice.text()
        jumlah_stock = self.stockLeft.text()
        quantity = self.quantityBox.value()
        total_price = int(harga_produk)*int(quantity)

        query = f"SELECT COUNT(id_user) FROM tbl_cart WHERE id_user = '{ID_USER_GLOBAL}' AND id_product = '{idProduk}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if (result[0] == 0):
            query = f"INSERT INTO tbl_cart (id_user, id_product, nama_barang, quantity, harga_total) VALUES ('{ID_USER_GLOBAL}','{idProduk}','{nama_produk}',{quantity},{total_price})"
            cursor.execute(query)
        else:
            query = f"UPDATE tbl_cart SET quantity = quantity + {int(quantity)}, harga_total = harga_total + {total_price}"
            cursor.execute(query)

        query = f"UPDATE tbl_product SET stock = stock - {int(quantity)} WHERE id_produk = '{idProduk}'"
        cursor.execute(query)
        db.commit()

        self.quantityBox.setValue(0)
        self.connect()

    def see_wishlist(self):
        widget.setCurrentIndex(1)
    
    def see_cart(self):
        widget.setCurrentIndex(2)

class Wishlist(QDialog):
    def __init__(self):
        super(Wishlist, self).__init__()
        loadUi('wishlist.ui', self)
        self.connect()

    def connect(self):
        db = con.connect(host='localhost', user='root', password='', db='db_bosbuy')
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

    def connect(self):
        db = con.connect(host='localhost', user='root', password='', db='db_bosbuy')
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


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
productDetail = ProductDetail()
wishlist = Wishlist()
cart = Cart()
widget.addWidget(productDetail)
widget.addWidget(wishlist)
widget.addWidget(cart)
widget.setCurrentIndex(0)
widget.setFixedWidth(1600)
widget.setFixedHeight(900)
widget.show()

app.exec_()