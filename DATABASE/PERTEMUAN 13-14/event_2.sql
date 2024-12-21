CREATE EVENT backup_barang
ON SCHEDULE EVERY 1 WEEK
DO
    INSERT INTO tbl_backup_barang SELECT * FROM tbl_barang;