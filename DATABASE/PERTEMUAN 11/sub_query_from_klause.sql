#menampilkan seluruh stok barang#
SELECT SUM(total_stok)
FROM (SELECT stok AS total_stok FROM tbl_barang) AS tbl_stok