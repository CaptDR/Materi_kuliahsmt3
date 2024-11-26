SELECT * FROM tbl_pengadaan WHERE kode_supplier
IN (SELECT kode_supplier FROM supplier 
WHERE alamat_supplier LIKE "Jl. Merdeka%") 