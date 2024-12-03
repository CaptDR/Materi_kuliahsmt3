#menampilkan total jumlah barang yg sudah dilakukan pengadaan#
SELECT nama_barang, 
(SELECT sum(jumlah) AS jumlah_brg
FROM tbl_detail_pengadaan
WHERE tbl_detail_pengadaan.kode_barang =
tbl_barang.kode_barang) AS tbl_jmlpengadaan
FROM tbl_barang;