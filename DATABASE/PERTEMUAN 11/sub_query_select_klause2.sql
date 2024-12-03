#menampilkan jumlah total penjualan#
SELECT nama_barang,
(SELECT SUM(qty) FROM tbl_detailtransaksi
WHERE tbl_detailtransaksi.kode_barang =
tbl_barang.kode_barang) AS total_penjualan
FROM tbl_barang	