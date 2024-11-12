CREATE TABLE tbl_barang(
kode_barang VARCHAR(10) PRIMARY KEY,
nama_barang VARCHAR(50),
harga_satuan INT,
stok INT NOT NULL,
harga_jual INT NOT NULL)