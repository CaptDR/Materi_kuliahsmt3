SELECT 
SUM(stok) AS stok_hari_ini
FROM (
SELECT kode_barang, nama_barang, stok FROM
tbl_barang) subquery