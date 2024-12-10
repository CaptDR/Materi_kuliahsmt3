#mencari stok barang per kode barang#
DELIMITER $$
CREATE PROCEDURE cek_stok_berdasarkan_kodebrg(
	IN kode_barang_in VARCHAR(10),
	OUT nama_barang_out VARCHAR(100),
	OUT stok_out INT)
BEGIN
	SELECT nama_barang, stok
	INTO nama_barang_out, stok_out
	FROM tbl_barang WHERE kode_barang = kode_barang_in;
END$$
DELIMITER;