CREATE TABLE tbl_backup_barang (
  kode_barang  varchar(20) NOT NULL,
  nama_barang  varchar(50) DEFAULT NULL,
    harga_jual  int DEFAULT NULL,
   stok  int DEFAULT NULL,
   harga_pengadaan  int DEFAULT NULL,
   tgl_backup TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)