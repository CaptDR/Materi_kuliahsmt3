CREATE TABLE tbl_arsipbarang(
id_arsip INT AUTO_INCREMENT PRIMARY KEY,
kode_barang VARCHAR(10) NOT NULL,
nama_barang VARCHAR(100) NOT NULL,
stok INT NOT NULL,
waktu_hapus DATETIME NOT NULL);