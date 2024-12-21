DELIMITER $$
CREATE TRIGGER arsip_barang
AFTER DELETE ON tbl_barang
FOR EACH ROW
BEGIN
    INSERT INTO tbl_arsip_barang (kode_barang, nama_barang, stok, waktu_hapus)
    VALUES (OLD.kode_barang, OLD.nama_barang, OLD.stok, NOW());
END$$
DELIMITER ;