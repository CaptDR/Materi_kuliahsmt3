#Membuat View Untuk Menampilkan stok barang yang habis atau stok = 0#
CREATE VIEW cek_stok AS
SELECT * FROM tbl_barang WHERE
stok=0;