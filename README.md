# IF3152-2021-G04-BosBuy

**Penjelasan singkat mengenai aplikasi**
Sistem BosBuy merupakan aplikasi yang memungkinkan pemesanan dan pembayaran produk-produk perusahaan Bostani secara online. Implementasinya menggunakan desktop app dan untuk saat ini belum di-deploy untuk digunakan secara online (masih lokal)

**Cara menjalankan aplikasi**
1. Pengguna memerlukan PyQt5 pada komputernya untuk menjalankan program. Bagi yang belum memiliki bisa instal pada terminal menggunakan command line 'pip install pyqt5'
2. Pastikan semua source code berada pada folder yang sama dan dapat meng-import PyQt5
3. Program terhubung dengan database MySQL lokal sehingga pengguna perlu mengonfigurasi MySQL secara lokal
4. Pengguna dapat menjalankan XAMPP dan start Apache serta MySQL kemudian menggunakan PHPMyadmin pad localhost
    (pengguna dapat menggunakan metode lain untuk mengonfigurasi MySQL pada localhost dan port yang dikonfigurasi)
5. Pastikan konfigurasi penghubung-penghubung python dengan MySQL pada program main.py sudah tepat
    contoh: 'db = con.connect(host="localhost", user="root",password="",db="users")'
6. Impor file sql ke dalam database MySQL
7. run main.py

**Modul Implementasi**
PJ: Galuh Dipa Bharata 18219100
1. Modul Login
2. Modul Validasi Username dan Password
3. Modul Register
4. Modul Validasi Data Pengguna

PJ: Ghifari Farras Azhar 18219105
1. Modul Menampilkan Katalog
2. Modul Memilih Product
3. Modul Profile

PJ: Handy Zulkarnain 18219060
1. Modul Add to Cart
2. Modul Add to Wishlist
3. Modul See Cart
4. Modul See Wishlist

PJ: Gavriel Benny 18219078
1. Modul Buy Product
2. Modul Payment
3. Modul See Wishlist

**Daftar Tabel Basis Data Implementasi**

Tabel customer
---------------------------------------------------------------------------
| Id Field     | Deskripsi         | Type & length | Boleh NULL | Default |
---------------------------------------------------------------------------
| customer_id  | ID customer       | VARCHAR(150)  | NO         |         |
| name         | nama customer     | VARCHAR(150)  | NO         |         |
| username     | username customer | VARCHAR(150)  | NO         |         |
| email        | surel customer    | VARCHAR(150)  | NO         |         |
| gender       | gender customer   | VARCHAR(150)  | NO         |         |
| address      | alamat customer   | VARCHAR(150)  | NO         |         |
| password     | kata sandi        | VARCHAR(150)  | NO         |         |
| amount       | jumlah uang       | INT(8)        | NO         |         |
| login_status | status login      | VARCHAR(150)  | NO         |         |
---------------------------------------------------------------------------

Tabel product
---------------------------------------------------------------------------
| Id Field    | Deskripsi          | Type & length | Boleh NULL | Default |
---------------------------------------------------------------------------
| idProduct   | ID produk          | VARCHAR(100)  | NO         |         |
| productName | nama produk        | VARCHAR(100)  | NO         |         |
| category    | kategori produk    | VARCHAR(100)  | NO         |         |
| price       | harga produk       | INT(11)       | NO         |         |
| stock       | jumlah stok produk | INT(11)       | NO         |         |
---------------------------------------------------------------------------

Tabel tbl_cart
---------------------------------------------------------------------------
| Id Field    | Deskripsi          | Type & length | Boleh NULL | Default |
---------------------------------------------------------------------------
| id_user_    | ID customer        | VARCHAR(8)    | NO         |         |
| id_product  | ID produk          | VARCHAR(8)    | NO         |         |
| nama_barang | nama produk        | VARCHAR(50)   | NO         |         |
| quantity    | jumlah produk      | INT(8)        | NO         |         |
| harga_total | harga total        | INT(50)       | NO         |         |
---------------------------------------------------------------------------

Tabel tbl_wishlist
---------------------------------------------------------------------------
| Id Field    | Deskripsi          | Type & length | Boleh NULL | Default |
---------------------------------------------------------------------------
| id_user_    | ID customer        | VARCHAR(8)    | NO         |         |
| id_product  | ID produk          | VARCHAR(8)    | NO         |         |
| nama_barang | nama produk        | VARCHAR(50)   | NO         |         |
| quantity    | jumlah produk      | INT(8)        | NO         |         |
| harga_total | harga total        | INT(50)       | NO         |         |
---------------------------------------------------------------------------