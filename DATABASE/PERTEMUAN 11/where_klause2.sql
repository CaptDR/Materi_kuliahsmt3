#pembelian barang, ingin menampilkan jumlah stok barang < permintaan#
SELECT * FROM tbl_barang WHERE stok <
(SELECT MAX(qty) FROM tbl_detailtransaksi)