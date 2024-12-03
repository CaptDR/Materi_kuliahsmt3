#ingin insert nama barang di tbl_barang berasal dari tbl_pengadaan#
INSERT INTO tbl_barang(kode_barang,
nama_barang, stok)
SELECT tbl_detail_pengadaan.kode_barang,
"Pop Mie Pedass",
tbl_detail_pengadaan.jumlah
FROM tbl_detail_pengadaan
WHERE tbl_detail_pengadaan.kode_barang
NOT IN (SELECT kode_barang FROM tbl_barang)